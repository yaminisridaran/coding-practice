
def findAllConcatenatedWordsInADict(words):
	print(words)
	lookup = set(words)
	print(lookup)
	result = []
	for word in words:
		dp = [False] * (len(word)+1)
		dp[0] = True
		print(word, dp)
		for i in xrange(len(word)):
			if not dp[i]:
				continue
           
			for j in xrange(i+1, len(word)+1):
				print("line 16", j, i)
				print(word[i:j])
				if j - i < len(word) and word[i:j] in lookup: 
					dp[j] = True
					print("line 20", dp[j], j)

			if dp[len(word)]:
				print("line23", dp[len(word)], word)
				result.append(word)
				break

	return result
        
        """
	    for i in xrange(len(word)):
          if not dp[i]:
            continue

            for j in xrange(i+1, len(word)+1):
            	if j - i < len(word) and word[i:j] in lookup: 
            		dp[j] = True

            if dp[len(word)]:
            	result.append(word)
            	break
            	"""

    


def main():
   words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
   print(findAllConcatenatedWordsInADict(words))


if __name__ == '__main__':
    main()
