# readlines 함수는 리스트형태로 만들어주는구나

f = open("writeData.txt", 'r')

lines = f.readlines()

for line in lines:
    print(line)
f.close()