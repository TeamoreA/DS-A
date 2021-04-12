def palindrome(s, start, end):
    if start > end:
        return 0
    elif start == end:
        return 1
    elif s[start] == s[end]:
        pali_resp = palindrome(s, start+1, end-1)
        return 2 + pali_resp
    else:
        opt1= palindrome(s, start+1, end)
        opt2= palindrome(s, start, end-1)
        return max(opt1, opt2)

# print(palindrome('elrmenmet', 0, 8)) 

def min_cost_2d_array(two_d_array, row, col):
    if row == -1 or col == -1:
        return float('inf')
    elif row == 0 and col == 0:
        return two_d_array[row][col]
    else:
        opt1 = min_cost_2d_array(two_d_array, row-1, col)
        opt2 = min_cost_2d_array(two_d_array, row, col-1)
        return min(opt1, opt2) + two_d_array[row][col]

two_d_array = [
    [4,7,8,6,4],
    [6,7,3,9,2],
    [3,8,1,2,4],
    [7,1,7,3,7],
    [2,9,8,9,3]
]
# print(min_cost_2d_array(two_d_array, 4,4))

def num_of_paths(arr, row, col, cost):
    if cost < 0:
        return 0
    elif row == 0 and col == 0:
        if cost - arr[0][0] == 0:
            return 1
        else:
            return 0
    elif row == 0:
        return num_of_paths(arr, row, col-1, cost - arr[row][col])
    elif col == 0:
        return num_of_paths(arr, row-1, col, cost- arr[row][col])
    else:
        opt1 = num_of_paths(arr, row-1, col, cost - arr[row][col])
        opt2 = num_of_paths(arr, row, col-1, cost - arr[row][col])
        return opt1+opt2

arr = [
    [4,7,1,6],
    [5,7,3,9],
    [3,2,1,2],
    [7,1,6,3]
]

print(num_of_paths(arr,3,3,25))


