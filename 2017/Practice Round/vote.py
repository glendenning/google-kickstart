
def solve(N, M):
    # N: num of voters for A
    # M: num of voters for B
    # Find the chance of A receiving all the votes
    num = N - M 
    totalVoters = N + M 
    ans = num / totalVoters
    
    return ans



T = int(raw_input())
for case in range(T):
    N, M = map(float, raw_input().split(' '))

    result = solve(N, M)

    print("Case #%i: %f" % (case+1, result))