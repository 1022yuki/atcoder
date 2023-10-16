#include <iostream>
#include <vector>
#include <set>
#include <string>
#include <deque>
using namespace std;

int main() {
    int N;
    string Tp;
    cin >> N >> Tp;

    vector<string> S(N);
    for (int i = 0; i < N; i++) {
        cin >> S[i];
    }

    set<string> setT;
    int ltp = Tp.length();

    // Tp[:x]とTp[x:]を計算
    vector<string> Tptox(ltp + 1);
    vector<string> Tpfromx(ltp + 1);
    deque<char> top, bottom(Tp.begin(), Tp.end());
    
    for (int i = 0; i <= ltp; i++) {
        Tptox[i] = string(top.begin(), top.end());
        Tpfromx[i] = string(bottom.begin(), bottom.end());
        if (i != ltp) {
            top.push_back(Tp[i]);
            bottom.pop_front();
        }
    }

    // Tpから1文字削除したものをsetTに追加
    for (int i = 0; i < ltp; i++) {
        setT.insert(Tptox[i] + Tpfromx[i + 1]);
    }

    // Tpの1箇所にある英小文字1文字を追加したものをsetTに追加
    for (int i = 0; i <= ltp; i++) {
        for (char j = 'a'; j <= 'z'; j++) {
            setT.insert(Tptox[i] + j + Tpfromx[i]);
        }
    }

    // Tpの1箇所をある英小文字1文字に変更したものをsetTに追加
    for (int i = 0; i < ltp; i++) {
        for (char j = 'a'; j <= 'z'; j++) {
            setT.insert(Tptox[i] + j + Tpfromx[i + 1]);
        }
    }

    vector<int> ans;
    for (int i = 0; i < N; i++) {
        if (setT.find(S[i]) != setT.end()) {
            ans.push_back(i + 1);
        }
    }

    cout << ans.size() << endl;
    for (int i = 0; i < ans.size(); i++) {
        cout << ans[i] << " ";
    }
    cout << endl;

    return 0;
}
