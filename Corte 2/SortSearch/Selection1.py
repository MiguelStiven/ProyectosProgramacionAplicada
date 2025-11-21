def selectionSort(arr, n):
    for i in range(n - 1):
        minIndex = i

        for j in range(i + 1, n):
            if arr[j] < arr[minIndex]:
                minIndex = j

        if minIndex != i:
            arr[i], arr[minIndex] = arr[minIndex], arr[i]

def printArray(arr, n):
    for i in range(n):
        print(arr[i], end=" ")
    print()

def main():
    arr = [2, 1, 9, 11, 4]
    n = len(arr)

    print("Arreglo original:")
    printArray(arr, n)

    selectionSort(arr, n)

    print("Arreglo ordenado:")
    printArray(arr, n)

if __name__ == "__main__":
    main()
