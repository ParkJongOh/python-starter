#0과 빈값 = False
# 나머지는 true

# readline.py
f = open("writeData.txt", 'r')

while True:
    line = f.readline()
    if not line: break
    print(line)

f.close()