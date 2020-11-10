import math

maze = []
path = []
closedPath = []
neigbhours = [[1, 1], [0, 1], [1, 0], [1, -1], [0, -1], [-1, 1], [-1, 0], [-1, -1]]


def hurestic(x, n, m):
    dist = math.sqrt((n - 1 - x[0]) * 2 + (m - 1 - x[1]) * 2)
    return dist


def findShortestPath(nextPath, n, m):
    minDistance = 999
    next = []
    for x in nextPath:
        if (hurestic(x, n, m) < minDistance):
            minDistance = hurestic(x, n, m)
            next = x

    return next


def aStar(n, m, dest):
    path.append([0, 0])

    curr = [0, 0]

    while (curr != dest):
        nextPath = []
        for x in neigbhours:
            a = []
            a.append(curr[0] + x[0])
            a.append(curr[1] + x[1])
            if a[0] > -1 and a[0] < n and a[1] > -1 and a[1] < m:
                if (maze[a[0]][a[1]]):
                    if a not in path and a not in closedPath:
                        nextPath.append(a)

        if (nextPath):
            curr = findShortestPath(nextPath, n, m)
            path.append(curr)
        else:
            if path:
                closedPath.append(curr)
                path.pop()
                if path:
                    curr = path[len(path) - 1]
                else:
                    print("No Path available")
                    exit(0)
            else:
                print("No Path available")
                exit(0)


def main():
    n = int(input("Enter number of Rows: "))
    m = int(input("Enter number of Column: "))
    print("Enter the (x, y) of destination")
    dest = list(map(int, input().split()))

    print("\nEnter the maze structure: (0 if blocked,1 if free): ")

    for i in range(n):
        a = []
        a = list(map(int, input().split(" ")))
        maze.append(a)

    print("The Maze is:")
    for i in range(n):
        for j in range(m):
            print(maze[i][j], end=" ")
        print()

    aStar(n, m, dest)

    print("The Path is:")
    for i in range(n):
        for j in range(m):
            if ([i, j] in path):
                print("-", end=" ")
            else:
                print(maze[i][j], end=" ")
        print()

    print()
    print(path)


main()
