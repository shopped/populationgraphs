#import numpy as np
import matplotlib.pyplot as plt
import re

plt.rcdefaults()

regex = (r'\d{,2}\.?\d{,2}%')

def extract_data(country):
	with open('parsed_age_data.txt') as text:
		matching = [s for s in text if country in s]
		strdata = re.findall(regex, matching[0])
		intdata = []
		for line in strdata:
			intdata.append(float(line[:len(line)-1]))
		return intdata

# axis label here
groups = (
"0-14 years",
"15-24 years",
"25-54 years",
"55-64 years",
"65 and over"
)

def make_graph(country, set_color):
	figure, ax = plt.subplots()
	y_data = extract_data(country)
	#y_pos = np.arange(len(groups))
	y_pos = [0, 1, 2, 3, 4]

	ax.bar(y_pos, y_data, align='center', 
	color=set_color, ecolor='black')
	ax.set_xticks(y_pos)
	ax.set_ylim([0,100])
	ax.set_xticklabels(groups)
	ax.set_ylabel('Percentage')
	ax.set_title('Age of Population in {}'.format(country))




make_graph("America", "green")
#make_graph("China", "red")
#make_graph("India", "blue")

plt.show()

