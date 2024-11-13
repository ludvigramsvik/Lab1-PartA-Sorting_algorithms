from faker import Faker
import copy
import time
import matplotlib.pyplot as plt
import numpy as np

# Testlists and -profiles
fake = Faker()
testProfiles = [fake.profile() for i in range(10)]
testList = [int(fake.numerify()) for i in range(1000)]

#print("Original List: ", testList)

"""------------------------------------- Task 1: Bubble Sort -------------------------------------"""
def BubbleSort(data, key=None):
    sorted_data = copy.copy(data)
    
    if len(data) <= 1: return sorted_data
    
    for i in range(len(sorted_data)):
        swapped = False
        for j in range(len(sorted_data) - 1 - i):
            # Handle both dictionaries and lists
            if key:
                if sorted_data[j][key] > sorted_data[j + 1][key]:
                    sorted_data[j], sorted_data[j + 1] = sorted_data[j + 1], sorted_data[j]
                    swapped = True
            else:
                if sorted_data[j] > sorted_data[j + 1]:
                    sorted_data[j], sorted_data[j + 1] = sorted_data[j + 1], sorted_data[j]
                    swapped = True
        
        if not swapped:
            break

    return sorted_data

#for profile in BubbleSort(testProfiles, 'birthdate'): print(profile['birthdate'])
#print(BubbleSort(testList))


"""------------------------------------- Task 2: Selection Sort -------------------------------------"""
def SelectionSort(data, key=None):
    sorted_data = copy.copy(data)
    
    if len(data) <= 1: return sorted_data

    for i in range(len(sorted_data)):
        min_idx = i
        # Handle both dictionaries and lists
        for j in range(i + 1, len(sorted_data)):
            if key:
                if sorted_data[j][key] < sorted_data[min_idx][key]:
                    min_idx = j
            else:
                if sorted_data[j] < sorted_data[min_idx]:
                    min_idx = j

        if min_idx != i:
            sorted_data[i], sorted_data[min_idx] = sorted_data[min_idx], sorted_data[i]

    return sorted_data

#for profile in SelectionSort(testProfiles, 'birthdate'): print(profile['birthdate'])
#print(SelectionSort(testList))


"""------------------------------------- Task 3: Merge Sort -------------------------------------"""
def MergeSort(data):
    sorted_data = copy.copy(data)
    
    if len(sorted_data) <= 1: return sorted_data

    lst1 = sorted_data[ : len(sorted_data) // 2]
    lst2 = sorted_data[len(sorted_data) // 2 : ]

    sortedLst1 = MergeSort(lst1)
    sortedLst2 = MergeSort(lst2)

    return Merge(sortedLst1, sortedLst2)

def Merge(lst1, lst2):
    result = []
    i, j = 0, 0

    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            result.append(lst1[i])
            i += 1
        else:
            result.append(lst2[j])
            j += 1

    result.extend(lst1[i:])
    result.extend(lst2[j:])

    return result


#print(MergeSort(testList))

"""------------------------------------- Task 4: Comparison -------------------------------------"""
def CalculateTime():
    bubbleSortClocks = []
    selectionSortClocks = []
    mergeSortClocks = []
    
    
    #Number of iterations made. Each iteration has a new random list 
    for i in range(1, 400):
        listTiming = [int(fake.numerify()) for j in range(i)]
        
        #  --Bubble--
        #Start timer
        start_time1 = time.perf_counter ()
        BubbleSort(listTiming)
        #Stop timer
        end_time1 = time.perf_counter ()
        bubbleSortClocks.append(end_time1 - start_time1)
        
        
        #  --Selection--
        #Start timer
        start_time2 = time.perf_counter ()
        SelectionSort(listTiming)
        #Stop timer
        end_time2 = time.perf_counter ()
        selectionSortClocks.append(end_time2 - start_time2)
        
        #  --Merge--
        #Start timer
        start_time3 = time.perf_counter ()
        MergeSort(listTiming)
        #Stop timer
        end_time3 = time.perf_counter ()
        mergeSortClocks.append(end_time3 - start_time3)
    
    VisualizeTiming(bubbleSortClocks, "Bubble sort", "Green")
    VisualizeTiming(selectionSortClocks, "Selection Sort", "Blue")
    VisualizeTiming(mergeSortClocks, "Merge Sort", "Red")


def VisualizeTiming(Y, lbl, clr):
    X = [i for i in range(len(Y))]
    
    plt.scatter(X, Y, marker=".", color=clr, label=f"Total time: {np.sum(Y)}")
    
    plt.xlabel("Numbers of sorting points")
    plt.ylabel("Time for each iteration")
    plt.title(f"{lbl}")

    plt.legend()
    plt.show()
        

#Start calculations 
CalculateTime()