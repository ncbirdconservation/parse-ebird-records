#compile bird codes from BirdMacroLibrary.csv
#this file came from http://fielddata.blogspot.com/p/field-notes-data-tips-download-page.html

import os
import sys

def main():
	infile = open('BirdMacroLibrary.csv', 'r')
	outfile = open('bird_code_lookup_dict.txt','w')
	h = []
	d = ','
	nl = '\n'

	outfile.write('bird_code_lookup = {')
	countline = 1	
	comma = ''
	with infile as f:
	    for line in f:

	    	if 'gen,' in line:
	    		line = line.replace('gen,','gen')
	    	r = line.split(d)
	    	if countline ==1:
	    		#header row, collect headers
	    		#should be: SPEC,COMMONNAME,SCINAME,SPEC6,CONF6,CONF,SP,Sort Order,Order,Family,Subfamily
	    		for i in r: 
	    			h.append(i)
	    	else:
	    		if countline>=3: 
	    			comma = ','
				sd = {}
				print str(len(r)) + ' line:' + str(r)
				sd = dict([(h[i],v.strip('"')) for i,v in enumerate(r)])
				outfile.write(nl + comma + '"'+sd['SPEC'] + '":"' + sd['SCINAME'] + '"')

	        countline +=1
	outfile.write('}')

if __name__ == '__main__':
	main()
