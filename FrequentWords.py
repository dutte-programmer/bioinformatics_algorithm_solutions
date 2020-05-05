

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
	print(*frequentwords, sep=" ")	
	return "Finished"


if __name__ == "__main__":
	print("Type in your sequence:")
	seq = input()
	print("Type in your k-length:")
	k = int(input())
	FrequentWords(seq, k)
