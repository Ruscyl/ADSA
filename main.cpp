#include <iostream>
#include <vector>
#include <string>
#include <tuple>
#include <algorithm>
using namespace std;

int letter_to_cost(char c) {
    return (c >= 'A' && c <= 'Z') ? (c - 'A') : (c - 'a' + 26);
}

struct DSU {
    vector<int> parent;
    DSU(int n) {
        parent.resize(n);
        for (int i = 0; i < n; ++i) parent[i] = i;
    }
    int find(int x) {
        if (parent[x] != x) parent[x] = find(parent[x]);
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

    vector<tuple<int, int, int, bool, int>> edges;

    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            if (country[i][j] == '1') {
                edges.emplace_back(0, i, j, false, letter_to_cost(destroy[i][j]));
            } else {
                edges.emplace_back(letter_to_cost(build[i][j]), i, j, true, 0);
            }
        }
    }

    sort(edges.begin(), edges.end());

    DSU dsu(n);
    int total_cost = 0;

    for (auto& e : edges) {
        int cost, u, v, destroy_cost;
        bool is_build;
        tie(cost, u, v, is_build, destroy_cost) = e;

        if (dsu.unite(u, v)) {
            total_cost += cost;
        } else {
            if (!is_build) {
                total_cost += destroy_cost;
            }
        }
    }

    cout << total_cost << endl;
    return 0;
}
