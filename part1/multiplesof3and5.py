# -*- coding: utf-8 -*-

def sumFunc(max=1000):
	sum = 0
	for i in range(1, max): # "below" 1000, so did not max+1
		if i % 3 == 0 or i % 5 == 0:
			sum += i

	return sum

if __name__ == '__main__':
	print("The sum of all the multiples of 3 or 5 below 1000 is %d" % sumFunc())