import timeit
import matplotlib.pyplot as plt

listA = [54,26,93,17,77,31,44,55,20]
listB = [54,26,93,17,77,31,44,55,20,21,48,65,98,48,12,36,59,75,49,46,10,25,30,97,45]
listC = [54,26,93,17]
listD = [100, 21, 48, 74, 51, 95, 57, 69, 88, 59, 24, 81, 2, 4, 7, 68, 1, 79, 43, 72, 56, 82, 12, 20, 67, 25, 33, 77, 99, 58, 55, 76, 11, 30, 15, 63, 46, 75, 89, 37, 9, 14, 35, 8, 86, 5, 40, 71, 42, 17, 50, 96, 29, 3, 91, 19, 87, 16, 64, 41, 32, 6, 18, 92, 73, 27, 28, 49, 65, 84, 23, 31, 39, 22, 38, 97, 80, 66, 93, 44, 90, 98, 61, 10, 62, 47, 45, 26, 34, 13, 36, 52, 94, 83, 53, 54, 70, 60, 78, 85]

#MODIFIED QUICKSORT

def mo3_quickSort(alist):
   mo3_quickSortHelper(alist,0,len(alist)-1)

def mo3_quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = mo3_partition(alist,first,last)

       mo3_quickSortHelper(alist,first,splitpoint-1)
       mo3_quickSortHelper(alist,splitpoint+1,last)

        
def mo3(alist, first, last):
    a = alist[first]
    b = alist[last]
    c = alist[int((last-first)/2)]
    if a > b:
        if a < c:
            med = a
        elif b > c:
            med = b
        else:
            med = c
    else:
        if a > c:
            med = a
        elif b < c:
            med = b
        else:
            med = c
    return med

    

def mo3_partition(alist,first,last):
    
   pivotvalue = mo3(alist, first, last)

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp

   return rightmark


# STANDARD QUICKSORT (from the textbook)



def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark



def timingTest():
    s = "from sorting import quickSort,mo3_quickSort,listA,listB,listC,listD"
    for x in range(0, 10):
        plt.plot(timeit.timeit("quickSort(listA)", setup=s, number=1), x, "ro")
        plt.plot(timeit.timeit("quickSort(listB)", setup=s, number=1), x, "rs")
        plt.plot(timeit.timeit("quickSort(listC)", setup=s, number=1), x, "r^")
        plt.plot(timeit.timeit("mo3_quickSort(listA)", setup=s, number=1), x, "bo")
        plt.plot(timeit.timeit("mo3_quickSort(listB)", setup=s, number=1), x, "bs")
        plt.plot(timeit.timeit("mo3_quickSort(listC)", setup=s, number=1), x, "b^")
    plt.xlabel("Execution Time (s)")#Labels for the x- and y-axis
    plt.ylabel("Iteration")
    
def timingTest2():
    s = "from sorting import quickSort,mo3_quickSort,listA,listB,listC,listD"
    for x in range(0, 10):
        plt.plot(timeit.timeit("quickSort(listD)", setup=s, number=1), x, "rx")
        plt.plot(timeit.timeit("mo3_quickSort(listD)", setup=s, number=1), x, "bx")
    plt.xlabel("Execution Time (s)")#Labels for the x- and y-axis
    plt.ylabel("Iteration")
