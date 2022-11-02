#include <iostream>
using namespace std;

double f(double x) {
  return x*x*x+x;
}

int main(){
  int N;
  cin >> N;

  // 二分探索
  double left=0, right=100, mid;
  for (int i=0; i<20; i++) {
    mid = (left+right)/2;
    double val = f(mid);

    if (val<N) left = mid;
    else right = mid;
  }

  printf("%.12lf\n", mid);
  return 0;
}