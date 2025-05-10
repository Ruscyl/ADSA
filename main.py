def char_to_cost(c):
    if 'A' <= c <= 'Z':
        return ord(c) - ord('A')
    else:
        return ord(c) - ord('a') + 26

def find(parent, x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(parent, x, y):
    xr, yr = find(parent, x), find(parent, y)
    if xr == yr:
        return False
    parent[yr] = xr
    return True

def main():
    import sys
    country_str, build_str, destroy_str = sys.stdin.read().strip().split()

    country = [list(map(int, row)) for row in country_str.split(',')]
    build = [list(row) for row in build_str.split(',')]
    destroy = [list(row) for row in destroy_str.split(',')]

    n = len(country)
    edges = []
    total_destroy_cost = 0

    for i in range(n):
        for j in range(i + 1, n):
            if country[i][j] == 1:
                cost = char_to_cost(destroy[i][j])
                total_destroy_cost += cost
                # if we keep it, we save destroy cost → negative weight
                edges.append((-cost, i, j))
            else:
                cost = char_to_cost(build[i][j])
                edges.append((cost, i, j))

    edges.sort()
    parent = list(range(n))
    mst_cost = 0

    for cost, u, v in edges:
        if union(parent, u, v):
            mst_cost += cost

    print(total_destroy_cost + mst_cost)

if __name__ == "__main__":
    main()
