# a=int(input())
# b=int(input())
# print(a+b)

# a=str(input())
# print(a[-1])

# a=list(map(int,input().split()))
# x=1
# for i in a:
#     x=x*i
# t=x**(1/(len(a)))
# print(t)

# T=open('C:/Users/User/PycharmProjects/PythonProject/input.txt')
# A=T.readlines()
# x1=A[0][:-1]
# x2=A[1]
# f=1
# r=x1.split(' ')
# for y in range(0,len(r)):
#     r[y]=int(r[y])
# if x2=='+':
#     f=sum(r)
# if x2=='-':
#     f=-sum(r)+2*r[0]
# if x2=='*':
#     for i in r:
#         f=f*i
# T.close()
# T=open('C:/Users/User/PycharmProjects/PythonProject/input.txt','w')
# T.write(str(f))
# T.close()

# a=list(map(int,input().split()))
# t=int(str(a[0]),a[1])
# o=''
# def f(x,y):
#     p=[]
#     while x>0:
#         p.append(x%y)
#         x=x//y
#     return p[::-1]
# for i in f(t,a[2]):
#     o+=str(i)
# print(o)


# def nm(x,y):
#     p=[]
#     while x>0:
#         p.append(x%y)
#         x=x//y
#     return p[::-1]
#
# T=open('C:/Users/User/PycharmProjects/PythonProject/input.txt')
# A=T.readlines()
# x1=A[0][:-1]
# x2=A[1][:-1]
# x3=A[2]
# o=''
# f=1
# r=x1.split(' ')
# for y in range(0,len(r)):
#     r[y]=int(r[y],int(x3))
# if x2=='+':
#     f=sum(r)
# if x2=='-':
#     f=-sum(r)+2*r[0]
# if x2=='*':
#     for i in r:
#         f=f*i
# m=nm(f,int(x3))
# for i in m:
#      o+=str(i)
# B=open('C:/Users/User/PycharmProjects/PythonProject/output.txt','w')
# B.write(o)
# B.close()



# a=list(map(int,input().split(' ')))
# n=a[0]
# b=a[1:]
# A=(1+n)//2*n
# print(A-sum(b))

# T=input()
# K=T.split(' ')
# N=int(K[0])
# V=''
# a=K[1]
# v=1
# n=int(len(a)/int(N))
# m=[]
# for i in range(int(n)):
#     m.append(a[N*(v-1):N*v])
#     v=v+1
# for j in m:
#     j=j[::-1]
#     V+=j
# print(V)
