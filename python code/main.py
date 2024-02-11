from tool import Tool
from data import _Data
from indata import In_data
import time
#import torch
class sudoku:
	def __init__(self):
		self.data=In_data()
		self.tool=Tool()
		self.n=self.data.n
		self.boxsize=self.data.boxsize
		self.save_path=self.data.save_path
		self.xy=self.data.array
		print('The puzzle to solve:')
		self.r_print(self.xy)
		self.choice=[i for i in range(1,self.n+1)]
		for i in range(0,self.n):
			for j in range(0,self.n):
				if not self.xy[i][j]:
					self.xy[i][j] = self.choice[:]
		self.box=[[0 for i in range(0,self.n)] for j in range(0,self.n)]
		self.tool.update(self.xy,self.box)
		self.out=[]#the number that is enough
		self.stop=0
	def list_str(self,a):
		p=[]
		for i in range(0,self.n):
			c=[]
			for j in range(0,int(self.n/self.boxsize)):
				c.append(' '.join(map(str,a[i][j*self.boxsize:(j+1)*self.boxsize])))
				d='\t'.join(c)
			p.append(d)
		c=[]
		for i in range(0,int(self.n/self.boxsize)):
			c.append('\n'.join(p[i*self.boxsize:(i+1)*self.boxsize]))
		pf='\n\n'.join(c)
		return pf
	def r_print(self,a):
		pf=self.list_str(a)
		print(pf)
	def zero(self,a):
		q=self.tool.init_array()
		for i in range(0,self.n):
			for j in range(0,self.n):
				if self.tool.type_(a[i][j]) and len(a[i][j]) > 1:
					q[i][j] = 0
				elif self.tool.type_(a[i][j]) and len(a[i][j]) == 1:
					q[i][j] = a[i][j][0]
				else:
					q[i][j] = a[i][j]
		return q
	def save(self):
		with open(self.save_path,'w') as f:
			f.write(self.list_str(self.xy))
	def solve(self):
		while not self.stop:
			self.operation()
		if self.stop == 1:
			print("The puzzle's solution:")
			self.r_print(self.xy)
			print("The window will be closed after 30 seconds")
			time.sleep(30)
			self.save()
		elif self.stop == 2 :
			print("The puzzle has no solution")
		return 1
	def operation(self):
		self.update_out(self.xy,self.box,self.out)
		if not self.simple_check(self.xy,self.box):
			self.update_out(self.xy,self.box,self.out)
			if self.stop:
				return 1
			queue = self.tool.f_choose_queue(self.xy)
			if self.magic(self.xy,self.box):
				return 0
			if self.hypothesis(self.xy,self.box,self.out,queue,0,0,0,0) != 1:
				self.stop=2
	def update_out(self,a,b,out):
		for k in range(1,self.n+1):
			if self.tool.checksum(a,k) and k not in out:
				out.append(k)
		for k in out:
			self.tool.clear_k(a,b,k)
	def magic(self,a,b):
		c=0
		for i in range(0,self.n):
			for k in range(1,self.n+1):
				q=self.tool.grid_sum(b,i,k)
				if len(q) == 3:
					if self.tool.way3(q,a,b,k):
						c=c+1
				if len(q) == 2:
					if self.tool.way2(q,a,b,k):
						c=c+1
		return c
	def hypothesis(self,a,b,out,queue,l,m,n,c):
		#c is the times we have hypothesis
		while queue:
			if self.stop:
				return 1
			if queue == []:
				return l,m,n
			T_queue = self.tool.choose_f_queue(a,queue)
			if T_queue:
				l0 = self.tool.choose_coordinate(a,T_queue)
				i,j,k = l0[0],l0[1],l0[2]
			else:
				l0 = self.tool.choose_coordinate(a,queue)
				i,j,k = l0[0],l0[1],l0[2]
			new_a = self.tool.init_array()
			self.tool.copy(a,new_a)
			new_b = self.tool.init_array()
			new_a[i][j]=k
			self.tool.update(new_a,new_b)
			self.subhypothesis(new_a,new_b,out,queue,i,j,k,c+1)
			if self.stop:
				return 1
		return l,m,n
	def subhypothesis(self,a,b,out,queue,i,j,k,c):
		hout=out[:]
		while self.tool.check_contridict(a,b):
			self.update_out(a,b,hout)
			if not self.simple_check(a,b):
				if self.stop:
					return 1
				self.update_out(a,b,hout)
				queue_ = self.tool.f_choose_queue(a)
				if self.magic(a,b):
					continue
				if self.hypothesis(a,b,hout,queue_,i,j,k,c) != 1:
					break
			if self.stop:
				return 1
			if self.tool.detect(a) and self.tool.check_contridict(a,b):
			#The hypothesis is right
				self.stop = 1
				self.xy=a
				return 1
		queue.remove((i,j,k))
		return 0
	def simple_check(self,a,b):
		#check every grid every choice,if we delete one choice then return 1
		c=0
		self.tool.check_row_choice(a,b,5)
		self.tool.check(a,b,0,5)
		for j in range(0,self.n):
			if self.tool.check_row_choice(a,b,j):
				c=c+1
		if self.tool.detect(self.xy):
			self.stop=1
		if c:
			return 1
		else:
			return 0
#device = torch.device("cuda:0")
s=sudoku()
s.solve()


#s.solve().to(device)