import sys

def hammingsub(pattern, dna, d):
	hamminglist = []
	for i in range(0, len(dna)-len(pattern)+1):
		#print(len(dna)-len(pattern)+1)
		hammingdistance=0
		subpattern = dna[i:len(pattern)+i]
		for x in range(len(pattern)):
			if pattern[x] ==  subpattern[x]:
				hammingdistance = hammingdistance
			else:
				hammingdistance += 1
		if hammingdistance <= int(d):
			if dna.index(dna[i:len(pattern)+i]) in hamminglist:
				hamminglist = hamminglist
			else:			
				hamminglist.append(dna.index(dna[i:len(pattern)+i]))
	print(*hamminglist, sep=" ")
	return "Finished!"

if __name__=="__main__":
	print("Type in pattern, dna and mismatches [d]!")
	data = list(sys.stdin.read().strip().split())
	pattern1 = data[0]
	dna1 = data[1]
	d1 = data[2]
	print("Your hammingdistance with at most {} mismatches is: ".format(d1) + hammingsub(pattern1, dna1, d1))
	


