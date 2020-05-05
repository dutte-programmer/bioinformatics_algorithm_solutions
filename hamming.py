import sys


def hammingdistance(seq1, seq2):
	hammingdistance = 0
	for i in range(len(seq1)):
		if seq1[i] == seq2[i]:
			hammingdistance = hammingdistance
		else:
			hammingdistance += 1
	print(hammingdistance)
	return

if __name__ == "__main__":
	print("Type in sequence 1 and sequence two for hammingdistance and press enter!")
	data = list(sys.stdin.read().strip().split())
	seq1 = data[0]
	seq2 = data[1]
	print("Your hammingdistance is:" + hammingdistance(seq1, seq2))
