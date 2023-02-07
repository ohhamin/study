def draw():
    for i in range(len(sharks)):
        if sharks[i][0]:
            if array[sharks[i][1]][sharks[i][2]] != -1:
                if sharks[array[sharks[i][1]][sharks[i][2]]][5] <= sharks[i][5]:
                    sharks[array[sharks[i][1]][sharks[i][2]]][0] = False
                    array[sharks[i][1]][sharks[i][2]] = i
                else:
                    sharks[i][0] = False
            else:
                array[sharks[i][1]][sharks[i][2]] = i

def catch(x):
    global result
    for i in range(1, r+1):
        if array[i][x] != -1:
            sharks[array[i][x]][0] = False
            result += sharks[array[i][x]][5]
            break

def move():
    for i in range(len(sharks)):
        if sharks[i][0]:
            if sharks[i][4] == 1 or sharks[i][4] == 2:
                s = sharks[i][3] % ((r - 1) * 2)
            else:
                s = sharks[i][3] % ((c - 1) * 2)
            for _ in range(s):
                n_x = sharks[i][1] + direction[sharks[i][4]][0]
                n_y = sharks[i][2] + direction[sharks[i][4]][1]
                if n_x == 0:
                    sharks[i][4] = 2
                    n_x = 2
                elif n_x == r + 1:
                    sharks[i][4] = 1
                    n_x = r - 1
                elif n_y == 0:
                    sharks[i][4] = 3
                    n_y = 2
                elif n_y == c + 1:
                    sharks[i][4] = 4
                    n_y = c - 1
                sharks[i][1] = n_x
                sharks[i][2] = n_y

r, c, m = map(int, input().split())
sharks = []
direction = [[0, 0], [-1, 0], [1, 0], [0, 1], [0, -1]]
for _ in range(m):
    sharks.append([True] + list(map(int, input().split())))

result = 0
for fisher in range(1, c + 1):
    array = [[-1] * (c + 1) for _ in range(r + 1)]
    draw()
    catch(fisher)
    move()
print(result)