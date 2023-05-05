"""
module providing binary_search_recursive function
"""
def binary_search_recursive(target: int, *args: tuple , left = 0 ,right = None) -> int:
    """
    This function is implemented
    for recursive binary search 
    """
    if right is None:
        right = len(args) - 1
    if left > right:
        return ValueError("Item Not Found in the Array")
    mid = (left + right) // 2
    if args[mid] == target:
        return mid
    if args[mid] > target:
        return binary_search_recursive(target,*args, left=left,right= mid - 1)
    return binary_search_recursive(target,*args, left=mid + 1, right=right)
print(binary_search_recursive(111,1,2,3,5,7,9,11,13))












