#include <iostream>
using namespace std;

int main(){
  int N, K, card_3, cnt=0;
  cin >> N >> K;

  for (int i=1; i<=N; i++){
    for (int j=1; j<=N; j++){
      card_3 = K-i-j;
      if (1<=card_3 && card_3<=N) {
        cnt += 1;
      }
    }
  }
  cout << cnt << endl;
  return 0;
}