def letter_to_cost(c):
    return ord(c) - ord('A') if 'A' <= c <= 'Z' else ord(c) - ord('a') + 26

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
    country_str, build_str, destroy_str = input().strip().split()
    country = country_str.split(',')
    build = build_str.split(',')
    destroy = destroy_str.split(',')
    n = len(country)

    edges = [] 
    used_existing_edges = set()

    for i in range(n):
        for j in range(i + 1, n):
            if country[i][j] == '1':
                edges.append((0, i, j, 'existing'))
            else:
                cost = letter_to_cost(build[i][j])
                edges.append((cost, i, j, 'new'))

    edges.sort()
    dsu = DSU(n)
    total_cost = 0

    for cost, u, v, typ in edges:
        if dsu.union(u, v):
            if typ == 'new':
                total_cost += cost
            else:
                used_existing_edges.add((u, v))

    for i in range(n):
        for j in range(i + 1, n):
            if country[i][j] == '1' and (i, j) not in used_existing_edges:
                total_cost += letter_to_cost(destroy[i][j])

    print(total_cost)

if __name__ == "__main__":
    main()
