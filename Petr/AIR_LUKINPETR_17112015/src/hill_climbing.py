#!/usr/bin/env python
import numpy as np
import math
 
def read_all_cities():
	data = np.loadtxt("cities.txt",delimiter=',',usecols = (1,2))
	
	return data
	
	
def find_distance(x,y):
	#print "x,y "
	#print x.shape
	#print y.shape
	#print x[0,1]
	#print y[1]
	if x.shape[0] ==2:
		d = math.sqrt((y[0]-x[0])*(y[0]-x[0])+(y[1]-x[1])*(y[1]-x[1]))
		
	else:
		d = math.sqrt((y[0]-x[0,0])*(y[0]-x[0,0])+(y[1]-x[0,1])*(y[1]-x[0,1]))
		
	
	return d
	
	
	
def find_closest_city(current_city,array_of_cities):
	min_dist = 1000000;
	index = 0;
	for i in range(array_of_cities.shape[0]):	
		dist = find_distance(current_city,array_of_cities[i])
		if dist < 0.1:
			continue
		if (dist<min_dist):
			min_dist = dist
			index = i
	#print "min dist "+str(min_dist)
	#print "index " +str(index )
	return min_dist,index
	
	
	
def climb_hill (number_of_random_points,array_of_cities):
	previous_random_numbers = np.array([])
	paths = np.array([])
	
	for i in range(number_of_random_points):
		r = np.random.randint(array_of_cities.shape[0]-1, size=1)
		if r in previous_random_numbers:
			while r in previous_random_numbers:			
				r = np.random.randint(array_of_cities.shape[0]-1, size=1)
		previous_random_numbers = np.append(previous_random_numbers,r)
		buf_array = array_of_cities
		path = 0
		
	
		
		print "Index of a random city: "+str(r)
		new_city = 0
		old_city = r
		
		for j in range(array_of_cities.shape[0]-1):
			
			cost,new_city = find_closest_city(buf_array[old_city],buf_array)
			path = path +cost
			buf_array = np.delete(buf_array,old_city,0)
			if old_city>new_city:
				old_city = new_city
			else: old_city = new_city-1
				
			
			#print buf_array.shape
			#print "j "+str(j)
		#print "Path "+str(path)
					
		paths = np.append(paths,[path],0)
		#print "Paths "+str(paths)
			
		
	print "Found minimal path length "+str(np.amin(paths)) 		
		
		
		
			
		


if __name__ == "__main__":
	
	#cities = np.array([])
	cities = read_all_cities()
	##print cities.shape
	N = input("Enter the number of cities ")
	climb_hill(N,cities)
	
