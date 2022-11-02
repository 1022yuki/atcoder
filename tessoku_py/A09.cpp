#include <iostream>
using namespace std;

int H, W, N;
int A[100009], B[100009], C[100009], D[100009];
int grid[1509][1509], sum_grid[1509][1509];

int main(){

  // 入力
  cin >> H >> W >> N;
  for (int i=1; i<=N; i++) cin >> A[i] >> B[i] >> C[i] >> D[i];

  // 配列の初期化
  for (int i=0; i<=H; i++){
    for (int j=0; j<=W; j++){
      grid[i][j] = 0;
      sum_grid[i][j] = 0;
    }
  }

  // 前処理
  for (int i=1; i<=N; i++){
    grid[A[i]][B[i]] += 1;
    grid[A[i]][D[i]+1] -= 1;
    grid[C[i]+1][B[i]] -= 1;
    grid[C[i]+1][D[i]+1] += 1;
  }

  // 累積和
  for (int i=1; i<=H; i++){
    for (int j=1; j<=W; j++){
      sum_grid[i][j] = sum_grid[i][j-1] + grid[i][j];
    }
  }
  for (int j=1; j<=W; j++){
    for (int i=1; i<=H; i++){
      sum_grid[i][j] = sum_grid[i-1][j] + sum_grid[i][j];
    }
  }

  // 出力
  for (int i=1; i<=H; i++){
    for (int j=1; j<=W; j++){
      if (j>=2) cout << " ";
      cout << sum_grid[i][j];
    }
    cout << endl;
  }
  return 0;
}