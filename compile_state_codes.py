#compile state code values from ebird EBD - will be used to build better query criteria for parse_ebird_records.py 

import os
import sys

def main():
	infile = open('E:\\ebird_data\\ebd_relMay-2015\\ebd_relMay-2015.txt', 'r')
	outfile = open('state_code_lookup.csv','w')
	h = []
	d = ','
	nl = '\n'

	# outfile.write('bird_code_lookup = {')
	# COUNTRY, COUNTRY CODE, STATE, STATE CODE
	countrycol = 10
	countrycodecol = 11
	statecol = 12
	statecodecol = 13

	unique_combos = []


	countline = 1	
	comma = ''
	with infile as f:
		for line in f:
			if len(line)>1: #skip blank lines
				r = line.split('\t')
				line_data = [r[statecodecol],r[countrycol], r[countrycodecol], r[statecol]]
				if line_data not in unique_combos:
					unique_combos.append(line_data)
					outfile.write(d.join(line_data)+nl)
			countline +=1

			# if countline>1000: break #for testing


if __name__ == '__main__':
	main()
