def palindromepermutation(code):
	unpaired_char = set()
	for char in code:
		if char in unpaired_char:
			unpaired_char.remove(char)
		else:
			unpaired_char.add(char)

	return len(unpaired_char) <=1


if __name__ == '__main__':
   print palindromepermutation("civic")
   print palindromepermutation("madam")
   print palindromepermutation("civic1")