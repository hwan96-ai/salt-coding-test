def solution(maps):
    h = len(maps)
    w = len(maps[0])
    visited = [[False] * w for _ in range(h)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    queue = [(0, 0, 1)]
    visited[0][0] = True

    while len(queue) > 0:
        x, y, distance = queue.pop(0)

        if x == h - 1 and y == w - 1:
            return distance

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < h and 0 <= ny < w and maps[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, distance + 1))

    return -1