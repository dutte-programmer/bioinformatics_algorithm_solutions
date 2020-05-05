import sys
seq = "CATTCCAGTACTTCGATGATGGCGTGAAGA"
reverseseq = seq[::-1]

def skew(seq):
	# create counter and skew list
	count = 0
	skew = []
	# calculate skew
	# for every G + 1 for every C - 1
	for i in seq:
		if i == "G":
			count += 1
		elif i == "C":
			count -= 1
		else:
			count = count
		# append current skew count
		skew.append(count)
	# search the min skew
	print(skew)
	mini = min(skew)
	indices = [i for i, x in enumerate(skew) if x == mini]
	for t in indices:
		print("The minimum skew value is: {}".format(skew[t]))
	return

if __name__=="__main__":
	print("Type in your sequence!")
	data = list(sys.stdin.read().strip().split())
	text = data[0]
	skew(text)


