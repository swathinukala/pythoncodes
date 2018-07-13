# Python Directory

# import os
# from os import *

# mkdir('DummyDir')
# mkdir('E:\\pythonkak\\DummyDir\\InDir')
# rename('DummyDir','MyDir')
# rmdir('MyDir')
# chdir()
# print(getcwd())

import csv
from csv import *

def writing(data,fileobj):
	csv_writer=writer(fileobj,delimiter=',')
	print(csv_writer)
	for i in data:
		csv_writer.writerow(i)

if __name__=='__main__':
	fileobj=open('CallDetails.csv','w')
	data=['Name,time,Ph.No,Address'.split(','),
	'Swathi,923,32354563,Hyderabad'.split(','),
	'Krishna,923,32354563,Hyderabad'.split(','),
	'Sweetie,923,32354563,Hyderabad'.split(','),
	'Ammu,923,32354563,Hyderabad'.split(',')]
	writing(data,fileobj)