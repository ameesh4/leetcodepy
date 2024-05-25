def subSets(arr, n, r,index, data, i, res):
        if(index == r):
            temp = data.copy()
            res.append(temp)
            return
        
        if(i >= n):
            return
        
        data[index] = arr[i]
        subSets(arr, n, r,index + 1, data, i + 1, res)
        
        subSets(arr, n, r, index, data, i + 1, res)
        

def main():
    res = []
    nums = [-1,0,1,2,-1]
    subSets(nums, len(nums), 3, 0, [0]*3, 0, res)
    print(res)

main()