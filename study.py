'''
#汉诺塔
count = 0
def hanoi(n,src,dst,mid):
	global count
	if n == 1:
		print("{}:{}->{}".format(1,src,dst))
		count += 1
	else:
		hanoi(n-1, src, mid, dst)
		print("{}:{}->{}".format(n,src,dst))
		count += 1
		hanoi(n-1, mid, dst, src)

hanoi(10,'A','C','B')
'''
'''
#科赫曲线
import turtle
def koch(size,n):
	if n == 0:
		turtle.fd(size)
	else:
		for angle in [0,60,-120,60]:
			turtle.left(angle)
			koch(size/3,n-1)
def main():
	size,n =eval(input("请依次输入边长和遍数，绘制科赫多边形"))
	angle=360/n
	turtle.setup(600,600)
	turtle.penup()
	turtle.goto(-200,100)
	turtle.pendown()
	turtle.pensize(2)
	for i in range(0,n):
		koch(size,n)
		turtle.right(angle)
	turtle.hideturtle()
	turtle.done()
main()
'''
'''
def prime(m):
    for i in range(2,n):
        if m%i == 0:
            return False
    return True

n = eval(input())
count=0
if '.' in str(n):
    n=int(n)+1
while count<5:
    if prime(n):
        count+=1
        if count<5:
            print(n,end=",")
        else:
            print(n)
    n+=1
    '''
'''   
s = 
ls=s.split()
d={}
for word in ls:
	d[word]=d.get(word,0)+1
lt=list(d.items())
lt.sort(key=lambda x:x[1])
name,count=lt[0]
print(name)
'''
try:
	s=input()
	if complex(s)==complex(eval(s)):
		print(eval(s)**2)
except :
	print("输入有误")