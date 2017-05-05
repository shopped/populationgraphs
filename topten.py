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

''' rtrn format: [1.0, 32.4, 2.0, 37.4, 3.0, 56.32...]'''
def create_array(age_range):
	rtrn = []
	with open('parsed_age_data.json') as data:
		d = json.load(data)
		for i in range(0, len(d)):
			rtrn.append(float(i)) # 1.0, 2.0, 3.0, @ [0], [2], [4]. THIS SERVES AS AN INDEX KEY!!!
			percentage = d[i][age_range] #gets 32.43%
			rtrn.append(float(percentage[:len(percentage)-1])) # 32.43, 53.12, 5.46 @ [1], [3], [5]
	return rtrn

'''rtrn a sorted array format: [32.0, 61.22, 3.0, 56.32, 132.0, 54.28...]'''
def sort_by_least_age_range(array):
	a = array
	for i in range(3, len(a), 2): # skips the first, i is the PERCENTAGE
		for j in range(1, i, 2): # j iterates through the sorted PERCENTAGES
			if a[i] < a[j]:
				a.insert(j-1, a.pop(i)) # this moves the PERCENTAGE
				a.insert(j-1, a.pop(i)) # this moves the INDEX KEY
	return a

'''could factor this out'''
def sort_by_greatest_age_range(array):
	a = array
	for i in range(3, len(a), 2):
		for j in range(1, i, 2):
			if a[i] > a[j]:
				a.insert(j-1, a.pop(i))
				a.insert(j-1, a.pop(i))
	return a

'''prints in the terminal'''
def print_top_x(array, age_range, num=0):
	a = array
	if num==0: # if no number is specified
		num = int(len(array)/2) # prints everything
	print('Age Range: {}'.format(age_range))
	with open('parsed_age_data.json') as data:
		d = json.load(data)
		for i in range(0, num*2, 2):
			index_key = (int)(a[i]) #
			country = d[index_key]["Country"]
			sys.stdout.write('{}. {}\n\t\t\t\t\t{}%'.format(int(i/2+1), country, a[i+1])) # 1: Azerbajan \n 32.60%
			sys.stdout.write('\n')
		sys.stdout.write('\n\n')
		sys.stdout.flush()


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
			self.d["most"+item]["command"] = lambda: self.button_press(item, int(self.entry.get()), True)
			self.d["most"+item].pack(side=tk.LEFT)
			self.d["least"+item] = tk.Button(x, text='least')
			self.d["least"+item]["command"] = lambda: self.button_press(item, int(self.entry.get()), False)
			self.d["least"+item].pack(side=tk.LEFT)
			x.pack()

	def button_press(self, action, num=10, greatest=True):
		if greatest:
			array = sort_by_greatest_age_range(create_array(action))
		else:
			array = sort_by_least_age_range(create_array(action))
		print_top_x(array, action, num)

root = tk.Tk()
app = Application(root)
app.mainloop()