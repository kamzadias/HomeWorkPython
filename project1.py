from itertools import permutations

arr = input().split()

if len(arr) == 1:
	print([arr])
else:
	print ([''.join(x) for x in permutations(arr)])