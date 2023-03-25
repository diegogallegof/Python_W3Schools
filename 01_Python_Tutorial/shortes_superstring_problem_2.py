# Source: https://www.geeksforgeeks.org/shortest-superstring-problem/
# python code for the above approach
import sys

# Utility function to calculate
# minimum of two numbers
def minimum(a, b):
	return a if a < b else b

# Function to calculate maximum
# overlap in two given strings
def findOverlappingPair(str1, str2):
	# Max will store maximum
	# overlap i.e maximum
	# length of the matching
	# prefix and suffix
	max_len = -sys.maxsize
	len1 = len(str1)
	len2 = len(str2)
	str_ = ""

	# Check suffix of str1 matches
	# with prefix of str2
	for i in range(1, minimum(len1, len2)+1):
		# Compare last i characters
		# in str1 with first i
		# characters in str2
		if str1[len1-i:] == str2[:i]:
			if max_len < i:
				# Update max and str_
				max_len = i
				str_ = str1 + str2[i:]
	
	# Check prefix of str1 matches
	# with suffix of str2
	for i in range(1, minimum(len1, len2)+1):
		# compare first i characters
		# in str1 with last i
		# characters in str2
		if str1[:i] == str2[len2-i:]:
			if max_len < i:
				# Update max and str_
				max_len = i
				str_ = str2 + str1[i:]
	
	return max_len, str_

# Function to calculate
# smallest string that contains
# each string in the given
# set as substring.
def findShortestSuperstring(arr, n):
	# Run n-1 times to
	# consider every pair
	while n != 1:
		# To store maximum overlap
		max_len = -sys.maxsize
		# To store array index of strings
		l, r = 0, 0
		# Involved in maximum overlap
		res_str = ""
	
		# Maximum overlap
		for i in range(n):
			for j in range(i+1, n):
				str_ = ""
				# res will store maximum
				# length of the matching
				# prefix and suffix str is
				# passed by reference and
				# will store the resultant
				# string after maximum
				# overlap of arr[i] and arr[j],
				# if any.
				res, str_ = findOverlappingPair(arr[i], arr[j])

				# check for maximum overlap
				if max_len < res:
					max_len = res
					res_str = str_
					l, r = i, j
		
		# Ignore last element in next cycle
		n -= 1

		# If no overlap, append arr[n-1] to arr[0]
		if max_len == -sys.maxsize:
			arr[0] += arr[n]
		else:
			# Copy resultant string to index l
			arr[l] = res_str
			# Copy string at last index to index r
			arr[r] = arr[n]
	
	return arr[0]

# Driver program
if __name__ == "__main__":
    arr = ["diego", "diego", "diego", "diego", "diego"]
    n = len(arr)
    #arr = ["catgc", "ctaagt", "gcta", "ttca", "atgcatc"]
	# Function Call
    # other 
    print("The Shortest Superstring is", findShortestSuperstring(arr, n))

# this code is contributed by bhardwajji
