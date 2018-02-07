def fin_product(k, nums):
    status = (1, 0) # (product of elements in window, left window)
    result = 0
    for i, num in enumerate(nums):
        print('num is: ', num)
        print('i is: ', i)
        product, left = status
        product *= num
        print('product is: ', product)
        while product >= k and left < i+1:
            product /= nums[left]
            left += 1
        status = (product, left)
        print('status is: ', status)
        result += i - left + 1
        print('res is: ', result)
        print('--------------------')
    return result


if __name__ == "__main__":
    nums  = [10, 5, 2, 6]
    k = 100
    print(fin_product(k,nums))