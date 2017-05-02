#!python3
import re

ONE = "0-14 years:"
TWO = "15-24 years:"
THREE = "25-54 years:"
FOUR = "55-64 years:"
FIVE = "65 years and over:"
regex = (r'\d{,2}\.\d{,2}%')

#2016 data
with open('unparsed_age_data.txt') as old, open('parsed_age_data.txt', 'w') as new:
	i = 0
	for line in old:
		if i is 0:
			country = line[:line.index(" 0")]
			new.write("{ ")
			new.write('"{}":"{}, "'.format(
				"Country", country)
			)
			percentage = re.search(regex, line).group(0)
			new.write('"{}":"{}, "'.format(
				ONE, percentage)
			)
		if i is 1:
			percentage = re.search(regex, line).group(0)
			new.write('"{}"."{}", '.format(
				TWO, percentage)
			)
		if i is 2:
			percentage = re.search(regex, line).group(0)
			new.write('"{}"."{}", '.format(
				THREE, percentage)
			)
		if i is 3:
			percentage = re.search(regex, line).group(0)
			new.write('"{}"."{}", '.format(
				FOUR, percentage)
			)
		if i is 4:
			percentage = re.search(regex, line).group(0)
			new.write('"{}"."{}" '.format(
				FIVE, percentage)
			)
			new.write("}\n")
		i = 0 if (i is 4) else i + 1
	old.close()
