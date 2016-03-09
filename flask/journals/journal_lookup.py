### Import the URL data fetcher ###
# https://docs.python.org/2/library/urllib.html

import string
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

def split(txt, seps):

	"""takes (string, list of separators); returns list"""

	default_sep = seps[0]
	# we skip seps[0] because that's the default seperator
	for sep in seps[1:]:
		txt = txt.replace(sep, default_sep)
	return [i.strip() for i in txt.split(default_sep)]

def main(dir,text=None):

	"""takes a list of journals; returns the journal OA from the SHERPA database"""

	journal_list = split(text,(',','\n'))
	resultsvar = []

	for journal_name in journal_list:
		url = 'http://www.sherpa.ac.uk/romeo/api29.php?ak=Ivc5b3cuZLk&jtitle=' + journal_name
		# example output: http://www.sherpa.ac.uk/romeo/api29.php?jtitle=PLoS%20One
		tree = ET.parse(urllib.urlopen(url))
		root = tree.getroot()

		if tree.find('header/numhits').text == '1':
			for journal in tree.iterfind('journals/journal'):
			# searching with XPath: http://www.w3schools.com/xml/xml_xpath.asp
				for publisher in tree.iterfind('publishers/publisher'):
					if publisher.find('pdfversion/pdfarchiving').text == 'can':
						resultsvar.append('gold, ' + journal.find('jtitle').text)
					else:
						print 'processing - ' + journal.find('jtitle').text #testing
						resultsvar.append(publisher.find('romeocolour').text + ', ' + journal.find('jtitle').text)
						# resultsvar.append('[OA ' + publisher.find('romeocolour').text + '], ' + journal.find('jtitle').text)
		elif tree.find('header/outcome').text == 'failed' or tree.find('header/outcome').text == 'notFound':
			print 'failed - no results - ' + journal_name.rstrip() #testing
			resultsvar.append('failed - not found, ' + journal_name.rstrip())
		else: 
			print 'failed - multiple results - ' + journal_name.rstrip() #testing
			resultsvar.append('failed - multiple results, ' + journal_name.rstrip())

	print 'Lookup Complete!' #testing
	return resultsvar

if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
   main()
