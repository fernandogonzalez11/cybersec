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

    vec<int> nums(n), sorted(n);
	loop(i,0,n) cin >> nums[i];

	vec<bool> vis(n, false);
	loop(i,0,n) {
		int sel = -1;
		loop(j,0,n) {
			if (vis[j]) continue;
			if (sel == -1 || nums[j] < nums[sel]) {
				sel = j;
			}

			
		}

		sorted[i] = nums[sel];
		vis[sel] = true;
	}

	loop(i,0,n) cout << sorted[i] << " ";
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
