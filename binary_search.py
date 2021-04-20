import random 

def binary_search(data, target, low_idx, high_idx):
    if low_idx > high_idx:
        return False
    
    mid = (low_idx + high_idx) // 2
    
    if target == data[mid]:
        return True
    
    elif target < data[mid]:
        return binary_search(data, target, low_idx, mid-1)
    
    else:
        return binary_search(data, target, mid + 1, high_idx)


if __name__ == '__main__':
    data = [random.randint(0,100) for i in range(10)]
    data.sort()

    print(data)
    target = int(input('What number would you like to find? '))
    found = binary_search(data, target, 0, len(data) - 1)
    print(found)
