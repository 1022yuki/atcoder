#include <iostream>
using namespace std;

int main(){
  string N;
  cin >> N;
  int answer = 0;

  for (int i=0; i < N.size(); i++) {
    int kurai = 1<<i;
    if (N[N.size()-1-i] == '1') {
      answer += kurai;
    }
  }

  cout << answer << endl; 
  return 0;
}