eBird Parse Code
================

This python script extracts records from the [eBird Basic Dataset](http://ebird.org/ebird/data/download) (2015) without having to load the entire text file. Records can be extracted by state, species, and year (or any combination). 

##Developer
Scott Anderson

[North Carolina Wildlife Resources Commission](http://www.ncwildlife.org)

[scott.anderson@ncwildlife.org](mailto:scott.anderson@ncwildlife.org)

919.707.0139

##To Do
- implement command line arguments (currently have to modify temp_argv variable)

##Arguments
Syntax: parse_ebird_records.py ebd_file_path \[State\] \[Species\] \[Years\]
- ebd_file_path
    + the file path to the eBird Basic Dataset
    + e.g., J:\\ebird_data\\ebd_relMay-2015\\ebd_relMay-2015.txt 
- State(s):
    + st=NC
    + st=NC,VA,SC
- Species:
    + spp=BACS
    + spp=BACS,WOTH,AMRE
- Year(s):
    + yrs=2002
    + yrs=2003,2005
    + yrs=2003-2010


##Literature
eBird Basic Dataset. Version: EBD_relMay-2015. Cornell Lab of Ornithology, Ithaca, New York. May 2015.