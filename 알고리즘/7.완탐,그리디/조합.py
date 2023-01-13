def comb(arr, n):
    result = []
    start = 0
    def recur(start):
        if len(result) == n:
            print(result)
            return
        for i in range(start, len(arr)):
            result.append(arr[i])
            start = i + 1
            recur(start)
            result.pop()
    recur(start)

arr = [1, 2, 3, 4]
comb(arr, 2)