#include <iostream>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

int main() {
  int H, W, rs, cs, N, Q;
  cin >> H >> W >> rs >> cs >> N;
  rs--;
  cs--;

  map<int, vector<int>> R;
  map<int, vector<int>> C;
  for (int i = 0; i < N; i++) {
    int r, c;
    cin >> r >> c;
    r--;
    c--;
    R[r].push_back(c);
    C[c].push_back(r);
  }

  for (auto& row : R) {
    row.second.push_back(-1);
    row.second.push_back(W);
    sort(row.second.begin(), row.second.end());
  }

  for (auto& col : C) {
    col.second.push_back(-1);
    col.second.push_back(H);
    sort(col.second.begin(), col.second.end());
  }

  cin >> Q;
  for (int i = 0; i < Q; i++) {
    char dir;
    int l;
    cin >> dir >> l;

    if (dir == 'L') {
      auto& col = R[rs];
      auto it_be = lower_bound(col.begin(), col.end(), cs);
      auto it_af = lower_bound(col.begin(), col.end(), cs - l);
      if (it_be == it_af) {
        cs -= l;
      } else {
        cs = *(it_be - 1) + 1;
      }
    }

    if (dir == 'R') {
      auto& col = R[rs];
      auto it_be = upper_bound(col.begin(), col.end(), cs);
      auto it_af = upper_bound(col.begin(), col.end(), cs + l);
      if (it_be == it_af) {
        cs += l;
      } else {
        cs = *(it_be) - 1;
      }
    }

    if (dir == 'U') {
      auto& row = C[cs];
      auto it_be = lower_bound(row.begin(), row.end(), rs);
      auto it_af = lower_bound(row.begin(), row.end(), rs - l);
      if (it_be == it_af) {
        rs -= l;
      } else {
        rs = *(it_be - 1) + 1;
      }
    }

    if (dir == 'D') {
      auto& row = C[cs];
      auto it_be = upper_bound(row.begin(), row.end(), rs);
      auto it_af = upper_bound(row.begin(), row.end(), rs + l);
      if (it_be == it_af) {
        rs += l;
      } else {
        rs = *(it_be) - 1;
      }
    }

    cout << rs + 1 << " " << cs + 1 << endl;
  }

  return 0;
}
