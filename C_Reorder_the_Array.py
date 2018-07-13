def reorder(s,arr):
    count = 0
    arr = sorted(arr,reverse=True)
    i = 0
    for j in xrange(1, len(arr)):
        if arr[i] > arr[j]:
            i += 1
            count += 1         
    return count
if __name__ == '__main__':
    s = input()
    arr = map(int,raw_input().split())
    print reorder(s, arr)