
# a=[[1,2],2,3]
# sum=0
# i=0
# while i<len(a):
#      type(a[i])!=int:
#         j=0
#         while j<len(a[i]):
#             sum=sum+a[i][j]
#             j=j+1
#     else:
#         sum=sum+a[i]
#     i=i+1
# print(sum)











# l=[1,2,3]
# l2=["fg","t",6]
# l3=["a",4,"c"]
# i=0
# sum=""
# while i<len(l):
#     sum=sum+str(l[i])+"\n"+str(l2[i])+"\n"+str(l3[i])
#     sum=sum+"\n"+"\n"
#     i=i+1
# print(sum)


# l=["he","m","na","ka"]
# l1=["llo","y","me","vita"]
# i=0
# sum=0
# b=[]
# while i<len(l):
#     sum=l[i]+l1[i]
#     i=i+1
#     b.append(sum)
# print(b)
    
# l=[1,2]
# l2 =[3,4]
# l3 = l+l2
# print(l3)
# b=[]
# i=0
# while i<len(l2):
#     l.append(l2[i])
#     i+=1
# print(l)


list1 = [1,2,3,4]
i=0
while i<len(list1):
    if list1[i]==3:
        list1[i]=5
    i+=1
print(list1)

# list1=[[1,2],3,[5,6],4]

# i=0
# b=[]
# while i<len(list1):
#     if type(list1[i])!=int:
#         j=0
#         while j<len(list1[i]):
#             b.append(list1[i][j])
#             j+=1
#     else:
#         b.append(list1[i])
#     i+=1
# print(b)