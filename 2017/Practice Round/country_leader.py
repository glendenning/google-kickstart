
def solve(N, names):

    record = 0
    longestName = names[0]

    for name in names:
        # calculate unique letters
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        uniqueLetters = 0
        for letter in alphabet:
            if letter in name:
                uniqueLetters += 1
        if (uniqueLetters > record) or (uniqueLetters == record and name < longestName):     
            record = uniqueLetters
            longestName = name
    
    return longestName


T = int(raw_input())
for case in range(T):

    # Input
    N = int(raw_input())
    names = []
    for i in range(N):
        names.append(raw_input())

    print("Case #%i: %s" % (case+1, solve(N, names)))
