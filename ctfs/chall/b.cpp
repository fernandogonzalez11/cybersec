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
    int n;
	cin >> n;

	int amt = 0;

	for (int k = 1; k*(k+1) < 2*n; k++) {
		int n1 = 2*n - k*(k+1);
		int n2 = 2*(k+1);

		// if (n1 % n2 == 0) cout << "caught:" << k << " " << n1/n2 << "\n";

		amt += (n1 % n2 == 0);
	}

	cout << amt << "\n";
}

signed main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	
	int t = 1;
	// cin >> t;
	while (t--) solve();

	return 0;
}
