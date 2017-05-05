import re
import json
import tkinter as tk
import sys

#from display import extract_data as ed

ONE = "0-14 years:"
TWO = "15-24 years:"
THREE = "25-54 years:"
FOUR = "55-64 years:"
FIVE = "65 years and over:"
regex = (r'\d{,2}\.?\d{,2}%')

def first_ten_countries():
	with open('parsed_age_data.json') as data:
		d = json.load(data)
		print(type(d))
		for i in range(0, 9):
			print(d[i][ONE])

def create_array(age_range):
	rt = []
	with open('parsed_age_data.json') as data:
		d = json.load(data)
		for i in range(0, len(d)):
			rt.append(float(i))
			percentage = d[i][age_range]
			rt.append(float(percentage[:len(percentage)-1]))
	return rt

def sort_by_least_age_range(array, age_range):
	a = array
	for i in range(3, len(a), 2):
		for j in range(1, i, 2):
			if a[i] < a[j]:
				a.insert(j-1, a.pop(i))
				a.insert(j-1, a.pop(i))
	return a

def sort_by_greatest_age_range(array, age_range):
	a = array
	for i in range(3, len(a), 2):
		for j in range(1, i, 2):
			if a[i] > a[j]:
				a.insert(j-1, a.pop(i))
				a.insert(j-1, a.pop(i))
	return a

def print_top_x(array, age_range, num=0):
	a = array
	if num==0:
		num = int(len(array)/2)
	print('Age Range: {}'.format(age_range))
	with open('parsed_age_data.json') as data:
		d = json.load(data)
		for i in range(0, num*2, 2):
			index = (int)(a[i])
			c = d[index]["Country"]
			sys.stdout.write('{}.: {}\n%: {}'.format(int(i/2+1), c, a[i+1]))
			sys.stdout.write('\n')
		sys.stdout.write('\n\n')
		sys.stdout.flush()


def menu():
	root = tk.Tk()

	root.mainloop()

class Application(tk.Frame):

	def __init__(self, master=None):
		super().__init__(master)
		self.pack()
		self.create_widgets()

	def create_widgets(self):
		self.d = {}
		self.mainlabel = tk.Label(self, text="Number of Countries to List").pack(side=tk.LEFT)
		self.entry = tk.Entry(self)
		self.entry.insert(0, "10")
		self.entry.pack(side=tk.LEFT)
		for item in (ONE, TWO, THREE, FOUR, FIVE):
			x = self.d["frame"+item] = tk.Frame(self, width=250, height=100)
			self.d["label"+item] = tk.Label(x, text=item).pack(side=tk.LEFT)
			self.d["most"+item] = tk.Button(x, text='most')
			self.d["most"+item]["command"] = lambda: self.button_press("{}".format(item), int(self.entry.get()), True)
			self.d["most"+item].pack(side=tk.LEFT)
			self.d["least"+item] = tk.Button(x, text='least')
			self.d["least"+item]["command"] = lambda: self.button_press(item, int(self.entry.get()), False)
			self.d["least"+item].pack(side=tk.LEFT)
			x.pack()

	def button_press(self, action, num=10, greatest=True):
		if greatest:
			array = sort_by_greatest_age_range(create_array(action), action)
		else:
			array = sort_by_least_age_range(create_array(action), action)
		print_top_x(array, action, num)

root = tk.Tk()
app = Application(root)
app.mainloop()