class Solution:
	"""
	def longestValidParentheses(self, s):
		longest, last, indices = 0, -1, []
		for i in xrange(len(s)):
			if s[i] == '(':
				indices.append(i)
			elif not indices:
				last = i
			else:
				indices.pop()
				if not indices:
					longest = max(longest, i - last)
				else:
					longest = max(longest, i - indices)
		return longest
	"""
	def longestValidParentheses(self, s): 
	    if (len(s) <= 1): 
	        return 0
	      
	    # Initialize curMax to zero  
	    curMax = 0
	  
	    longest = [0] * (len(s)) 
	  
	    # Iterate over the string starting  
	    # from second index 
	    for i in range(1, len(s)): 
	    	print("i", i)
	    	print("longest0", longest[i])
	        if ((s[i] == ')' and i - longest[i - 1] - 1 >= 0 and s[i - longest[i - 1] - 1] == '(')):  
	                longest[i] = longest[i - 1] + 2
	                print("longest", longest[i])
	                if (i - longest[i - 1] - 2 >= 0): 
	                    longest[i] += (longest[i - longest[i - 1] - 2]) 
	                else: 
	                    longest[i] += 0
	                print("longest2", longest[i])
	                curMax = max(longest[i], curMax) 
	    return curMax 

if __name__ == "__main__":
	#print Solution().longestValidParentheses("()")
	print Solution().longestValidParentheses(")((()())()")

