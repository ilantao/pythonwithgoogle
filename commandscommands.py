import sys
import os
import commands

def List(dir):
	cmd = 'ls -l ' + dir
	(status, output) = commands.getstatusoutput(cmd)
	print output
	

def main():
	List(sys.argv[1])

if __name__ == '__main__':
    main()