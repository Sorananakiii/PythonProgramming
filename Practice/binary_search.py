
def binary_search(lists, element):
    
    mid = 0
    start = 0
    end = len(lists)
    steps = 0
    
    while(start <= end):
        steps += 1
        mide = (start+end) // 2
        if element == list[mid]
            return mid
        elif element < list[mid]
            end = mid - 1
        else:
            start = mid + 1
            
    return -1

# if __name__ == '__main__':
# sample = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# tartget = 12
# binary_search(sample, target)