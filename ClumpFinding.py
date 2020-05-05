
import sys 

def PatternCount(text, pattern):
	count = 0
	for i in range(0, len(text)-len(pattern)+1):
		if text[i:i+len(pattern)] == pattern:
			count += 1
	return count 


def FrequentWords(text, k):
	frequentpatterns = {}
	for i in range(0, len(text)-k+1):
		pattern = text[i:i+k]
		frequentpatterns[pattern] = PatternCount(text, pattern)
	MaxCount = max(frequentpatterns.values())
	frequentwords = list()
	for key, value in frequentpatterns.items():
		if MaxCount == value and not key in frequentwords:
			frequentwords.append(key)
	return frequentwords

def ClumpFinding(text, k, L, t):
	Clumpfinding = []
	for i in range(0, len(text)-L+1):
		clump = text[i:i+L]
		for i in range(0, len(text)-k+1):
			pattern = text[i:i+k]
			if PatternCount(clump, pattern) == t and not pattern in Clumpfinding:
				Clumpfinding.append(pattern)
	print(*Clumpfinding, sep=" ")
	return



if __name__ == "__main__":
	print("Type in: k, L, t and the sequence!")
	data = list(sys.stdin.read().strip().split())
	k = int(data[0])
	L = int(data[1])
	t = int(data[2])
	genome = data[3]
	ClumpFinding(genome, k, L, t)
	
