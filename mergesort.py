def main():
    print(mergesort([0], [1], 0, 1))

def mergesort(list1: list[int], list2: list[int], m: int, n: int) -> list:
    list1 = list1[:m] + list2[:n]
    list1.sort()
    return list1

main()