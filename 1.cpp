#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;  
    while(t--) {
        int n, k;
        cin >> n >> k;
        string s;
        cin >> s;

        string rev_s = s;
        reverse(rev_s.begin(), rev_s.end());

        if(s < rev_s) {
            cout << "YES\n";
            continue;
        }

        if(s == rev_s) {
            bool allSame = true;
            for(int i = 1; i < n; i++) {
                if(s[i] != s[0]) {
                    allSame = false;
                    break;
                }
            }
            if(allSame) {
                cout << "NO\n";
            } else {
                if(k > 0) cout << "YES\n";
                else      cout << "NO\n";
            }
            continue;
        }

        if(k > 0) {
            cout << "YES\n";
        } else {
            cout << "NO\n";
        }
    }

    return 0;
}
