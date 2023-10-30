# Enter your code here. Read input from STDIN. Print output to STDOUT
x = int(input())

for i in range(0, x):
    s = input()
    print(str(s[0::2] + " " + s[1::2]))
