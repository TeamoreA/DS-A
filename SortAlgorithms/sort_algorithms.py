import math

def bubble_sort(arr):
    swap_count = 0
    i = 0
    while i < len(arr)-1:
        if arr[i] > arr[i+1]:
            tmp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = tmp
            swap_count += 1
        i += 1
    if swap_count >= 1:
        bubble_sort(arr)
    return arr

def selection_sort(arr, sorted_index = 0):
    max_len = len(arr)
    least_index = sorted_index
    for i in range(sorted_index, max_len-1):
        if arr[i+1] < arr[least_index]:
            least_index = i+1
    temp = arr[sorted_index]
    arr[sorted_index] = arr[least_index]
    arr[least_index] = temp
    sorted_index += 1

    if sorted_index < len(arr):
        selection_sort(arr, sorted_index)
    return arr

def insertion_sort(arr, sorted_index = 0):
    if arr[sorted_index] > arr[sorted_index+1]:
        temp = arr[sorted_index]
        arr[sorted_index] = arr[sorted_index+1]
        arr[sorted_index+1] = temp
        sorted_index += 1
    sub_list_len = len(arr[:sorted_index]) - 1
    while sub_list_len > 0:
        if arr[sub_list_len] < arr[sub_list_len - 1]:
            temp = arr[sub_list_len]
            arr[sub_list_len] = arr[sub_list_len-1]
            arr[sub_list_len-1] = temp
        sub_list_len -= 1
    if sorted_index < len(arr)-1:
        insertion_sort(arr, sorted_index)
    return arr

def bucket_sort(arr):
    max_number = max(arr)
    buckets_no = round(math.sqrt(max_number))
    new_arr = []
    for _ in range(buckets_no):
        new_arr.append([])
    for i in arr:
        target_index = math.ceil(i*buckets_no/max_number)
        new_arr[target_index-1].append(i)
    for bucket in new_arr:
        bubble_sort(bucket)
    str_arr = '{}'.format(new_arr)
    str_arr = str_arr.replace('[','')
    str_arr = str_arr.replace(']','')
    return [int(i) for i in str_arr.split(',')]

def merge(arr, l, m ,r):
    n1 = m-l+1
    n2 = r-m

    L = [0] * (n1)
    R = [0] * (n2)
    for i in range(n1):
        L[i] = arr[l+i]

    for j in range(n2):
        R[j] = arr[m+1+j]

    i = 0        
    j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n1:
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr, l, r):
    if l < r:
        m = (l+(r-1))//2
        merge_sort(arr, l, m)
        merge_sort(arr, m+1, r)

        merge(arr, l, m, r)

        return arr

def partition(arr, l, r):
    i = l - 1
    pivot = arr[r]
    for j in range(l, r):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i+1

def quick_sort(arr, l, r):
    if l < r:
        partition_index = partition(arr, l, r)
        quick_sort(arr, l, partition_index-1)
        quick_sort(arr, partition_index+1, r)
    return arr

def heap_sort(arr):
    from heap import BinaryHeap
    heap = BinaryHeap()
    arr_len = len(arr)
    for i in range(arr_len):
        heap.insert(arr[i])
    resp = []
    while arr_len > 0:
        resp.append(heap.extract())
        arr_len -= 1
    return resp

    




arr = [5,9,3,1,2,8,4,7,6]
print(heap_sort(arr))