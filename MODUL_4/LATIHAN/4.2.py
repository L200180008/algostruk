def binSE(kumpulan, target):
    low = 0
    high = lwn(kumpulan) - 1

    while low <= high:
        mid = (high+low) // 2
        if kumpulan[mid] == target:
            return True
        elif target < kumpulan[mid]:
            high = mid -1
        else:
            low = mid + 1
    return False
