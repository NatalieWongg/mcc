import sys
input = sys.stdin.read
data = input().split()

N, M, K = int(data[0]), int(data[1]), int(data[2])
a = list(map(int, data[3:]))
destroyed = False
X = 1
result = [0] * N

while destroyed ==False:
    i = 0
    for arrow in range(K):
        for j in range(len(a)): 
            damage = (M*X) - (j - i)*(j-i)
            if damage >0:
                a[j]= a[j] - damage
        for j in range(N):
            if a[j] <=0:
                a [j] = 0
                if j < N/2:
                    i = i + 1
                if j > N/2:
                    i = i - 1
    if a == result:
        destroyed = True
    else:
        X = X + 1
        a = list(map(int, data[3:]))
print(X)
