#include <iostream>
using namespace std;

int main(){
  int A, B;
  bool Answer=false;

  cin >> A >> B;

  for (int i=A; i<=B; i++){
    if (100 % i == 0) Answer = true;
  }

  if (Answer) cout << "Yes" << endl;
  else  cout << "No" << endl;
  return 0;
}