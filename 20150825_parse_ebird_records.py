#parse eBird Records
# this file will parse through eBird Basic Dataset records and retrieve specified records
# inputs:
#		spp = species list
#		yr = year list

import os
import sys


params = {"yrs":[],"spp":[]}
ebird_delim = '\t' 
delim = ','
fn_delim = '_' #delim for filename
nl = "\n"

#retrieve command line arguments
#arg 1 = program file
#arg 2 = file to be processed
#other arg syntax:
#	yrs=2002,2003
#	spp=BACS,RUGR

for argn, arg in enumerate(sys.argv): 
	print argn
	if argn>1: #parse values
		#format should be: argname=[val1,val2,val3]
		flag = arg.split("=")
		params[flag[0]]= flag[1].split(",")
	elif argn==1:
		fn = arg
	elif argn==0:
		dirfilesep = arg.rfind("\\")+1
		rootdir = arg[:dirfilesep]
		sourcefile = arg[dirfilesep:] 



def main():
	# outname = str(fn_delim.join(params.values()))
	print str(fn_delim.join(params['yrs']))
	out = open(rootdir + "ebird_temp.txt","w")
	count = 0
	with open("ebird_sample.txt") as f:
	    for line in f:
	        out.write(line + nl)
	        count +=1
	        if count>100: break



if __name__ == "__main__":
	main()
