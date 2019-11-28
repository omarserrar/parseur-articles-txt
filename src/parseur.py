import sys
from glob import glob  
from os import path
import os
def find_ext(dr, ext):
    return glob(path.join(dr,"*.{}".format(ext)))
   
def pdftotext(pdffile):
	txtfile = os.path.basename(pdffile)
	txtfile = "../tmp/"+(txtfile.split(".pdf")[0]+'.txt')
	myCmd = 'pdftotext '+pdffile.replace(" ", "\ ")+' '+txtfile.replace(" ", "\ ")
	print 'brjbber '+pdffile
	print myCmd
	os.system(myCmd)
	parsefile(txtfile)
	
def parsefile(txtfile):
	filename = txtfile.split(".txt")[0].split('/')[-1]
	outputname = "../out/PARSED_"+filename
	fparsed = open(outputname,"w+")
	fparsed.write(filename+'\n')
	with open(txtfile) as fp:
		line = fp.readline()
		fparsed.write(line.replace("\n"," ")+"\n")
		abstract = ""
		while line:
			if line.find("Abstract") != -1 or line.find("ABSTRACT") != -1 or line.find("abstract") != -1:
				
				while line:
					if line.find("INTRODUCTION") != -1 or line.find("Introduction") != -1 or line.find("introduction") != -1 or line == "\n" :
						break
					abstract = abstract + line.replace("\n"," ")
					line = fp.readline()
			if abstract != "":
				fparsed.write(abstract)
				break
			line = fp.readline()
	
	fparsed.close()
args = sys.argv

if len(args) < 2:
	print "Usage:"
	print " parseur.py fichiertxt"
else:	
	filepath = args[1]
	files = find_ext(filepath,"pdf")
	for pdffile in files:
		pdftotext(pdffile)


