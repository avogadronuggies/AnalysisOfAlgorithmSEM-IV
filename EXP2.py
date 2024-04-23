import random
import time


def mergeSort(arr):
  if len(arr) > 1:
    mid = len(arr) // 2
    L = arr[:mid]
    R = arr[mid:]
    mergeSort(L)
    mergeSort(R)
    i = j = k = 0
    while i < len(L) and j < len(R):
      if L[i] <= R[j]:
        arr[k] = L[i]
        i += 1
      else:
        arr[k] = R[j]
        j += 1
      k += 1
    while i < len(L):
      arr[k] = L[i]
      i += 1
      k += 1
    while j < len(R):
      arr[k] = R[j]
      j += 1
      k += 1
  print(arr)
  return arr


def partition(arr, low, high):
  pivot = arr[low]
  i = low + 1
  j = high

  while True:
    while i <= j and arr[i] <= pivot:
      i += 1
    while i <= j and arr[j] > pivot:
      j -= 1
    if i <= j:
      arr[i], arr[j] = arr[j], arr[i]
    else:
      break

  arr[low], arr[j] = arr[j], arr[low]
  print(arr)
  return j


def quickSort(arr, low, high):
  if low < high:
    pivot_index = partition(arr, low, high)
    quickSort(arr, low, pivot_index - 1)
    quickSort(arr, pivot_index + 1, high)


n = int(input("Enter Number of Elements: "))
arr = []

for i in range(n):
  arr.append(random.randint(0, 100))

print("Original List:")
print(arr)

arr1 = arr[:]
arr2 = arr[:]

print("\nMerge SORT:")
t1 = time.time()
print(mergeSort(arr1))
t2 = time.time()
print("Time taken for MERGE SORT:", (t2 - t1), "seconds")

print("\nQUICK SORT:")
t3 = time.time()
quickSort(arr2, 0, len(arr) - 1)
print(arr2)
t4 = time.time()
print("Time taken for QUICK SORT:", (t4 - t3), "seconds")
