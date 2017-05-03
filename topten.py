import re
import json
import operator as o

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

def sort_by_greatest_age_range(age_range):
	#parse oldest data
	with open('parsed_age_data.json') as data:
		d = json.load(data)
		for i in range(1, len(d)):
			for j in range(0, i-1):
				if d[i][age_range] > d[j][age_range]:
					d[i].index = 0
	#do a sort!


def sort_by_smallest_age_range(age_range):
	with open('parsed_age_data.json') as data:
		d = json.load(data)
		dd = dict(d)
		print(dd)
		#sorted(d, key= o.attrgetter(age_range), reverse=True)
		for i in range(0, 9):
			print("{}:\t{}:{}".format(
				d[i]["Country"],
				age_range,
				d[i][age_range])
			)

sort_by_smallest_age_range(ONE)