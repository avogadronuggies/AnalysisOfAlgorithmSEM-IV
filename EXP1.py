import random
import time
def insertionsort(arr1,n):
  t1=time.time()
  for j in range(1,n):
    key=arr1[j]
    i=j-1
    while i>=0 and arr1[i]>key:
      arr1[i+1]=arr1[i]
      i=i-1
    arr1[i+1]=key
    print(arr1)
  t2=time.time()
  print("Time taken for INSERTION SORT:",  (t2 - t1), "seconds")
def selectionSort(arr2,n):
  t1=time.time()
  for j in range(n):
    min=j
    for k in range(j+1,n):
      if arr2[k]<arr2[min]:
        min=k
    temp = arr2[j]
    arr2[j] = arr2[min]
    arr2[min] = temp
    print(arr2)
  t2=time.time()
  print("Time taken for INSERTION SORT:",  (t2 - t1), "seconds")
n = int(input("Enter Number of Elements:"))
arr=[]
for i in range(n):
  arr.append(random.randint(0,100))
print("Original List:")
print(arr)
arr1=arr[:]
arr2=arr[:]
print("\nINSERTION SORT:")
insertionsort(arr1,n)
print("\nSELECTION SORT:")
selectionSort(arr2,n)