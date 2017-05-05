#import numpy as np
import matplotlib.pyplot as plt
import re

regex = (r'\d{,2}\.?\d{,2}%')


def extract_data(country):
	with open('parsed_age_data.json') as text:
		matching = [s for s in text if country in s]
		strdata = re.findall(regex, matching[0])
		intdata = []
		for line in strdata:
			intdata.append(float(line[:len(line)-1])) # Creates an array with the five age percentages, in float form
		return intdata

# axis label here
groups = (
"0-14",
"15-24",
"25-54",
"55-64",
"65+"
)

TOTAL_GRAPHS = 4
t = TOTAL_GRAPHS

def make_graph(country, set_color, i):
	ax = plt.subplot2grid((t, t), (0, i), rowspan=t)
	x_data = extract_data(country)
	#y_pos = np.arange(len(groups))
	x_pos = [0,1,2,3,4]

	ax.bar(x_pos, x_data, align='center', 
	color=set_color, ecolor='black')
	ax.set_xticks(x_pos)
	ax.set_ylim([0,50])
	ax.set_xticklabels(groups)
	ax.set_title(country)

	for i, v in enumerate(x_data): #gets x and y for the value of the bar chart
		ax.text(i - .4, v + .3, str(v) + '%', color=set_color, fontweight='bold') #puts percentage of text above graph


def make_four_graphs(array):
	ct = 0
	colors = ["blue", "green", "red", "purple"]
	for i in range(len(array)):
		make_graph(array[i], colors[ct], i)
		ct += 1

''' CALL FROM EXTERNAL PROGRAM LIKE THIS
from display.py import graph4
a = ["India", "America", "China", "Japan"]
graph(a)
'''
def graph4(array):
	plt.rcdefaults()
	plt.suptitle('Age of Population')
	make_four_graphs(array)
	plt.show()

def main():
	graph4(["India", "America", "China", "Japan"])

if __name__ == '__main__':
	main()