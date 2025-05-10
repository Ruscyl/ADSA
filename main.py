def letter_to_cost(ch):
    if 'A' <= ch <= 'Z':
        return ord(ch) - ord('A')
    else:
        return ord(ch) - ord('a') + 26

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xroot, yroot = self.find(x), self.find(y)
        if xroot != yroot:
            self.parent[xroot] = yroot
            return True
        return False

def main():
    import sys
    country_str, build_str, destroy_str = input().strip().split()
    country = country_str.split(',')
    build = build_str.split(',')
    destroy = destroy_str.split(',')
    n = len(country)

    dsu = DSU(n)
    edges = []

    for i in range(n):
        for j in range(i + 1, n):
            if country[i][j] == '1':
                cost = letter_to_cost(destroy[i][j])
                edges.append((0, i, j, 'keep', cost))  

    for i in range(n):
        for j in range(i + 1, n):
            if country[i][j] == '0':
                cost = letter_to_cost(build[i][j])
                edges.append((cost, i, j, 'build'))

    edges.sort()

    used_edges = set()
    total_cost = 0

    for edge in edges:
        if len(edge) == 5:
            cost, u, v, typ, destroy_cost = edge
        else:
            cost, u, v, typ = edge
            destroy_cost = None

        if dsu.union(u, v):
            if typ == 'build':
                total_cost += cost
            elif typ == 'keep':
                used_edges.add((u, v))

    for i in range(n):
        for j in range(i + 1, n):
            if country[i][j] == '1' and (i, j) not in used_edges:
                total_cost += letter_to_cost(destroy[i][j])

    print(total_cost)

if __name__ == "__main__":
    main()
