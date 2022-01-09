def selectionSort(alist):
    for i in range(len(alist)):
        
        # Find the minimum element in remaining
        minPosition = i

        for j in range(i+1, len(alist)):# for (int j = i+1; j < n; j++)
            if alist[minPosition] > alist[j] :
                minPosition = j

                
        # Swap the found minimum element with minPosition 
        temp = alist[i]
        alist[i] = alist[minPosition]
        alist[minPosition] = temp


    return alist

print(selectionSort([64,25,12,22,11]))
