import sys 

pattern1 = "TGAGATTTG"
text1 = "TGAGATTATTGAGATTGTGAGATTGTGAGATTGATGAGATTGGTGAGATTGTTGAGATTGATTGAGATTATGAGATTTCGCCCGTGAGATTTGAGATTGCGGCACGATGAGATTTGAGATTTGAGATTTCGTACTGAGATTTGAGATTTGAGATTATGAGATTTGAGATTAGTTGAGATTGTTTGAGATTGTGAGATTTGAGATTGATGAGATTTGAGATTAGGAGTGAGATTGTGAGATTGGTGCTTGAGATTTTGAGATTGTGAGATTTTGTTGAGATTTTCTCAGAACCACTGAGATTCTGAGATTGTTGAGATTGACTGAGATTCTGAGATTGAAAAATGAGATTGATGAGATTTGAGATTCCATTGAGATTACTGAGATTTAATGAGATTTGAGATTACGGGATGAGATTTGAGATTCTGTCCGTGAGATTTATCATTGAGAGCCACTGAGATTTATATAGTTCTTGAGATTCATGAGATTTTGAGATTAGGTGTGAGATTTATGAGATTACTGAGATTCGCGTGAGATTACTAGCTTGAGATTGGGCTGAGATTATCTGAGATTGTGAGATTATAGGTGAGATTAGTCTGAGATTTGAGATTTCTTGAGATTCTATGAGATTGAGATTCGTGAGATTGGATAGCCTGAGATTAGCACCATTTGAGATTATCGATTATGAGATTATTTATGAGATTAATTGAGATTACGCCAGCCTCTTTGTGAGATTAAAATTTGCACGTGTGAGATTTGTGTGCTGAGATTTGAGATTCTGGATGATGAGATTTGAGATTTGAGATTCTGTTGTGAGATTTGACATGAGATTTTTATGAGATTATCGGCGTCATGAGATTAATTTGTTGACTAATTGAGATTGTCTGAGATTTGAGATTGGTTGAGATTCTCTGGTGAGATTTGAGATTTGTGAGATTGTGAGATTTATGAGATTTGAGATTGAGATAAACTTGTGAGATTAGTGAGATTGCTGAGATTTGAGATTCTGAGATTGCTCAACGGTGAGATTGAATGAGATTTCTGAGATTAGTGAGATTTGAGATTTGAGATTATGAGATTTACATCGTGAGATTCGCACTTGAGATTTGAGATTGTGAGATTTATCTGAGATTGTGAGATTCCTTGAGATTCGTGAGATTCTGAGATTGCGTCGGGTGAGATTTTGAGATTCCGTGAGATTGGTGAGATTTGAGATTCGTGAGATTTCAGCTGAGATTGCGGTGAGATTGTAATCTGAGATTTGAGATTTACATGCATCAATGAATTTTGTATTTGAGATTAGCATACAATCACGGTGAGATTTCTGAGATTTTGAGATTGGTCAGTGAGATTCTTGAGATTTGTCTGAGATTTGAGATTGTTGAGATTTGAGATTCCGTGACTGAGATTCTGAGATTTGAGATTGACTGAGATTAGTGAGATTTATGAGATTACCCCTGAGATTGATGAGATTTGAGATTCGGTTGTGTGAGATTTGAGATTTTGAGATTTGAGATTTGAGATTTGAGATTTGAGATTTATCGCCTGATCGGTGAGATTTCGGCTTGAGATTTCTGAGATTACTTTTGAGATTGATGTGAGATTTGAGATTTTTTTCTGAGATTTTGCATGAGATTGTGAGATTCGATGAGATTTGAGATTAAGCATGAGATTCCTGAGATTTGAGATTCTGAGATTTGAGATTAGGCGTAGTGAGATTCCTGTGAGATTTAGTTGAGATTCAAGCTGGTGAGATTTTCACTTGCTGAGATTTGAGATTTGAGATTTAGTGAGATTTTGAGATTTGAGATTCTGAGATTTGAGATTAATGGATTCTGAGATTCTGAGATTTCATGAGATTGATTTGAGATTTATTGAGATTGATAGAAGATATGTGAGATTGGTCTGCCGTGAGATTGTATACTGAGATTTATTGAGATTTGAGATTTGAGATTGTCTGAGATTTGAGATTTGAGATTTGAGATTTGAGATTCGTGAGATTATGGATATGAGATTTCTGAGATTTGAGATTTGAGATTGGTGAGATTAATGAGATTTGAGATTTTTGAGATTTGAGATTAACCCTTGAGATTGCAAACATGAGATTGACTGAGATTAGCTGTGAGATTCAAGTGAGATTGCTGAGATTTGTATGAGATTTCCCCATATGAGATTATTGAGATTTGAGATTTGAGATTTGAGATTTGTTGAGATTTGAGATTCTTCTTGAGATTTACAATGAGATTGTTTGAGATTGCGGTGAGATTTGAGATTATGAGATTATCTGGGCTTGAGATTTTGAGATTTGAGATTTGAGATTTGAGATTACTGAGATTGATGAGATTAGATGAGATTTGAGATTTGAGATTTCGGCTGAGATTACTGAGATTTGAGATTTTAATGTTGAGATTGTATACTGGGCTCTGTGAGATTTGAGATTTGAGATTTGAGATTCGCTGAGATTACTATTTCTGTGAGATTGTGAGATTTCTGAGATTCGAGTTCTGAGATTATGAGATTTGAGATTAATTGAGATTTGAGATTCTTGAGATTTGAGATTGAAGGTGAGATTTTTGAGATTACTTGAGATTCCTTTGAGATTTGAGATTATGAGATTCACTGAGATTAAATGAGATTTATGACTCGTCGTGAGATTGTGAGATTCCTGAGATTGAATGATGAGATTCATGAGATTGTGAGATTTTGTGAGATTATTGAGATTTGAGATTGGTGTGGATGAGATTGTTGAGATTCGCAGATCCTGAGATTTGTGAGATTTGCCTAATGCCTGAGATTATGAGATTTCTGAGATTTGAGATTCTTGGATTGAGATTACCTGAGATTTGAGATTCTAATGAGATTAACTTCTTGAGATTCCCCCTGTGAGATTGAGAGTTTGAGATTAGACTGAGATTGCGTGAGATTGGTCCCTTTTTGAGATTTGAGATTAGTGAGATTCTTGAGATTGTGAGATTTGAGATTTGAGATTTTGAGATTCTGAGATTTGAGATTGAGGTGAGTTGAGATTTTCTGAGATTCTGAGATTACCGGTCCTTTCTGAGATTTGAGATTACTCATGAGATTCATGAGATTATGAGATTCGTGAGATTGTGGGTGAGATTACGAAGGAAGTGAGATTGGTGTTGAGATTTGAGATTTGAGATTTTGAGATTCTGAGATTTGAGATTTTGCTGTTTCTCCCATGAGATTGAGTTAATCATGAGATTCATGAGATTCCCTATGAGATTGTGAGATTTGAATGTGATGAGATTACTTGAGATTCTGAGATTTTCTCTGAGATTTGAGATTGCAAGTTGAGATTGATGAGATTACACTTGAGATTGCCCCTTTGAGATTTGAGATTCTTGAGATTGCTATTGCATGAGATTGTAGCTGAGATTTGAGATTGGCCGCAACTTGAGATTCGTGAGATTCATTATTGCTGAGATTCTGAGATTTTTCCATGAGATTTGAGATTCTGAGATTTGTGAGATTCTGAGATTCTGAGATTACTGAGATTTGAGATTTAATCTGAGATTCTCCAGCGTGAGATTTTGAGATTATTTATACATGAGATTTGCTTGAGATTCCTGAGATTTGAGATTGATTCACTGAGATTTGAGATTTGAGATTAAGTGAGATTTTGAGATTTTGAGATTTGAGATTTGAGATTATATGAGATTAATGAGATTGATGAGATTTATGAGATTTATGAGATTGTATCGGTCAGTGAGATTGGTGAGATTGGACTTCTGCGTGAGATTTTGAGATTTGAGATTGGAGCACGGTCACTGAGATTGGTTGAGATTATGAGATTGTGAGATTATGAGATTTGAGATTATGAGATTTGTGCACGTAAGTACCGTGAGATTTGCTCAGTGTGAGATTGGGGTAATGAGATTGTTTTGAGATTTGAGATTACCTGAGATTGTGACAGTGAGATTTGAGATTATGTTTTGAGATTTGAGATTGCATAAATGCTGAGATTTCCGTTTGAGATTTCAGATGAGATTTACGGCTTCGTGAGATTTTGGTGAGATTTGAGATTCGTGTGAGATTTGAGATTGATGAGATTAATGAGATTTATGAGATTCGGATTTGAGATTGCTGAGATTCAGCCAGTGAGATTGGATGAGATTCCAGTGAGATTCTGAGATTAATGAGATTTGAGATTTGAGATTGAAATGAGATTGTAGTGAAGTAAACTGAGATTGGTGAGGTGAGATTTTGAGATTGCTGAGATTGTAATCGGTGAGATTGCCGGTTCTAGAAGATGAGATTTTCGTTTGAGATTAGTCGACTGAGATTTAGACATTATGAGATTATGGTTGAGATTTGAGATTGCGCCTGAGATTTACATGAGATTGTTGAGATTTGAGATTATGAGATTATCGCTGAGATTGACTTGGTTGAGATTATTTGAGATTTGAGATTGCGTGAGATTATGAGATTTGAGATTCACGTGAGATTCGTGAGATTGTGCGGGTAGTGAGATTGGTGAGATTGATTGAGATTGTGAGATTATGAGATTGTGAGATTTGAGATTCATTCTGAGATTAGCCTGAGATTTGAGATTTATTTGAGATTTGAGATTTGAGATTTGAGATTTGACTGAGATTTTGAGATTCTGCTGAGATTCACCTTAGCCTGAGATTAATATGAGATTGTGAGATTCGTGAGATTTGAGATTCGGCTCATCGTTGAGATTTGAGATTGCGTTGAGATTTGAGATTAACACTGAGATTGTGAGATTTTGAGATTACTGAGATTTTGAGATTTTGAGATTAGGAACTGAGATTTTTGAGATTTGAGATTTTTTGAGATTGATTTGAGATTTCGCTGAGATTCAGCCGTGTTGACCTTAACAGCGTTGAGATTCCTGTTGAGATTTGAGATTTCTATACGGTGAGATTGACAATGAGATTATGAGATTCTTGAGATTTGAGATTGATTGAGATTTTGAGATTAATGAGATTACTGAGATTTGAGATTGATGAGATTGTGAGATTGTGAGATTTCTTGAGATTTGAGATTTGAGATTTCTTGAGATTGGTGAGATTGGCTGAGATTACTAGTGAGATTTGAGATTCCAATGAGATTCGTTATGAGATTTGAGATTTATTGACTGAGATTAATATGAGATTGCCCTGAGATTCTGAGATTTGAGATTTGTGTGAGATTTGAGATTCTGAGATTTGATGAGATTAACCTGTGAGATTACATGAGATTAACGTGAGATTCGCTGAGATTTTGAGATTATGAGATTGCCGTATATGAGATTTTTGAGATTTTGAGATTGTTGTGAGATTCACACAGTTGAGATTTGAGATTGTGAGATTAGATGAGATTTTGAGATTCCTGAGATTTGAGATTTAGTTGAGATTCCTTGAGATTATGGCATGAGATTACCCTGAGATTTATACCCTGAGATTTGAGATTACTCTGAGATTATGAGATTTGAGATTTGAGATTTGAGATTTGAGATTGATGAGATTGGATTGAGATTGTATGAGATTATGAGATTTATAGACTATGAGATTCGTCTTTGAGATTCTGAGATTTTGAGATTGGATGAGATTTTGAGATTTGAGATTAGGATGAGATTGTGAGATTTGAGATTGCTGAGATTACAGCGTTGAGATTCCTGGCAGAAAATGAGATTAAATGAGATTCTGAGATTTGAGATTTGAGATTTGAGATTATGAGATTATGTGAGATTCTGAGATTCGCCCTGAGATTATTTGAGATTGTTGAGATTTGAGATTTCTGAGATTCCGTGTGAGATTCAATGAGATTATGAGATTTGACTGAGATTTACTGAGATTGTGCCTGAGATTTGAGATTACTGAGATTTGTGAGATTGTGAGATTTGAGATTTGAGATTTTGAGATTAAACTTGAGATTTGAGATTTCGCTGAGATTGCCTGTGAGATTTGAGATTGGTGAGATTTGAGATTCCACAGTTGAGATTGCTGAGATTCTTCGTGTGAGATTCACATGACGTGAGATTTTGAGATTGAATTGAGATTATGAGATTTGAGATTCAATGAGATTTTGAGATTATGAGATTGGTGCATGAGATTTGAGATTGCTGAGATTTAAGTTGAGATTTGAGATTTACTGAGATTTGGATTGAGATTCCAGCAAACTGAGATTCTGACTGAGATTGTGAGATTCAGTGAGATTCCAGTTCTTTAGCTGAGATTTGAGATTTGAGATTTGAGATTATGAGATTATTCTAGTGAGATTCAAATGAGATTCTGAGATTATGAGATTCGTGAGATTTGAGATTTGAGATTATTGAGATTGTTGAGATTTGAGATTTGAGATTCCGATGTGAGATTACTGAGATTAATTCTGAGATTTGAGATTTTGTGAGATTTTGAGATTTGAGATTTTGAGATTTGAGATTCTTCATGAGATTATGAGATTAAAAGTATGAGATTCAATGAGATTTGAGATTTCCTGAGATTGTTGAGATTAGTGAGATTGAGGTGAGATTTTGAGATTGGATGTGAGATTTGAGATTTTGAGATTGAACATGAGATTTGTCGAACTCTGTGAGATTTGAGATTTGATGAGATTACCTGAGATTCGGCGCACCGTGAGATTGTGAGATTGGTGAGATTCAACATGAGATTGATGAGATTGTGAGATTGTACCTGAGATTGCTCTGAGATTGTGGCCATGAGATTCTGAGATTTTGAGATTCGCGTCCCTGAGATTTTTGAGATTCAGTGACTGAGATTGCTGCAATTGATGAGATTTGAGATTAGCAGTGAGATTTGAGATTCCTCTGAGATTCTGAGATTTGAGATTTGAGATTCTGAGATTTGAGATTTGAGATTATGTGAGATTGAATATGAGATTGTGAGATTGAGCTGAGATTGTAGACATGAGATTTGTCATGTGAGATTGTAACCTAAGAGCCTGAGATTGACCTGAGATTTAGGAAGTGAGATTGAGAATGAGATTGGTTGTTTGAGATTAGTGAGATTTCTGAGATTTGAGATTTGAGATTTGAGATTTGGTGAGATTGAAATATGAGATTTATTGAGATTTGAGATTGTGAGATTATGAGATTTGAGATTGGACGAGGTGAGATTGTGAGATTGGATGAAGATATCTGAGATTTGAGATTTGAGATTTTGAGATTTGAGATTATGAGATTATTGAGATTTGAGATTCATTTGAGATTCTGAGATTCATTGAGATTGTACATGAGATTTGAGATTTGTCGTTTGAGATTATGAGATTAATGAGATTATGAGATTCTTGAGATTGCTGTGAGATTGGTATTCAAGGATGAGATTTGAGATTTGCTCCGTCCTGAGATTTTGAGATTAGAAAACTGAGATTCGGATGAGATTTGAGATTTTCAAATGAGATTTGAGATTAGTATGAGATTTGAGATTTGATGAGATTTGAGATTAGATGAGATTTGAGATTCCTGAGATTCTGAGATTATGAGATTTGAGATTCCTGGATTGAGATTCTGGCTGAGATTAGCTGAGATTCTGAGATTCGGCCTGAGATTCGGGTGAGATTGTGAGATTTGAGATTCTGAGATTTGAGGTGAGATTTGTTGAGATTTGAGATTTGAGATTCCTGGGGTCCATGAGATTTGAGATTCCTTCTGGTTGAGATTTGAGATTTGAGATTTGAGATTCTTTGAGATTTGAGATTTGAGATTCGTTTTCTGAGATTGTGAGATTGCATTTGTGGGTGAGATTATCTGTGAGATTTTGAGATTCGCCGCTTGTAGGTGAGATTTGTGAGATTAATGAGATTATTTTGAGATTTTGAGATTATATGCTATGAGATTTGAGATTTGAGATTGGTGAGATTCAGGTGAGATTCTGAGATTCTGAGATTAGCAGTGAGATTTATGAGATTTTTGAGATTTGAGATTTTGAGATTAGAAAATTTGAAGGCACTGGGACTGAGATTATGAGATTCCTGAGATTTGAGATTGTGAGATTTTACTGAGATTACTGAGATTGTGAGATTTATGAGATTTGAGATTCTTGAGATTTTGCATGAGATTACTACTTTGAGATTTGAGATTCGGGTGGAGGTGAGATTAGATGAGATTCGCTGAGATTATTAGCCTGAGATTTGAGATTTGAGATTTCTTTGAGATTCTGAGATTCTGAGATTGTGAGATTCTGAGATTTGAGATTATCGGTGAGATTTGAGATTTGAGATTAGTGAGATTATGAGATTTCTTGAGATTTGAGATTACTGATTGAGATTTTGAGATTTCGTTGAGATTCTGAGATTAAGCTGAGATTGCCGGGGTGAGATTTTGAGATTCGCTGAGATTTGAGATTACGTGAGATTGCGCATGTCTTGAGATTAAGTGGTGACATGAGATTTTGAGATTACCGGATTCCTGAGATTGGTGAGATTTAAGATGAGATTTGAGATTTGAGATTTCATGAGATTGTGAGATTTGAGATTCCTTGAGATTCTGTTGAACTGAGATTTGAGATTCTGAGATTTGAGATTATGAGATTTGAGATTGTACATGAGATTTTCGATTACGTATAATGAGATTTCTCTATTTGAGATTTGAGATTCTGAGATTATTGAGATTTTGAGATTGTGAGATTTGAGATTGTGAGATTTGAGATTGTTGAGATTTAGTGAGATTTGAGATTAGTGAGATTTTAGGTCTCGTGTGAGATTTGAGATTCCCTGAGATTGATTCGTGAGATTTGAGATTGTTGAGATTTGTGAGATTTGTGAGATTGACTGAGATTTTATGAGATTTGAGATTTGAGATTGTCCGGAATGAGATTTTGTGAGATTAAGGCGGGTGAGATTTGAGATTCTGAGATTCGTGAGATTTGAGATTAGTCATTGAGATTATGAGATTTGAGATTTGGATGAGATTTGAGATTTGAGATTTGAGATTTACCAGTAATGAGATTTGAGATTCTGAGATTGGTGAGATTGTGAGATTTCCGCTGAGATTTTGAGATTAACGGACGCGTGTGAGATTTGAGATTGTGAGATTTAGGCGGTGCTGAGATTCTGAGATTTATGAGATTCTTCTTTACATGAGATTTCTTATGTGAGATTATCTGATGGGTGAGATTTGAGATTTTGAGATTCTTGAGATTCCTTCTTGAGATTCTGAGATTGTATGAGATTCTGAGATTTGAGATTAACGACTGAGATTCCCGTGAGATTAAGTGAGATTGATAGTTGAGATTTGAGATTCGTTTGAGATTATTAGCTACCTTGTGAGATTCAGTGAGATTCGTGAGATTTGCTGAGATTTTGAGATTCTGAGATTCCCCGTAGTGAGATTCTGAGATTAGCTGATATTGAGATTTGAGATTGATGAGATTTGAGATTTGATGAGATTTGAGATTGTAGATTGCTGAGATTGTGGCTAAAGTTGAGATTGTGTCATTGAGATTGGATGAGATTTATGAGATTTGAGATTTGAGATTTGAGATTTAGCAAATGAGATTAACACGAATGAGATTAGACTGTCTATGAGATTTGAGATTTGAGATTATGAGATTATGAGATTTGAGATTATCGGCCAGAGCTGAGATTGTGAGATTGTGCTGAGATTATACGGTGGGAAATGAGATTTGAGATTTGAGATTTGTGAGATTTATGAGATTTGAGATTTTGAGATTTTGAGATTTGAGATTTGAGATTTTGAGATTCTGAGATTGTGAGATTCTGAGATTTGAGATTACGTCGATGAGATTGATACTGAGATTTGTCTGAGATTCAATGAGATTTGAGATTTTTGAGATTACTGAGATTTGAGATTTTCATGAGATTGAGCCAGTGAGATTTGAGATTATGAGATTCTGAGATTAG"

def index(text, pattern):
	indexlist = []
	count = 0
	for base in range(0, len(text)):
		if text[base:len(pattern)+base] == pattern:
			indexlist.append(count)
		count += 1
	print(*indexlist, sep=" ")
	return "Finished"


	

if __name__ == "__main__":
	print("Type in your pattern and press 'Enter'")
	pat = input()
	print("Type in your sequence and press 'Enter'")
	seq = input()
	indices = index(seq, pat)

	'''
	YOU CAN ALSO USE THIS INSTEAD OF INPUT
	#data = sys.stdin.read()
	#pattern_text = data.split("\n")
	#indices = index(pattern_text[1], pattern_text[0])
	'''
	print(indices)