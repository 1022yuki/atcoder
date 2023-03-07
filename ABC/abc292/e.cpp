#include <iostream>
#include <vector>
using namespace std;

int main() {
  int N, M;
  cin >> N >> M;

  vector<vector<int>> edges(N);
  vector<vector<int>> edges_rev(N);

  vector<int> U(M), V(M);
  for (int i = 0; i < M; i++) {
    cin >> U[i] >> V[i];
    U[i] -= 1;
    V[i] -= 1;
    edges[U[i]].push_back(V[i]);
    edges_rev[V[i]].push_back(U[i]);
  }

  int cnt = 0;
  function<void(int,int)> ap_ed = [&](int s, int e) {
    if (s == e) {
      return;
    }
    if (find(edges[s].begin(), edges[s].end(), e) == edges[s].end()) {
      cnt++;
      edges[s].push_back(e);
      edges_rev[e].push_back(s);
    }
    for (int ne1 : edges[e]) {
      if (find(edges[s].begin(), edges[s].end(), ne1) == edges[s].end()) {
        ap_ed(s, ne1);
      }
    }
    for (int ne2 : edges_rev[s]) {
      if (find(edges[ne2].begin(), edges[ne2].end(), e) == edges[ne2].end()) {
        ap_ed(ne2, e);
      }
    }
  };

  for (int i = 0; i < M; i++) {
    int u = U[i];
    int v = V[i];
    ap_ed(u, v);
  }

  cout << cnt << endl;
  return 0;
}
