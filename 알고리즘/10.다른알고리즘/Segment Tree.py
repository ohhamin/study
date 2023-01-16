arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 실제로는 데이터의 개수 N에 4를 곱한 크기만큼 미리 세그먼트 트리의 공간을 할당한다.
tree = [0] * (len(arr) * 4)


# <세그먼트 트리를 배열의 각 구간 합으로 채워주기>
# start : 배열의 시작 인덱스, end : 배열의 마지막 인덱스, index : 세그먼트 트리의 인덱스
def init(start, end, index):
    # 가장 끝에 도달했으면 arr 삽입
    if start == end:
        tree[index] = arr[start]
        return tree[index]
    mid = (start + end) // 2
    # 재귀를 통해 좌측 노드와 우측 노드를 채워주면서 부모 노드의 값도 채워준다.
    tree[index] = init(start, mid, index * 2) + init(mid + 1, end, index * 2 + 1)
    return tree[index]


# <구간 합을 구하는 함수>
# start : 시작 인덱스, end : 마지막 인덱스
# left, right : 구간 합을 구하고자 하는 범위
def interval_sum(start, end, index, left, right):
    # 범위 밖에 있는 경우
    if left > end or right < start:
        return 0
    # 범위 안에 있는 경우
    if left <= start and right >= end:
        return tree[index]
    # 그렇지 않다면 두 부분으로 나누어 합을 구하기
    mid = (start + end) // 2
    # start와 end가 변하면서 구간 합인 부분을 더해준다고 생각하면 된다. (바이너리)
    return interval_sum(start, mid, index * 2, left, right) + interval_sum(mid + 1, end, index * 2 + 1, left, right)


# <특정 원소의 값을 수정하는 함수>
# 특정 원소를 수정하면 구간 합이 당연히 달라진다.
# 이때, 해당 원소를 포함하고 있는 모든 구간 합 노드들을 갱신해주면 된다. 
# (즉, 전체가 아닌 부분적인 노드들만 바꿔주면 된다!)
# start : 시작 인덱스, end : 마지막 인덱스
# what : 구간 합을 수정하고자 하는 노드
# value : 수정할 값
def update(start, end, index, what, value):
    # 범위 밖에 있는 경우
    if what < start or what > end:
        return
    # 범위 안에 있으면 내려가면서 다른 원소도 갱신
    tree[index] += value
    if start == end:
        return
    mid = (start + end) // 2
    update(start, mid, index * 2, what, value)
    update(mid + 1, end, index * 2 + 1, what, value)


init(0, len(arr) - 1, 1)
print(interval_sum(0, len(arr) - 1, 1, 0, 9))  # 0부터 9까지의 구간 합 (1 + 2 + ... + 9 + 10)
print(interval_sum(0, len(arr) - 1, 1, 0, 2))  # 0부터 2까지의 구간 합 (1 + 2 + 3)
print(interval_sum(0, len(arr) - 1, 1, 6, 7))  # 0부터 2까지의 구간 합 (7 + 8)

# arr[0]을 +4만큼 수정
update(0, len(arr) - 1, 1, 0, 4)
print(interval_sum(0, len(arr) - 1, 1, 0, 2))   # 0부터 2까지의 구간 합 ((1 + 4) + 2 + 3)

# arr[9]를 -11만큼 수정
update(0, len(arr) - 1, 1, 9, -11)
print(interval_sum(0, len(arr) - 1, 1, 8, 9))   # 8부터 9까지의 구간 합 (9 + (10 - 11))