#include <iostream>
using namespace std;

int N, A[100009], S[100009];
int Q, L[100009], R[100009];
int atari, hazure;

int main(){
  cin >> N;
  for (int i=1; i<=N; i++) cin >> A[i];
  cin >> Q;
  for (int i=1; i<=Q; i++) cin >> L[i] >> R[i];

  S[0] = 0;
  for (int i=1; i<=N; i++) S[i] = S[i-1] + A[i];

  for (int i=1; i<=Q; i++) {
    atari = S[R[i]] - S[L[i]-1];
    hazure = R[i]-L[i]+1-atari;
    if (atari>hazure) {
      cout << "win" << endl;
    } else if (atari==hazure) {
      cout << "draw" << endl;
    } else {
      cout << "lose" << endl;
    }
    
  }
  return 0;
}