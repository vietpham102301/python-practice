"""
Input:

    3
         n-2=2  n-1= 1 n = 0
    1 3 2 5 7
    1 swap n-1 vs 0
    7 3 2 5 1
    2 move n-2 to 0 -> move 0 to 1 -> move 1 to n-2 -> move n to 2 -> move 2 to n
    5 7 1 3 2

    2 5 7 1 3


    7 3 2 5 1
    7 5 2 3 1
    7 5 2 3 1
Output:

    2 5 7 1 3


"""


def rotate_array_clockwise(arr, k):
    n = len(arr)
    # Calculate the effective rotation amount (k modulo n)
    k = k % n # 2 % 5
    # Perform the rotation using slicing
    #-2: , + :-2
    # 4 5 , 1 2 3
    print(arr[-k:])
    print(arr[:-k])
    rotated_array = arr[-k:] + arr[:-k]
    return rotated_array

# Example usage:
original_array = [1, 2, 3, 4, 5]
k = 2  # Rotate by 2 positions
rotated = rotate_array_clockwise(original_array, k)
print(rotated)