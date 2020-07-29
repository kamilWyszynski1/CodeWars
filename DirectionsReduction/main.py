pairs = [{"NORTH", "SOUTH"}, {"WEST", "EAST"}]
def dirReduc(arr):
    x = 0 
    while True:
        if x == len(arr) - 1 or arr == []:
            return arr
        pair = {arr[x], arr[x+1]}
        if pair in pairs:
            del arr[x]
            del arr[x]
            x = 0
        else:
            x+=1
