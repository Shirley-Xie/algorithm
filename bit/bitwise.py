# Python3 code to find the element that
# appears once
def getSingle(arr, n):
    ones = 0
    twos = 0

    for i in range(n):
        # 有0则为0
        twos = twos | (ones & arr[i])
        ones = ones ^ arr[i]
        common_bit_mask = ~(ones & twos)
        # Remove common bits (the bits that
        # appear third time) from 'ones'
        ones &= common_bit_mask
        # Remove common bits (the bits that
        # appear third time) from 'twos'
        twos &= common_bit_mask

    return ones


# driver code
arr = [3, 3, 1, 3, 1, 1, 5]
n = len(arr)
print("The element with single occurrence is ", getSingle(arr, n))

