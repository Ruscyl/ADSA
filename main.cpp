#include <iostream>
#include <vector>
#include <string>
#include <tuple>
#include <algorithm>
using namespace std;

// Convert letter to cost
int letter_to_cost(char c) {
    return (c >= 'A' && c <= 'Z') ? (c - 'A') : (c - 'a' + 26);
}

// Disjoint Set Union
struct DSU {
    vector<int> parent;
    DSU(int n) {
        parent.resize(n);
        for (int i = 0; i < n; ++i)
            parent[i] = i;
    }
    int find(int x) {
        if (parent[x] != x)
            parent[x] = find(parent[x]);
        return parent[x];
    }
    bool unite(int x, int y) {
        int xr = find(x), yr = find(y);
        if (xr == yr) return false;
        parent[xr] = yr;
        return true;
    }
};

int main() {
    string country_input, build_input, destroy_input;
    cin >> country_input >> build_input >> destroy_input;

    vector<string> country, build, destroy;
    int n = 1;
    for (char c : country_input)
        if (c == ',') ++n;

    country.resize(n);
    build.resize(n);
    destroy.resize(n);

    int idx = 0;
    for (char c : country_input) {
        if (c == ',') ++idx;
        else country[idx] += c;
    }
    idx = 0;
    for (char c : build_input) {
        if (c == ',') ++idx;
        else build[idx] += c;
    }
    idx = 0;
    for (char c : destroy_input) {
        if (c == ',') ++idx;
        else destroy[idx] += c;
    }

    vector<tuple<int, int, int, string, char>> edges;

    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            if (country[i][j] == '1') {
                // Two choices: keep (0 cost) or destroy (destruction cost)
                edges.emplace_back(0, i, j, "keep", destroy[i][j]);
                edges.emplace_back(letter_to_cost(destroy[i][j]), i, j, "destroy", '-');
            } else {
                // Only one choice: build it
                edges.emplace_back(letter_to_cost(build[i][j]), i, j, "build", '-');
            }
        }
    }

    // Sort all edges by cost ascending
    sort(edges.begin(), edges.end());

    DSU dsu(n);
    int total_cost = 0;

    for (auto& edge : edges) {
        int cost, u, v;
        string type;
        char dummy;
        tie(cost, u, v, type, dummy) = edge;

        if (type == "keep" || type == "build") {
            if (dsu.unite(u, v)) {
                total_cost += cost;
            }
        } else if (type == "destroy") {
            if (dsu.find(u) == dsu.find(v)) {
                // Already connected, so we must destroy it
                total_cost += cost;
            }
        }
    }

    cout << total_cost << endl;
    return 0;
}
