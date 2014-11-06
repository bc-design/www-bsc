### Import the URL data fetcher ###
# https://docs.python.org/2/library/urllib.html

import urllib
import os

### Import the XML manipulation package ###
# https://docs.python.org/2/library/xml.etree.elementtree.html
# http://eli.thegreenplace.net/2012/03/15/processing-xml-in-python-with-elementtree/
# http://www.w3schools.com/xml/default.asp

try:
	import xml.etree.cElementTree as ET
except ImportError:
	import xml.etree.ElementTree as ET

def statusclear(file):
	"""takes a filename; clears this file, returning nothing"""
	open(file,'w').close()

def statuswrite(file,text):
	"""takes a file and text; writes the text, closes the file; returns nothing"""
	statusdoc = open(file,'a')
	statusdoc.write(text)
	statusdoc.close()

def split(txt, seps):
	"""takes string, list of separators; returns list"""
    default_sep = seps[0]
    # we skip seps[0] because that's the default seperator
    for sep in seps[1:]:
		txt = txt.replace(sep, default_sep)
    return [i.strip() for i in txt.split(default_sep)]

def main(dir,text=None):
	file_status = dir+'temp/status_info.txt'
	file_info   = dir+'temp/journal_info.csv'
	file_list   = dir+'temp/journal_list.txt'

	statusclear(file_status)
	journal_info = open(file_info,'w')	

	if text==None:
		journal_list = open(file_list,'r')
	else:
		journal_list = split(text,(',','\n'))

	for journal_name in journal_list:
		url = 'http://www.sherpa.ac.uk/romeo/api29.php?ak=Ivc5b3cuZLk&jtitle=' + journal_name
		# example output: http://www.sherpa.ac.uk/romeo/api29.php?jtitle=modern%20language
		tree = ET.parse(urllib.urlopen(url))
		root = tree.getroot()

		if tree.find('header/numhits').text == '1':
			for journal in tree.iterfind('journals/journal'):
			# searching with XPath: http://www.w3schools.com/xml/xml_xpath.asp
				for publisher in tree.iterfind('publishers/publisher'):
					print 'processing - ' + journal.find('jtitle').text
					journal_info.write('[OA ' + publisher.find('romeocolour').text + '] ' + journal.find('jtitle').text + '\n')
					statuswrite(file_status,'processing - ' + journal.find('jtitle').text + '\n')
		elif tree.find('header/outcome').text == 'failed' or tree.find('header/outcome').text == 'notFound':
			print 'failed - no results - ' + journal_name.rstrip()
			journal_info.write('not found - ' + journal_name.rstrip() + '\n')
			statuswrite(file_status,'failed - no results - ' + journal_name.rstrip() + '\n')
		else: 
				print 'failed - multiple results - ' + journal_name.rstrip()
				journal_info.write('failed - multiple results - ' + journal_name.rstrip() + '\n')
				statuswrite(file_status,'failed - multiple results - ' + journal_name.rstrip() + '\n')

	if text==None:
		journal_list.close()
	journal_info.close()
	print 'Lookup Complete!'

if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
   main()
