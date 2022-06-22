# 트리

## 트리

* 비선형 구조
* 원소들 간에 1:n 관계를 가지는 자료구조
* 노드(node) : 트리의 원소
* 간선(edge) : 노드를 연결하는 선, 부모 노드와 자식 노드를 연결
* 루트노드(root node) : 트리의 시작 노드
* 노드의 차수 : 노드에 연결된 자식 노드의 수  

## 이진 트리

* 모든 노드들이 최대 2개의 서브트리를 갖는 특별한 형태의 트리

* 포화 이진 트리 : 모든 레벨에 노드가 포화상태로 차 있는 이진 트리

  ![image-20220621150554967](Tree.assets/image-20220621150554967.png)

* 완전 이진 트리 : 높이가 h이고 노드 수가 n개 일 때, 포화 이진 트리의 노드 번호 1번부터 n번까지 빈자리가 없는 이진 트리

  ![image-20220621150609910](Tree.assets/image-20220621150609910.png)

* 편향 이진 트리 : 높이 h에 대한 최소 개수의 노드를 가지면서 한쪽 방향의 자식 노드만을 가진 이진 트리

  ![image-20220621150625981](Tree.assets/image-20220621150625981.png)

* 이진트리 순회 : 트리의 각 노드를 중복되지 않게 방문하는 것

  * 전위 순회 : VLR - 부모노드 방문 후 자식노드를 좌, 우 순서로 방문

    ![image-20220316094919211](Tree.assets/image-20220316094919211.png)

    ![image-20220317171124346](Tree.assets/image-20220317171124346.png)

    
  
  * 중위 순회 : LVR - 왼쪽 자식노드, 부모노드, 오른쪽 자식노드 순으로 방문
  
    ![image-20220317171150801](Tree.assets/image-20220317171150801.png)
  
    ![image-20220317171203560](Tree.assets/image-20220317171203560.png)
  
  * 후위 순회 : LRV - 자식노드를 좌우 순서로 방문한 후, 부모노드로 방문한다.
  
    ![image-20220317171218928](Tree.assets/image-20220317171218928.png)
  
    ![image-20220317171227704](Tree.assets/image-20220317171227704.png)

## 이진트리의 표현

* ![image-20220317173106617](Tree.assets/image-20220317173106617.png)

* ![image-20220317173115321](Tree.assets/image-20220317173115321.png)

* ![image-20220317173124249](Tree.assets/image-20220317173124249.png)

* ![image-20220317173136049](Tree.assets/image-20220317173136049.png)

* 비효율적

* ![image-20220317173736226](Tree.assets/image-20220317173736226.png)

* ![image-20220317173749697](Tree.assets/image-20220317173749697.png)

* ![image-20220317173756786](Tree.assets/image-20220317173756786.png)

* ![image-20220317182249220](Tree.assets/image-20220317182249220.png)

  

## 이진탐색 트리

* ![image-20220317183447861](Tree.assets/image-20220317183447861.png)

* ![image-20220317183700142](Tree.assets/image-20220317183700142.png)

* ![image-20220317183735021](Tree.assets/image-20220317183735021.png)

* ![image-20220317183743037](Tree.assets/image-20220317183743037.png)


- https://velog.io/@seanlion/bstimplementation

## 힙

* ![image-20220317231644752](Tree.assets/image-20220317231644752.png)
* ![image-20220318141547793](Tree.assets/image-20220318141547793.png)
* ![image-20220318141559007](Tree.assets/image-20220318141559007.png)

- https://daimhada.tistory.com/108
