def insertion_sort(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1

    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge(arr, left, mid, right):
    left_copy = arr[left:mid+1]
    right_copy = arr[mid+1:right+1]

    left_index = right_index = 0
    k = left

    while left_index < len(left_copy) and right_index < len(right_copy):
        if left_copy[left_index] <= right_copy[right_index]:
            arr[k] = left_copy[left_index]
            left_index += 1
        else:
            arr[k] = right_copy[right_index]
            right_index += 1
        k += 1

    while left_index < len(left_copy):
        arr[k] = left_copy[left_index]
        left_index += 1
        k += 1

    while right_index < len(right_copy):
        arr[k] = right_copy[right_index]
        right_index += 1
        k += 1

def timsort(arr):
    min_run = 32
    n = len(arr)

    for i in range(0, n, min_run):
        insertion_sort(arr, i, min((i + min_run - 1), (n - 1)))

    size = min_run
    while size < n:
        for left in range(0, n, 2 * size):
            mid = left + size - 1
            right = min((left + 2 * size - 1), (n - 1))
            merge(arr, left, mid, right)
        size *= 2

# Ejemplo de uso
arr = [64, 34, 25, 12, 22, 11, 90]
timsort(arr)
print("Arreglo ordenado:", arr)
