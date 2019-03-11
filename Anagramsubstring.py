
MAX=256

def compare(arr1, arr2):
    for i in range(MAX):
        if arr1[i] != arr2[i]:
            return False
    return True


def search(pat, txt):
    M = len(pat)
    N = len(txt)
    #print("M and N", M, N)
    countP = [0]*MAX
    countTW = [0]*MAX
    for i in range(M):
        #print("before countP", i, (countP[ord(pat[i]) ]))
        (countP[ord(pat[i]) ]) += 1
        #print("after countP", (countP[ord(pat[i]) ]))
        #print("before countTW", (countTW[ord(txt[i]) ]))
        (countTW[ord(txt[i]) ]) += 1
        #print("after countTW", (countTW[ord(txt[i]) ]))

    #print("before compare ", i, countP, countTW)
    for i in range(M,N):
        #print("compare ", i, countP, countTW)
        if compare(countP, countTW):
            print("Found at Index", (i-M))

        (countTW[ ord(txt[i]) ]) += 1
        (countTW[ ord(txt[i-M]) ]) -= 1

    if compare(countP, countTW):
        print("Found at Index down", N-M)

def main():
    txt = "BACDGABCDA"
    pat = "ABCD"
    search(pat, txt)

if __name__ == "__main__":
    main()
