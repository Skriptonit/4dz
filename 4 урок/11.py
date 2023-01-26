x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x = abs(x1-x2)
y=abs(y1-y2)
if(x==1 and y==2) or (x==2 and y==1):
    print("YES")
else:
    print("NO")