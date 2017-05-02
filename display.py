import numpy as np
import matplotlib.pyplot as plt
import re

plt.rcdefaults()
figure, ax = plt.subplots()

regex = (r'\d{,2}\.?\d{,2}%')

def extract_data(country):
	with open('parsed_age_data.txt') as text:
		matching = [s for s in text if country in s]
		strdata = re.findall(regex, matching[0])
		intdata = []
		for line in strdata:
			intdata.append(float(line[:len(line)-1]))
		return intdata

America = extract_data("America")
China = extract_data("China")
India = extract_data("India")

# data here
groups = (
"0-14 years",
"15-24 years",
"25-54 years",
"55-64 years",
"65 and over"
)

y_pos = np.arange(len(groups))
performance = America

ax.bar(y_pos, performance, align='center', 
	color='green', ecolor='blue')
ax.set_xticks(y_pos)
ax.set_ylim([0,100])
ax.set_xticklabels(groups)
ax.set_ylabel('Percentage')
ax.set_title('Age of Population in America')

plt.show()

