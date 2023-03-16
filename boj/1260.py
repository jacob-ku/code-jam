from collections import deque


def bfs(graph, start, visited):
    wait_queue = deque([start])
    visited[start] = True
    result = []

    while wait_queue:
        current = wait_queue.popleft()
        result.append(current)
        temp = list()
        for a, b in graph:
            if a == current and visited[b] is False:
                temp.append(b)
                visited[b] = True
            elif b == current and visited[a] is False:
                temp.append(a)
                visited[a] = True
        temp.sort()
        wait_queue.extend(temp)

    return result


def dfs(graph, start, visited):
    wait_stack = deque([start])
    result = []

    while wait_stack:
        current = wait_stack.pop()
        if visited[current] is True:
            continue
        result.append(current)
        visited[current] = True

        temp = list()
        for a, b in graph:
            if a == current and visited[b] is False:
                temp.append(b)
            elif b == current and visited[a] is False:
                temp.append(a)
        temp.sort(reverse=True)
        wait_stack.extend(temp)
    return result


def solve():
    N, M, V = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(M)]
    print(*dfs(graph, V, [False]*(N + 1)), sep=' ')
    print(*bfs(graph, V, [False]*(N + 1)), sep=' ')


if __name__ == '__main__':
    solve()
