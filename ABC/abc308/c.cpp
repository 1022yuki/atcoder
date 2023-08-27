#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<double> A(N);
    vector<double> B(N);
    for(int i = 0; i < N; i++) {
        cin >> A[i] >> B[i];
    }

    vector<pair<double, int>> li(N);
    for(int i = 0; i < N; i++) {
        double suc = A[i] / (A[i] + B[i]);
        li[i] = make_pair(-suc, i + 1);
    }

    sort(li.begin(), li.end());

    for(int i = 0; i < N; i++) {
        cout << li[i].second;
        if(i != N - 1) {
            cout << " ";
        }
    }
    cout << "\n";
    return 0;
}
