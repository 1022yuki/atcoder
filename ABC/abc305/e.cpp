#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int main() {
    int N, M, K;
    cin >> N >> M >> K;

    vector<vector<int>> edges(N);
    for (int i = 0; i < N; i++) {
        edges[i] = vector<int>();
    }

    for (int i = 0; i < M; i++) {
        int a, b;
        cin >> a >> b;
        a -= 1;
        b -= 1;
        edges[a].push_back(b);
        edges[b].push_back(a);
    }

    priority_queue<pair<int, int>> Q;
    vector<bool> done(N, false);

    vector<pair<int, int>> keibi;
    vector<int> ver_keibi(N, -1);
    for (int i = 0; i < K; i++) {
        int p, h;
        cin >> p >> h;
        Q.push(make_pair(-h, p - 1));
        keibi.push_back(make_pair(-h, p - 1));
        ver_keibi[p - 1] = h;
    }

    vector<int> ans;
    int cnt = 0;

    while (!Q.empty()) {
        if (Q.top().first == 0) {
            break;
        }

        int h = -Q.top().first;
        int n = Q.top().second;
        Q.pop();

        if (done[n]) {
            continue;
        }

        for (int j : edges[n]) {
            if (ver_keibi[j] < h - 1) {
                Q.push(make_pair(-(h - 1), j));
                ver_keibi[j] = h - 1;
            }
        }
    }

    for (int i = 0; i < N; i++) {
        if (ver_keibi[i] != -1) {
            ans.push_back(i + 1);
            cnt += 1;
        }
    }

    cout << cnt << endl;
    for (int a : ans) {
        cout << a << " ";
    }
    cout << endl;

    return 0;
}
