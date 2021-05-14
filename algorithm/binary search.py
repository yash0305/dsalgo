
# def linearSearch(numList,numberToFind):
    
#     for index, element in enumerate(numList):
#         if numList[index] == numberToFind:
#             return index
#     return -1 

# [1 , 2 ,3, 4, 5,6,7]

# def binarySearch(numList,numberToFind):
#     leftIndex = 0
#     rightIndex = len(numList)
#     midIndex = 0

#     while leftIndex <= rightIndex:
#         midIndex = (leftIndex+rightIndex)//2
#         midNumber = numList[midIndex]

#         if midNumber == numberToFind:
#             return midIndex

#         if midNumber < numberToFind:
#             leftIndex = midIndex + 1 
#         else:   
#             rightIndex = midIndex -1

#     return -1    


# if __name__ == '__main__':
#     numList = [i for i in range(1000)]
#     numberToFind = 999

#     index = binarySearch(numList,numberToFind)
#     print(f"Number found at index {index} using binary search")

def binary_search_recursive(numbers_list, number_to_find, left_index, right_index):
    if right_index < left_index:
        return -1

    mid_index = (left_index + right_index) // 2
    if mid_index >= len(numbers_list) or mid_index < 0:
        return -1

    mid_number = numbers_list[mid_index]

    if mid_number == number_to_find:
        return mid_index

    if mid_number < number_to_find:
        left_index = mid_index + 1
    else:
        right_index = mid_index - 1

    return binary_search_recursive(numbers_list, number_to_find, left_index, right_index)

if __name__ == '__main__':
    numbers_list = [12, 15, 17, 19, 21, 24, 45, 67]
    number_to_find = 45

    index = binary_search_recursive(numbers_list, number_to_find, 0, len(numbers_list))
    print(f"Number found at index {index} using binary search")