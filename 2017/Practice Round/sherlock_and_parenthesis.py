

def solve(l, r):

    n = min(l, r)
    if n <= 1:
        return n
    return (n + 1) * n / 2


T = int(raw_input())
for case in range(T):

    l, r = map(int, raw_input().split(' '))

    print("Case #%d: %d" % (case+1, solve(l, r)))

