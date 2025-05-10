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
        xroot = self.find(x)
        yroot = self.find(y)
        if xroot == yroot:
            return False
        self.parent[xroot] = yroot
        return True

def main():
    country_str, build_str, destroy_str = input().strip().split()
    country = country_str.split(',')
    build = build_str.split(',')
    destroy = destroy_str.split(',')
    n = len(country)

    dsu = DSU(n)
    total_cost = 0
    build_edges = []

    for i in range(n):
        for j in range(i + 1, n):
            if country[i][j] == '1':
                if not dsu.union(i, j): 
                    total_cost += letter_to_cost(destroy[i][j])
            else:
                build_cost = letter_to_cost(build[i][j])
                build_edges.append((build_cost, i, j))

    build_edges.sort()
    for cost, u, v in build_edges:
        if dsu.union(u, v):
            total_cost += cost

    print(total_cost)

if __name__ == "__main__":
    main()
