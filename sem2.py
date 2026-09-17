# #задача1
# a=list(map(int,input().split(' ')))
# n=a[0]
# b=a[1:]
# A=(1+n)//2*n
# print(A-sum(b))

##задача2
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

# #задача3
# s=input()
# def f(st):
#     st=st.replace('E',',')
#     st=st.replace('3',',')
#     st=st.replace('J','.')
#     st=st.replace('L','.')
#     st=st.replace('2','!')
#     st=st.replace('S','!')
#     st=st.replace('5','?')
#     st=st.replace('Z','?')
#     if len(st)%2==1:
#         if st[(len(st)//2)+1] in 'A, H, I, M, O, T, U, V, W, X, Y, 1, 8':
#             if st==st[::-1]:
#                 return 1
#         else:
#             if st==st[::-1]:
#                 return 1
# if s==s[::-1]:
#     n=1
# if n==1 and f(s)!=1:
#     print('string is a regular polindrome')
# if n!=1 and f(s)==1:
#     print('mirror string')
# elif n!=1 and f(s)!=1:
#     print('string is not polindrome')
# elif n==1 and f(s)==1:
#     print('mirror polindrome')


# #задача4
# lst = [1, 2, 3, 4, 5, 6]
# lst[::2], lst[1::2] = lst[1::2], lst[::2]
# print(lst)

# #задача5
# lst = [1, 2, 3, 4, 5]
# lst = lst[-1:] + lst[:-1]
# print(lst)

# #задача6
# a=list(map(int,input().split()))
# for i in a:
#     if a.count(i)==1: print(i)

# #задача7
# a=list(map(int,input().split()))
# c=0
# e=0
# for i in a:
#     if a.count(i)>c:
#         e=i
#         c=a.count(i)
# print(e)

# #задача9
# t=open('input.txt').read()
# n=['.','...','!','?','?!']
# for i in n:
#     i.replace(n,'-')
#     i.replace(n, '-')
# print(t.count('-'))