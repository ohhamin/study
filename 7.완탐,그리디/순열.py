def perm(arr, n):
    result = []

    def recur():
        if len(result) == n:
            print(result)
            return
        for i in arr:
            if i not in result:
                result.append(i)
                recur()
                result.pop()
    recur()

arr = [1, 2, 3, 4]
perm(arr, 2)