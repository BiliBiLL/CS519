def qsort(arry):
    if arry == []:
        return []
    else:
        pivot = arry[0]
        left = [x for x in arry if x < pivot]
        right = [y for y in arry[1:] if y >= pivot]
        return [qsort(left)] + [pivot] + [qsort(right)]


if __name__ == "__main__":
    x = qsort([3,5,2,7,8])
    print x
