from data import _Data
import random
class Tool:
	def __init__(self):
		self.data=_Data()
		self.n=self.data.n
		self.boxsize=self.data.boxsize
	def init_array(self):
	# initlize the array to 0 matrix
		return [[0 for i in range(0,self.n)] for j in range(0,self.n)]
	def type_(self,a):
	#check if a has choices or is certain
		b=[]
		if type(a)==type(b):
			return 1
		return 0
	def del_xy_choice(self,a,b,i,j,k):
	#del choice k base on x-y coordinate i,j
		a[i][j].remove(k)
		if len(a[i][j]) == 1:
			a[i][j] = a[i][j][0]
		self.update(a,b)
	def del_box_choice(self,a,b,i,j,k):
	#del choice k base on 9-box coordinate i,j
		b[i][j].remove(k)
		if len(b[i][j]) == 1:
			b[i][j] = b[i][j][0]
		self.i_update(b,a)
	def check_(self,a,b,i,j):
	#check whether the number in vertex(i,j) is appropriate
		if self.type_(a[i][j]):
			return 1
		for m in range(0,self.n):
			if m == j:
				continue
			if self.type_(a[i][m]):
				continue
			elif a[i][m] == a[i][j]:
				return 0
		for m in range(0,self.n):
			if m == i:
				continue
			if self.type_(a[m][j]):
				continue
			elif a[m][j] == a[i][j]:
				return 0
		p,q=self.map(i,j)
		for m in range(0,self.n):
			if m == q:
				continue
			if self.type_(b[p][m]):
				continue
			elif b[p][m] == a[i][j]:
				g,h = self.i_map(p,m)
				return 0
		return 1
	def check(self,a,b,i,j):
	#check is i row or j column have its all choice k, we only check if it has choice
		if not self.type_(a[i][j]):
			return 0
		if len(a[i][j]) == 1:
			a[i][j]=a[i][j][0]
			return 0
		for k in a[i][j]:
			for m in range(0,self.n):
				if m == j:
					continue
				if self.type_(a[i][m]):
					continue
				elif a[i][m] == k:
					self.del_xy_choice(a,b,i,j,k)
					return 1
			for m in range(0,self.n):
				if m == i:
					continue
				if self.type_(a[m][j]):
					continue
				elif a[m][j] == k:
					self.del_xy_choice(a,b,i,j,k)
					return 1
			p,q=self.map(i,j)
			for m in range(0,self.n):
				if m == q:
					continue
				if self.type_(b[p][m]):
					continue
				elif b[p][m] == k:
					self.del_box_choice(a,b,p,q,k)
					return 1
		return 0
	def checksum(self,a,k):
	#compute the sum of value k that we have filled
		s=0
		b=[]
		for i in range(0,self.n):
			for j in range(0,self.n):
				if not self.type_(a[i][j]):
					if a[i][j] == k:
						s=s+1
				else:
					if len(a[i][j]) == 1 and a[i][j][0] == k:
						s=s+1
		if s == self.n:
			return 1
		elif s > self.n:
			raise Exception('algorithm error')
		else:
			return 0
	def check_contridict(self,a,b):
	#check if there is a contridict
		for i in range(0,self.n):
			for j in range(0,self.n):
				if 0 == self.check_(a,b,i,j):
					return 0
		return 1
	def check3(self,q):
	#check whether 2 vertices in q is in the same row or column
		x1,y1 = self.i_map(q[0][0],q[0][1])
		x2,y2 = self.i_map(q[1][0],q[1][1])
		x3,y3 = self.i_map(q[2][0],q[2][1])
		if x1 == x2 and x2 == x3:
			return 1
		if y1 == y2 and y2 == y3:
			return 1
		return 0
	def check2(self,q):
	#check whether 2 vertices in q is in the same row or column
		x1,y1 = q[0][0],q[0][1]
		x2,y2 = q[1][0],q[1][1]
		x1,y1 = self.i_map(x1,y1)
		x2,y2 = self.i_map(x2,y2)
		if x1 == x2 or y1 == y2:
			return 1
		return 0
	def grid_rc_clear(self,q,a,b,k,i,rc):
	#clear the choices of value k for those vertices that is in the same row or column with the vertices in q except vertices in q
		c=0
		if rc == 0:
		#rc:0 for row, 1 for column
			j = []
			for s in q:
				j.append(s[1])
			for m in range(0,self.n):
				if m in j:
					continue
				if self.type_(a[i][m]) and len(a[i][m]) > 1 and k in a[i][m]:
					self.del_xy_choice(a,b,i,m,k)
					c=c+1
		elif rc == 1:
			j = []
			for s in q:
				j.append(s[0])
			for m in range(0,self.n):
				if m in j:
					continue
				if self.type_(a[m][i]) and len(a[m][i]) > 1 and k in a[m][i]:
					self.del_xy_choice(a,b,m,i,k)
					c=c+1
		self.update(a,b)
		return c
	def clear_k(self,a,b,k):
	#clear the choices of value k for all vertices
		for i in range(0,self.n):
			for j in range(self.n):
				if self.type_(a[i][j]):
					if len(a[i][j]) > 1 and k in a[i][j]:
						a[i][j].remove(k)
		self.update(a,b)
		return 1
	def detect(self,a):
	#check whether a is full
		for i in range(0,self.n):
			for j in range(0,self.n):
				if self.type_(a[i][j]):
					if len(a[i][j]) > 1:
						return 0
		return 1
	def check_column_choice(self,a,b,j):
	#check all location in j column for its choice k
		c=0
		for i in range(0,self.n):
			if self.type_(a[i][j]):
				if self.check(a,b,i,j):
					c=1
		return c
	def check_row_choice(self,a,b,i):
	#check all location in i row for its choice k
		c=0
		for j in range(0,self.n):
			if self.type_(a[i][j]):
				if self.check(a,b,i,j):
					c=1
		return c
	def check_box_choice(self,a,b,r):
	#search location in r big box for value k
		x=0
		for l in range(0,self.n):
			if self.type_(b[r][l]):
				i,j=i_map(r,l)
				if self.check(a,b,i,j):
					c=1
		return c
	def choose_f_queue(self,a,b):
	#choose the vertices that only have 2 choices and are in list b for hypothesis
		q=[]
		for i in range(0,self.n):
			for j in range(0,self.n):
				if self.type_(a[i][j]) and len(a[i][j]) == 2 :
					for k in a[i][j]:
						if (i,j,k) in b:
							q.append((i,j,k))
		return q
	def f_choose_queue(self,a):
	#initlize the choose queue for hypothesis
		q=[]
		for i in range(0,self.n):
			for j in range(0,self.n):
				if self.type_(a[i][j]) and len(a[i][j]) >= 2:
					for k in a[i][j]:
						q.append((i,j,k))
		return q
	def choose_e_queue(self,a,b):
	#get all vertices that have choices and in list b for hypothesis
		q=[]
		for i in range(0,self.n):
			for j in range(0,self.n):
				if self.type_(a[i][j]) and len(a[i][j]) >= 2:
					for k in a[i][j]:
						if (i,j,k) in b:
							q.append((i,j,k))
		return q
	def select(self,q):
	#choose a vertexin list q with a value in random
		l=len(q)
		n=random.randint(0,l-1)
		return q[n]
	def choose_coordinate(self,a,b):
	#choose a vertex in list k with a value in random, we firstly choose verte that only have 2 choice to simplify
		q=self.choose_f_queue(a,b)
		if q:
			return self.select(q)
		q=self.choose_e_queue(a,b)
		if q:
			return self.select(q)
	def way3(self,q,a,b):
		xy=[]
		if self.check3(q,a,b):
			i,rc=self.rc3(q)
			for s in q:
				x,y=self.i_map(s[0],s[1])
				xy.append((x,y))
			if self.grid_rc_clear(xy,a,b,k,i,rc):
				return 1
		return 0
	def way2(self,q,a,b):
		xy=[]
		if self.check2(q,a,b):
			i,rc=self.rc2(q)
			for s in q:
				x,y=self.i_map(s[0],s[1])
				xy.append((x,y))
			if self.grid_rc_clear(xy,a,b,k,i,rc):
				return 1
		return 0
	def grid_sum(self,b,i,k):
	#compute the sum of value k in i-th grid
		s=[]
		for j in range(0,self.n):
			if b[i][j] == k:
				s.append((i,j))
		return s
	def rc2(self,q):
	#compute column or row that the vertices in q is in, if 0, is row; if 1, is column
		x1,y1=self.i_map(q[0][0],q[0][1])
		x2,y2=self.i_map(q[1][0],q[1][1])
		if x1 == x2:
			return x1,0
		if y1 == y2:
			return y1,1
	def rc3(self,q):
	#compute column or row that the vertices in q is in, if 0, is row; if 1, is column
		x1,y1=self.i_map(q[0][0],q[0][1])
		x2,y2=self.i_map(q[1][0],q[1][1])
		x3,y3=self.i_map(q[2][0],q[2][1])
		if x1 == x2 and x2 == x3:
			return x1,0
		if y1 == y2 and y2 == y3:
			return y1,1
	def map(self,i,j):
	#map x-y coordinate to 9-box grid coordinate
		a=int(i/self.boxsize)
		b=int(j/self.boxsize)
		#a,b is big box's coordinate
		c=i%self.boxsize
		d=j%self.boxsize
		#c,d is small box's corrdinate
		l=self.boxsize*c+d
		r=self.boxsize*a+b
		return r,l
	def copy(self,a,na):
	#copy a to na
		for i in range(0,self.n):
			for j in range(0,self.n):
				if self.type_(a[i][j]) and len(a[i][j]) > 1:
					na[i][j]=a[i][j][:]
				else:
					na[i][j]=a[i][j]
	def i_map(self,r,l):
	#map 9-box grid coordinate to x-y coordinate
		c=int(l/self.boxsize)
		a=int(r/self.boxsize)
		d=l%self.boxsize
		b=r%self.boxsize
		i=self.boxsize*a+c
		j=self.boxsize*b+d
		return i,j
	def update(self,a,b):
	#from x-y coordinate update 9-box grid coordinate
		for i in range(0,self.n):
			for j in range(0,self.n):
				p,q=self.map(i,j)
				if b[p][q] == a[i][j]:
					continue
				if self.type_(a[i][j]):
					b[p][q]=a[i][j][:]
				else:
					b[p][q]=a[i][j]
	def i_update(self,a,b):
	#from 9-box grid coordinate update x-y coordinate
		for i in range(0,self.n):
			for j in range(0,self.n):
				p,q=self.i_map(i,j)
				if b[p][q] == a[i][j]:
					continue
				if self.type_(a[i][j]):
					b[p][q]=a[i][j][:]
				else:
					b[p][q]=a[i][j]

