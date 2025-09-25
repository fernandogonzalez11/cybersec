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

vec<int> fact_amt(int n) {
	vec<int> uniq;
	for (int i = 2; i * i <= n; i++) {
		if (n % i == 0) {
			uniq.push_back(i);
			while (n % i == 0) n /= i;
		}
	}

	if (n > 1) uniq.push_back(n);
	return uniq;
}

void solve() {
    int n;
	cin >> n;

	vec<int> v = fact_amt(n);
	loop(i,0,v.size()) cout << v[i] << " ";
	cout << "\n"; 
}

signed main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	
	int t = 1;
	// cin >> t;
	while (t--) solve();

	return 0;
}
