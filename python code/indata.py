from data import _Data
import json
class In_data:
	def __init__(self):
		self.data=_Data()#输入默认值
		self.config_path=self.data.config
		self.n=self.data.n
		self.array=[[0 for i in range(0,self.n)] for j in range(0,self.n)]
		self.path=self.data.path
		self.input_path=self.data.t_path
		self.input_class=self.data.input_class
		self.boxsize=self.data.boxsize
		if self.config():
			self.Input_data()
		else:
			self.Indata()
	def config(self):
		with open(self.config_path) as f:
			w=json.load(f)
			if w :
				self.n=w['n']
				self.path=w['path']
				self.boxsize=w['boxsize']
				self.input_class=w['input_class']
				self.input_path=w['input_path']
				self.save_path=w['save_path']
			else:
				f.close()
				return 0
		f.close()
		return 1
	def Input_data(self):
		if self.input_class:
			self.Transform_data()
		else:
			self.Indata()
	def Indata(self):
		with open(self.path) as f:
			coordinate = json.load(f)
			for c in coordinate:
				if c :
					self.array[c[0]][c[1]] = c[2]
		f.close()
	def Transform_data(self):
		with open(self.input_path) as f:
			l0 = list(f)
			while '\n' in l0:
				l0.remove('\n')
			c1=0
			for i in l0:
				c2 = 0
				l1 = i.split('\t')
				for j in l1:
					l2 = j.split(' ')
					for i in range(0,3):
						self.array[c1][c2+i] = int(l2[i])
					c2 = c2 + 3
				c1 = c1 + 1
		f.close()