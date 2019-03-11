def findallAnagram(input):
    dict = {}
    for strVal in input:
        key = ''.join(sorted(strVal))
        if key in dict.keys():
            dict[key].append(strVal)
        else:
            dict[key] = []
            dict[key].append(strVal)
    out    
    output = ""
    #traverse the dict
    for key,value in dict.iteritems():
        output = output + ' '.join(value) + ' '

    return output

if __name__ == "__main__":
    input = ['cat', 'dog', 'tac', 'god', 'act']
    print findallAnagram(input)

