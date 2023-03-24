# Python program for the above approach

def shortestSuperstring(A):
	n = len(A)
	graph = [[0 for i in range(n)] for j in range(n)]

	# Build the graph
	for i in range(n):
		for j in range(n):
			graph[i][j] = calc(A[i], A[j])
			graph[j][i] = calc(A[j], A[i])

	# Creating dp array
	dp = [[0 for i in range(n)] for j in range(1 << n)]

	# Creating path array
	path = [[0 for i in range(n)] for j in range(1 << n)]
	last = -1
	min_val = float('inf')

	# start TSP DP
	for i in range(1, (1 << n)):
		for j in range(n):
			dp[i][j] = float('inf')

		for j in range(n):
			if (i & (1 << j)) > 0:
				prev = i - (1 << j)

				# Check if prev is zero
				if prev == 0:
					dp[i][j] = len(A[j])
				else:
					# Iterate k from 0 to n - 1
					for k in range(n):
						if dp[prev][k] < float('inf') and dp[prev][k] + graph[k][j] < dp[i][j]:
							dp[i][j] = dp[prev][k] + graph[k][j]
							path[i][j] = k

				if i == (1 << n) - 1 and dp[i][j] < min_val:
					min_val = dp[i][j]
					last = j

	# Build the path
	sb = ""
	cur = (1 << n) - 1

	# Creating a stack
	stack = []

	# Until cur is zero
	# push last
	while cur > 0:
		stack.append(last)
		temp = cur
		cur -= (1 << last)
		last = path[temp][last]

	# Build the result
	i = stack.pop()
	sb += A[i]

	# Until stack is empty
	while len(stack) > 0:
		j = stack.pop()
		sb += A[j][len(A[j]) - graph[i][j]:]
		i = j

	return sb

# Function to check
def calc(a, b):
	for i in range(1, len(a)):
		if b.startswith(a[i:]):
			return len(b) - len(a) + i
	
	# Return size of b
	return len(b)

# Driver Code
if __name__ == '__main__':
	#arr = [ "catgc", "ctaagt", "gcta", "ttca", "atgcatc" ]
	arr = [ "diego", "diego", "diego", "diego", "diego" ]
	
	# Function Call
	print("The Shortest Superstring is " + shortestSuperstring(arr))
