from scanner import *
import sys
def main():
	s = Scanner(sys.argv[1])
	words = 0
	lines = 0
	p = s.readtoken()
	while(p != ""):
		if (p == 'END'):
			lines += 1
		else:
			words += 1
		p = s.readtoken()
	print("number of words is", words)
	print("number of lines is", lines)
	print("average number of words per line is", words/lines)
		



main()
