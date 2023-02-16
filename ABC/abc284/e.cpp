#include <bits/stdc++.h>
using namespace std;
// #define rep(i,n) for (int i=0; i<(n); i++);
using ll = long long;

int N, M;
int u, v;
int i;
vector<int> G[1000009];
bool visited[1000009];
int cnt = 0;

int dfs(int pos) {
  visited[pos] = true;
  cnt++;
  if (cnt == 1e6) {
    cout << cnt << endl;
    exit(0);
  }
  for(int i=0; i<G[pos].size(); i++){
    int nex = G[pos][i];
    if (visited[nex] == false) dfs(nex);
  }
  visited[pos] = false;
  return cnt;
}

int main(){
  cin >> N >> M;
  for (int i=0; i<M; i++){
    cin >> u >> v;
    u--;
    v--;
    G[u].push_back(v);
    G[v].push_back(u);
  }
  for(int i=0; i<N; i++) visited[i] = false;
  dfs(0);
  cout << cnt << endl;
  return 0;
}