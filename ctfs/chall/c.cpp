#include <bits/stdc++.h>

// macros
typedef long long int ll;
#define vec vector 
#define loop(i, a, b) for (int i = a; i < b; i++)
#define F first
#define S second
// constants
#define INF (1LL << 62)
#define int long long
#define printarr(a) cout << #a << ": "; \
	 	    for (auto x : a) cout << x << " "; \
		    cout << "\n";

using namespace std;

void solve() {
    string s;
	cin >> s;

	loop(i,0,s.size()) {
		if (s[i] >= 'A' && s[i] <= 'Z') 
			s[i] = s[i] - 'A' + 'a';
	}

	bool lets[26];
	loop(i,0,26) lets[i] = false;

	for (char c : s) lets[c - 'a'] = true;

	cout << (lets['a' - 'a'] + lets['e' - 'a'] + lets['i' - 'a'] + lets['o' - 'a'] +lets['u' - 'a']) << "\n";
}

signed main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	
	int t = 1;
	// cin >> t;
	while (t--) solve();

	return 0;
}
