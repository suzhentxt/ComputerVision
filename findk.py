def tk(n, k):
    while True:
        s = str(n)
        if k <= len(s):
            return int(s[k-1])
        if n <= 60:
            tmp = f[n]
            tmp -= len(s)
            tmp //= 2
            tmp += len(s)
            if k <= tmp:
                k -= len(s)
                n -= 1
            else:
                k -= tmp
                n -= 1
        else:
            k -= len(s)
            n -= 1

n, k = map(int, input().split())

f = [0]*70
f[1] = 1
for i in range(2, 61):
    s = str(i)
    f[i] = f[i-1]*2+len(s)

if n > 60:
    print(tk(n, k))
else:
    if f[n] >= k:
        print(tk(n, k))
    else:
        print(-1)
