import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
integers = list(map(int, data[1:]))
x = 0
y = 0
arrayx = []
arrayy = []
for i in range(0,2*n,2):
    arrayx.append([integers[i],i])
arrayx.sort()
arrayx.reverse()
for i in range(1,2*n,2):
    arrayy.append([integers[i],i])
arrayy.sort()
arrayy.reverse()
while len(arrayx)>0:
    x = x + arrayx[0][0]
    if len(arrayy)>0:
        for j in range(len(arrayy)):
            if arrayy[j][1] == (arrayx[0][1]+1):
                arrayy.remove(arrayy[j])
                break
    del(arrayx[0])
    if len(arrayy) > 0:
        y = y + arrayy[0][0]
        for j in range(len(arrayx)):
            if arrayx[j][1] == (arrayy[0][1]-1):
                arrayx.remove(arrayx[j])
                break
        del(arrayy[0])

output = str(x-y)
sys.stdout.write(str(output))