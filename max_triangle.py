# (3) Consider a triangle of numbers. By starting at the top of the triangle and moving to adjacent numbers below, 
# we want to find the maximum total from top to bottom.
#    2                 19             
#   6 3              17  16           find the biggest number underneath this number, return its index
#  1 3 5           8  11  13          find the biggeest number underneath this number, reutrn its index
# 7 4 8 2         7      8
# In the triangle above, the maximum value is found by the sequence
 # 2 + 6 + 3 + 8 = 19
# Consider the triangle with a hundred rows in the file
 # http://people.ischool.berkeley.edu/~tygar/for.i206/maxtriangle.txt
# Find the path from top to bottom with maximum value. 
# (Note that you will need to think of a good algorithm here -- 
# if you try searching all possible paths, it will take in excess of 5 billion years.)
# Your output format should list the chain, starting from the top and going
 # to the bottom, as a sum. For the small example above, the output would be
# "2 + 6 + 3 + 8 = 19"
import copy


def triangle(triangle):
	tri_list = []
	with open(triangle,"r") as file_handle:
		triangle = file_handle.readlines()
	n = 0
	while n <= len(triangle)-1:
		triangle[n] = triangle[n].split()
		n += 1

	for row in triangle:
		int_row = []
		for n in row:
			int_row.append(int(n))
		tri_list.append(int_row)
	triangle = tri_list
	return triangle


def max_triangle(input):
	triangle_to_max = triangle(input)
	tri_copy = copy.deepcopy(triangle_to_max)
	for line in reversed(range(len(triangle_to_max))):
		for number in range(0, line): #for the indices (i.e. 0,1,...x) in each line
			
			bigger = max(triangle_to_max[line][number], triangle_to_max[line][number+1]) #compare the nth value to its neighbor and return the bigger one
			bigger_copy = max(tri_copy[line][number], tri_copy[line][number+1]) #I think there's something wrong here. This doesn't  add up to the sum. But this is supposed to keep track of all the indivudual numbers, so they're not lost as you add up the triangle
			
			original_number = triangle_to_max[line-1][number] #number above the compared-pair
			original_number_copy = tri_copy[line-1][number] #keeps track of original numbers
			
			triangle_to_max[line-1][number] = bigger + original_number #add the bigger number to the number "above" the compared pair of numbers 
			tri_copy[line-1][number] = "{}, {}".format(bigger_copy, original_number_copy) #collects the lower bigger number and upper original number in the copy
			
	route = [] 
	str_route = tri_copy[0][0] # this is the numbers the route takes down the triangle from bottom to top
	revers_route = str_route.replace(",","").split(" ") #clean it up
	for i in reversed(revers_route): #reverse it so it goes from top to bottom
		route.append(i) 
	route_print = (" + ".join(route)) + "{}{}".format(" = ", triangle_to_max[0][0]) #output
	return route_print


def main():
	
	print(max_triangle("maxtriangle.txt"))

if __name__ == "__main__":
	main()
