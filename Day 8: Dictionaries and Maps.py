# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
d = {}

for i in range(n):
    x = input().split(" ")
    d[x[0]] = x[1]
while True:
    try:
        name = input()
    except EOFError:
        break
    if name in d.keys():
        print(name, d.get(name), sep="=")
    else:
        print("Not found")
        
     
