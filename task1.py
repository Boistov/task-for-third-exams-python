#l1 = [3, 6, 9, 12, 15, 18, 21]
#l2 = [4, 8, 12, 16, 20, 24, 28]

#num =[]
#for i in range(len(l1)):
#    if i % 2 !=0:
#        num.append(l1[i])
#   else:
#        num.append(l2[i])
#p#rint(num)






l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

list1=[]
list2=[]

for i in range(len(l1)):
    if i % 2 != 0:
        list1.append(l1[i])

    if i % 2 == 0:
        list2.append(l2[i])
list3 = list1+list2

print(list1)
print(list2)
print(list3)
