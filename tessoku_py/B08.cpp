#include <iostream>
using namespace std;

int N, X, Y, grid[1509][1509], sum_grid[1509][1509];
int Q, a, b, c, d;
int ans;

int main(){
  cin >> N;

  // 配列初期化
  for (int i=0; i<=1500; i++) {
    for (int j=0; j<=1500; j++) {
      grid[i][j] = 0;
      sum_grid[i][j] = 0;
    }
  }

  // 座標ごとに点の数を集計
  for (int i=1; i<=N; i++) {
    cin >> X >> Y;
    grid[X][Y] += 1;
  }

  // 二次元累積和作成
  for (int i=1; i<=1500; i++) {
    for (int j=1; j<=1500; j++) {
      sum_grid[i][j] = sum_grid[i][j-1] + grid[i][j];
    }
  }
  for (int j=1; j<=1500; j++) {
    for (int i=1; i<=1500; i++) {
      sum_grid[i][j] = sum_grid[i-1][j] + sum_grid[i][j];
    }
  }

  cin >> Q;
  for (int i=1; i<=Q; i++) {
    cin >> a >> b >> c >> d;
    ans = sum_grid[c][d]-sum_grid[c][b-1]-sum_grid[a-1][d]+sum_grid[a-1][b-1];
    cout << ans << endl;
  }

  return 0;
}