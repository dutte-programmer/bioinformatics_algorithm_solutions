import sys

def hammingdistance(seq1, seq2):
	hammingdistance = 0
	for i in range(len(seq1)):
		if seq1[i] == seq2[i]:
			hammingdistance = hammingdistance
		else:
			hammingdistance += 1
	return hammingdistance

def ApproximatePatternCount(text, pattern, d):
    count = 0
    for i in range(0, len(text)-len(pattern)+1):
        pattern2 = text[i:i+len(pattern)]
        if int(hammingdistance(pattern, pattern2)) <= int(d):
            count += 1
    return count

if __name__ == "__main__":
    print("Type in pattern, text(sequence) and integer(d)!")
    data = list(sys.stdin.read().strip().split())
    pattern = data[0]
    seq = data[1]
    d = data[2]
    print("Your Approximatepattern count with at most {} mismatches is ".format(d) + str(ApproximatePatternCount(seq, pattern, d)))