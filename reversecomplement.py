import sys

def reversecomplement(seq):
	lower = seq.lower()

	a = lower.replace("a", "T")
	b = a.replace("c", "G")
	c = b.replace("g", "C")
	d = c.replace("t", "A")

	return d[::-1]



if __name__ == "__main__":
    data = sys.stdin.read()
    seq = data
    revseq = reversecomplement(seq)
    print(revseq)
