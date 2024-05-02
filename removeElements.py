def main():
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    temp = nums.copy()
    for a in temp:
        if a == val:
            nums.remove(a)

    print(nums)

main()

    