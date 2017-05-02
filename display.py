#import numpy as np
import matplotlib.pyplot as plt
import re

plt.rcdefaults()
plt.suptitle('(CIA FACTBOOK 2016)')

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
	y_data = extract_data(country)
	#y_pos = np.arange(len(groups))
	y_pos = [0, 1, 2, 3, 4]

	ax.bar(y_pos, y_data, align='center', 
	color=set_color, ecolor='black')
	ax.set_xticks(y_pos)
	ax.set_ylim([0,50])
	ax.set_xticklabels(groups)
	#ax.set_ylabel('Percentage')
	ax.set_title('Age of Population in {}'.format(country))

	for i, v in enumerate(y_data):
		ax.text(i - .4, v + .3, str(v) + '%', color=set_color, fontweight='bold')



make_graph("India", "blue", 0)
make_graph("America", "green", 1)
make_graph("China", "red", 2)
make_graph("Japan", "purple", 3)

plt.show()

