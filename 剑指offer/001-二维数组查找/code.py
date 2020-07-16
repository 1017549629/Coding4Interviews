
def find(target, array):
    i = 0
    j = len(array[0]) - 1 #这里len(array[0])只能使用array[0],因为这个二维数组的维度没有定义，也可以是假二维真一维np.array([[1], [4]])
    while i < len(array) and j >= 0: #也可以是i <= len(array)-1 and j >= 0
        base = array[i][j]
        if target == base:
            return True
        elif target > base: 
            i += 1
        else:
            j -= 1
    return False

print(find(4,[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]))
