import sys
from glob import glob  
from os import path
import os
 
def find_ext(dr, ext):
    return glob(path.join(dr,"*.{}".format(ext)))
   
def pdftotext(pdffile):
	txtfile = os.path.basename(pdffile)
	txtfile = "../tmp/"+(txtfile.split(".pdf")[0]+'.txt')
	myCmd = 'pdftotext -enc UTF-8 '+pdffile.replace(" ", "\ ")+' '+txtfile.replace(" ", "\ ")
	print 'brjbber '+pdffile
	print myCmd
	os.system(myCmd)
	return txtfile
def abstract(fp):
	line = fp.readline()
	abstract = ""
	while line:
		if line.lower().find("abstract") != -1:
			
			while line:
				if line.lower().find("introduction") != -1 :
					break
				abstract = abstract + line.replace("\n"," ")
				line = fp.readline()
		if abstract != "":
			return abstract
		else:
			line = fp.readline()
	return ""
def introduction(fp):
	fp.seek(0,0)
	line = fp.readline()
	introduction = ""
	c = 0
	while line:
		if line.lower().replace(' ','').find("introduction") != -1:
			
			while line:
				if line == "\n" and c ==1:
					break
				if line == "\n":
					c = 1
				introduction = introduction + line.replace("\n"," ")
				line = fp.readline()
		if introduction != "":
			return introduction
		else:
			line = fp.readline()
	return ""
def corp(fp):
	line = fp.readline()
	corp = ""
	while line:
		
		while line:
			print("corp "+line)
			lastfp = fp.tell()
			if line.lower().find("conclusion\n") != -1 or line.lower().find("references\n") != -1 or line.lower().find("discussion\n") != -1 or line.lower().find("conclusions\n") != -1:
				break
			corp = corp + line.replace("\n"," ")
			line = fp.readline()	
		print(line)		
		fp.seek(lastfp,0)
		line = fp.readline()
		print(line)
		return corp
	return ""
def conclusion(fp):
	fp.seek(0,0)
	line = fp.readline()
	conclusion = ""
	while line:
		if line.lower().find("conclusion") != -1:
			while line:
				if line.lower().find("references") != -1:
					print(line)
					break
				conclusion = conclusion + line.replace("\n"," ")
				line = fp.readline()
		if conclusion != "":
			return conclusion
		else:
			line = fp.readline()
	return ""
def discussion(fp):
	fp.seek(0,0)
	line = fp.readline()
	conclusion = ""
	while line:
		if line.lower().find("discussion\n") != -1:
			
			while line:
				if line.lower().find("conclusion") != -1:
					break
				conclusion = conclusion + line.replace("\n"," ")
				line = fp.readline()
		if conclusion != "":
			return conclusion
		else:
			line = fp.readline()
	return ""
def references(fp):
	fp.seek(0,0)
	line = fp.readline()
	
	while line:
		references = ""
		if line.lower().find("references") != -1:
			while line:
				if line.lower().find("references") != -1:
					references = ""
				references = references + line.replace("\n"," ")
				line = fp.readline()
		if references != "":
			return references
		else:
			line = fp.readline()
	return ""
def parsefilexml(txtfile):
	filename = txtfile.split(".txt")[0].split('/')[-1]
	outputname = "../out/xml/PARSED_"+filename+".xml"
	fparsed = open(outputname,"w+")
	fparsed.write("<article>\n")
	fparsed.write("<preamble>"+filename+'</preamble>\n')
	auteur = ""
	with open(txtfile) as fp:
		titre = fp.readline()
		line = fp.readline()
		if len(line) > 5:
			titre += line
			auteur = fp.readline()
			line = fp.readline()
			if len(line) > 5:
				auteur += line
		fparsed.write("<titre>"+titre.replace("\n"," ")+"</titre>\n")
		fparsed.write("<auteur>"+auteur.replace("\n"," ")+"</auteur>\n")
		fparsed.write("<abstract>"+abstract(fp)+"</abstract>\n")
		fparsed.write("<introduction>"+introduction(fp)+"</introduction>\n")
		fparsed.write("<corp>"+corp(fp)+"</corp>\n")
		fparsed.write("<discussion>"+discussion(fp)+"</discussion>\n")
		fparsed.write("<conclusion>"+conclusion(fp)+"</conclusion>\n")
		fparsed.write("<references>"+references(fp)+"</references>\n")
		fparsed.write("</article>\n")
def parsefiletxt(txtfile):
	filename = txtfile.split(".txt")[0].split('/')[-1]
	outputname = "../out/txt/PARSED_"+filename+".txt"
	fparsed = open(outputname,"w+")
	fparsed.write(filename)
	auteur = ""
	with open(txtfile) as fp:
		titre = fp.readline()
		line = fp.readline()
		if len(line) > 5:
			titre += line
			auteur = fp.readline()
			line = fp.readline()
			if len(line) > 5:
				auteur += line
		fparsed.write(titre.replace("\n"," ")+"\n")
		fparsed.write(auteur.replace("\n"," ")+"\n")
		fparsed.write(abstract(fp)+"\n")
		fparsed.write(introduction(fp)+"\n")
		fparsed.write(corp(fp)+"\n")
		#fparsed.write("<discussion>"+discussion(fp)+"</discussion>\n")
		fparsed.write(conclusion(fp)+"\n")
		fparsed.write(references(fp)+"\n")
def menu(files):
	i=1
	print("Entrez le numero du fichier que vous voulez parser...")
	for file in files:
		print("{} {}".format(i, file))
		i= i+1
	mode=int(raw_input('Input:'))
	if mode > len(files) or mode <= 0:
		print "Numero incorrect"
		menu(files)
	else:
		return mode
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
	print(typesortie)
	files = find_ext(filepath,"pdf")
	mode = menu(files)
	txtfile = pdftotext(files[mode-1])
	if typesortie == "-t":
		parsefiletxt(txtfile)
	if typesortie == "-x":
		parsefilexml(txtfile)
