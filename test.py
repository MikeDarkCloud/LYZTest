#冒泡排序
a = [3,2,5,7,85,8,3,0,54,77,99,9]

for i in range(len(a)):
    for j in range(len(a)-1):
        if a[j]>a[j+1]:
            tmp = a[j]
            a[j]=a[j+1]
            a[j+1]=tmp
print(a)


#选择排序
b = [3,2,5,7,85,8,3,0,54,77,99,9]
for i in range(len(b)):
    for j in range(len(b)-i):
       tmp = b[i]
       if b[i]>b[j+1] and b[j+1]<tmp:
            tmp = b[j+1]

       b[i]=tmp


print(b)
def selection_sort(list):
    n=len(list)
    for i in range (0,n):
        min = i
        for j in range(i+1,n):
            if list[j]<list[min]:
                min=j
                list[min],list[i]=list[i],list[min]
    return list



#快速排序









