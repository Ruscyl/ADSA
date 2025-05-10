def letter_to_cost(ch):
    return ord(ch) - ord('A') if 'A' <= ch <= 'Z' else ord(ch) - ord('a') + 26

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr != yr:
            self.parent[xr] = yr
            return True
        return False

def main():
    import sys
    country_str, build_str, destroy_str = input().strip().split()
    country = country_str.split(',')
    build = build_str.split(',')
    destroy = destroy_str.split(',')
    n = len(country)

    edges = []
    destroy_total = 0

    for i in range(n):
        for j in range(i + 1, n):
            if country[i][j] == '1':
                cost = letter_to_cost(destroy[i][j])
                destroy_total += cost
                edges.append((-cost, i, j))
            else:
                cost = letter_to_cost(build[i][j])
                edges.append((cost, i, j))

    edges.sort()
    dsu = DSU(n)
    savings = 0

    for cost, u, v in edges:
        if dsu.union(u, v):
            savings += -cost if cost < 0 else -cost 

    print(destroy_total + savings)

if __name__ == "__main__":
    main()
