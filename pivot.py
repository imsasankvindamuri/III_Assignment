num=int(input("Enter Number of Elements: "))
list1 = []
for i in range(num):
    entry=int(input("Enter element: "))
    list1.append(entry)

# file=open("./inppivot.txt")
# full=file.readlines()
# list1=[]
# for i in full:
#     try:
#         list1.append(int(i))
#     except ValueError:
#         continue

# import random as rand
# list1=[]
# for i in range(1000000000):
#     list1.append(rand.randint(0,1000000000))

print(f"\n\nUnorganized list: {list1}\n\n")

def pivot_sort(arr):
    if len(arr)>1:
        pivot=arr.pop(0)
        lower=[]
        higher=[]
        for i in arr:
            if i<pivot:
                lower.append(i)
            else:
                higher.append(i)
        higher=pivot_sort(higher)
        lower=pivot_sort(lower)
        lower.append(pivot)
        arr=lower+higher
    return arr

sort=pivot_sort(list1)

print(f"Reorganized list: {sort}\n\n")