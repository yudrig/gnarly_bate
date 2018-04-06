from random import *

def randLine(inFileName):

	file = open(inFileName,"r")

	fileLines = file.read().splitlines()

	lineNum = randint(0,(len(fileLines)-1))

	return fileLines[lineNum]


