num=int(input("Enter Number of Elements: "))
list1 = []
for i in range(num):
    entry=int(input("Enter element: "))
    list1.append(entry)

# file=open("./inpmerge.txt")
# full=file.readlines()
# list1=[]
# for i in full:
#     try:
#         list1.append(int(i))
#     except ValueError:
#         continue

# import random as rand
# list1=[]
# for i in range(10000):
#     list1.append(rand.randint(0,1000000))



print(f"\n\nUnorganized list: {list1}\n\n")

def merge_sort(arr):
    if len(arr)>1:
        arr1=arr[:len(arr)//2]
        arr2=arr[len(arr)//2:]
        
        arr1=merge_sort(arr1)
        arr2=merge_sort(arr2)
        
        lst=[]
        i=0
        j=0

        while i<len(arr1) and j<len(arr2):
            if arr1[i]>arr2[j]:
                x=arr2.pop(j)
                lst.append(x)
            else:
                x=arr1.pop(i)
                lst.append(x)
        if len(arr1)==0:
            lst+=arr2
        if len(arr2)==0:
            lst+=arr1
        arr=lst
    return arr
sort=merge_sort(list1)
print(f"Reorganized list: {sort}\n\n")