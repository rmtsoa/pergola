#!/usr/bin/env python

"""
26 Nov 2014

Script to run pergola from the command line using isatab format
"""

sp = " "

from pergola import parsers
from pergola  import intervals
from pergola  import mapping
# from scripts import pergola_rules
from argparse import ArgumentParser, ArgumentTypeError
from sys      import stderr, exit
import os
# from bcbio import isatab
import pergola_rules


from urllib import urlretrieve, URLopener

url = "https://raw.githubusercontent.com/cbcrg/pergola/master/data/feeding_beh_files/20120502_FDF_CRG_hab_DevW1_W2_filt_c1.csv" 
file_name = url.split('/')[-1]

from os.path import expanduser
home_dir = expanduser('~')

path_pergola = os.path.join(home_dir,".pergola/projects")
if not os.path.exists(path_pergola):
    os.makedirs(path_pergola)

path_file = os.path.join(path_pergola, file_name)
print "...............",home_dir
print "...............",path_file

# exit("culo...................")#del


print "file name is::::::::::::::::::::::::::", path_file

# "/users/cn/jespinosa/Desktop/test.csv"


url_file = URLopener()

url_file.retrieve(url, path_file)

# urlretrieve("https://raw.githubusercontent.com/cbcrg/pergola/master/dat/feeding_beh_files/20120502_FDF_CRG_hab_DevW1_W2_filt_c1.csv", "/users/cn/jespinosa/Desktop/test.csv")
        
exit("culo...................")          

def main():
    parser = ArgumentParser(parents=[parsers.parser])
    
    args = parser.parse_args()
    
    print >> stderr, "@@@Pergola_isatab.py: Input file: %s" % args.input 
    print >> stderr, "@@@Pergola_isatab.py: Configuration file: %s" % args.ontology_file
    print >> stderr, "@@@Pergola_isatab.py: Selected tracks are: ", args.tracks
    
    # I have to check whether when a isatab folder is given if it is actually a folder or a file
    # difference with -i
    if not os.path.isdir(args.input):
        raise ValueError ("Argument input must be a folder containning data in isatab format")
    
    dict_files = parsers.parse_isatab_assays (args.input)
    print dict_files
#It might be interesting to implement a append option

if __name__ == '__main__':
    exit(main())