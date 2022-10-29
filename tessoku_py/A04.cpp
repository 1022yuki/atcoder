#include <iostream>
using namespace std;

int main(){
  int N;
  cin >> N;

  for (int x=9; x>=0; x--){
    int wari = (1<<x); //2**xと同じ
    cout << (N/wari)%2;
  }
  cout << endl;
  return 0;
}