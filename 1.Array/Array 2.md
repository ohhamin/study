# Array 2

## 배열 : 2차원 배열

* 1차원 list를 묶어놓은 list

* 다차원 list는 차원에 따라 index 선언

* 배열 순회 : 행 우선 순회, 열 우선 순회

  지그재그 순회

  ```python
  for i in range(n):
      for j in range(m):
          Array[i][j + (m-1-2*j) * (i%2)]
  ```

  델타를 이용한 2차 배열 탐색 한 좌표에서 4방향의 인접 배열 요소를 탐색

  ```python
  arr[0...N-1][0...N-1]
  di = [-1, 1, 0, 0]
  dj = [0, 0, -1, 1] # 상 하 좌 우
  for i in range(N):
      for j in range(N):
          for k in range(4):
              ni = i + di[k]
              nj = j + dj[k]
              if 0<=ni<N and 0<=nj<M: # 유효 인덱스
                  print(i, j, arr[ni][nj])
              
  ```

  

## 부분집합 생성

* 부분집합의 수 : 집합의 원소가 n개일 때, 공집합을 포함한 부분집합은 2^n 개

* 비트 연산자 << : 피연산자의 비트 열을 왼쪽으로 이동시킨다.

  1 << n : 2^n 즉, 원소가 n개일 경우의 모든 부분집합의 수를 의미한다.

* 비트 연산자 & : 비트 단위로 AND 연산을 한다

  i & (1<<j) : i 의 j 번째 비트가 1 인지 아닌지를 검사한다

```python
# https://j-ungry.tistory.com/137 참고

arr = [3, 6, 7, 1, 5, 4]
n = len(arr)  # n:원소의 개수
for i in range(1<<n):
    for j in range(n):
        if i & (1<<j):
            print(arr[j], end=", ")
    print()
print()
```

## 순차 검색

* 일렬로 되어 있는 자료를 순서대로 검색하는 방법
* 정렬되어 있지 않은 경우
  * 첫 번째 원소부터 순서대로 검색 대상과 키 값이 같은 원소가 있는지 비교하며 찾는다.
  * 키 값이 동일한 원소를 찾으면 그 원소의 인덱스를 반환한다.
  * 찾고자 하는 원소의 순서에 따라 비교횟수가 결정됨
* 정렬되어 있는 경우
  * 자료를 순차적으로 검색하면서 키 값을 비교하여, 원소의 키 값이 검색 대상의 키 값보다 크면 찾는 원소가 없다는 것이므로 더 이상 검색하지 않고 검색을 종료한다.
  * 평균 비교 횟수가 반으로 줄어듬

## 바이너리 서치

* 정렬된 자료의 가운데에 있는 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속 진행하는 방법 => 검색 범위를 줄여가며 보다 빠르게 검색을 수행함
* 검색과정
  1. 자료의 중앙에 있는 원소를 고름
  2. 중앙 원소의 값과 찾고자 하는 목표 값을 비교한다.
  3. 목표 값이 중앙 원소의 값보다 작으면 자료의 왼쪽 반에 대해서 새로 검색을 수행하고, 크다면 자료의 오른쪽 반에 대해서 새로 검색을 수행한다.
  4. 찾고자하는 값을 찾을 때까지 1~3의 과정을 반복
* 구현

```python
def binarySearch(a, N, key):
    start = 0
    end = N-1
    while start <= end:
        middle = (start + end)//2
        if a[middle] == key: #검색성공
            return True
        elif a[middle] > key:
            end = middle -1
        else:
            start = middle + 1
    return False
```



## 선택 정렬

* 주어진 리스트 중에서 최소값을 찾는다.
* 그 값을 리스트의 맨 앞에 위치한 값과 교환한다.
* 맨 처음 위치를 제외한 나머지 리스트를 대상으로 위의 과정을 반복한다
* O(n^2) (교환의 횟수가 버블, 삽입정렬보다 작다)

```python
def selectionSort(a, N):
    for i in range(N-1):
        minIdx = i
        for j in range(i+1, N):
            if a[minIdx] > a[j]:
                minIdx = j
        a[i], a[minIdx] = a[minIdx], a[i]
```



## 셀렉션 알고리즘

* 저장되어 있는 자료로부터 k번째로 큰 혹은 작은 원소를 찾는 방법을 셀렉션 알고리즘 이라고 한다.
* k번째로 작은 원소를 찾는 알고리즘
* k가 비교적 작을때 유용하며, O(kn)의 수행시간을 필요로 한다(선택 정렬을 k까지 함)

```python
def select(arr, k):
    for i in range(0, k):
        minIndex = i
        for j in range(i+1, len(arr)):
            if arr[minIndex] > arr[j]:
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr[k-1]
```

