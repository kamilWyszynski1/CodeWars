digits = '123456789'
validSum = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9
def valid_solution(param):
    print(len(param))
    for row in param:
        if not check(row):
            return False

    for i in range(9):
        if not check(column(param, i)):
            return False

    for i in range(3):
        arr = []
        arr2 = []
        arr3  = []
        for j in range(3):
            arr.extend(param[j][i*3:(i+1)*3])
            arr2.extend(param[j+3][i*3:(i+1)*3])
            arr3.extend(param[j+6][i*3:(i+1)*3])
        print(arr, arr2, arr3)
        if not check(arr) or not check(arr2) or not check(arr3):
            return False

    return True

def column(matrix, i):
    return [row[i] for row in matrix]

def check(arr):
    if sum(arr) != validSum or set(arr) == set(digits):
        print(arr)
        return False
    return True
