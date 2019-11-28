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
	return txtfile
	
def parsefilexml(txtfile):
	filename = txtfile.split(".txt")[0].split('/')[-1]
	outputname = "../out/xml/PARSED_"+filename+".xml"
	fparsed = open(outputname,"w+")
	fparsed.write("<article>\n")
	fparsed.write("<preamble>"+filename+'</preamble>\n')
	with open(txtfile) as fp:
		line = fp.readline()
		
		fparsed.write("<titre>"+line.replace("\n"," ")+"</titre>\n")
		abstract = ""
		while line:
			if line.find("Abstract") != -1 or line.find("ABSTRACT") != -1 or line.find("abstract") != -1:
				
				while line:
					if line.find("INTRODUCTION") != -1 or line.find("Introduction") != -1 or line.find("introduction") != -1 or line == "\n" :
						break
					abstract = abstract + line.replace("\n"," ")
					line = fp.readline()
			if abstract != "":
				fparsed.write("<abstract>"+abstract+"</abstract>\n")
				break
			line = fp.readline()
		fparsed.write("</article>\n")
	
	fparsed.close()

def parsefiletxt(txtfile):
	filename = txtfile.split(".txt")[0].split('/')[-1]
	outputname = "../out/txt/PARSED_"+filename+".txt"
	fparsed = open(outputname,"w+")
	fparsed.write(""+filename+'\n')
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

if len(args) < 3 or (args[1] != "-x" and args[1] != "-t"):
	print "Usage:"
	print " parseur.py types repertoire"
	print "Types:"
	print "-t\tgenerer les fichiers dans une version texte (.txt)"
	print "-x\tgenerer les fichiers dans une version XML (.xml)"
	print "Repertoire:"
	print "Repertoire qui contient les fichiers PDF"
else:	
	filepath = args[2]
	typesortie = args[1]
	files = find_ext(filepath,"pdf")
	for pdffile in files:
		txtfile = pdftotext(pdffile)
		if typesortie == "-t":
			parsefiletxt(txtfile)
		if typesortie == "-x":
			parsefilexml(txtfile)
