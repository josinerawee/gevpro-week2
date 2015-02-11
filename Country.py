#!/usr/bin/env python
import sys

class Country:
	def __init__(self,country):
		self.country=country
	def __str__(self):
		return "Hello from {0}".format(self.country)
		
def main():
	a=Country('The Netherlands')
	print a
	
main()
