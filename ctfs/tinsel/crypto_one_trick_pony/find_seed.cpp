#include <bits/stdc++.h>
#include <boost/multiprecision/cpp_int.hpp>

using namespace std;
using boost::multiprecision::cpp_int;
using u128 = __uint128_t;
using u64 = uint64_t;

static const int X_BITS = 500;

/////////////////////////////
static const u64 p_rng = 11465860909ULL;
static const cpp_int X_TARGET(
    "1821220944764715655231246124577895384774548096775611482136074557991461107008224881116341006411437064082513412888291565045318367830748002399825157105220"
);
/////////////////////////////

inline u64 norm(u64 z) {
    z %= p_rng;
    return z == 0 ? 1 : z;
}

u64 mult(u64 a, u64 b, u64 mod) {
    return (u128)a * b % mod;
}

u64 binexp(u64 base, u64 exp, u64 mod) {
    u64 res = 1;
    while (exp) {
        if (exp & 1) res = mult(res, base, mod);
        base = mult(base, base, mod);
        exp >>= 1;
    }
    return res;
}

inline int legendre_bit(u64 z) {
    z = norm(z);
    return binexp(z, (p_rng - 1) / 2, p_rng) == 1;
}

int main() {
    //ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cout << "p: " << p_rng << "\n";
    cout << "x: " << X_TARGET.str() << "\n";

    int PARTITIONS, WORKER_ID;
    
    cout << "partitions: ";
    cin >> PARTITIONS;

    cout << "worker id: ";
    cin >> WORKER_ID;

    u64 chunk = p_rng / PARTITIONS;
    u64 RAW_START = chunk * (WORKER_ID - 1);
    u64 RAW_STOP  = chunk * WORKER_ID;

    u64 START = (RAW_START > X_BITS) ? RAW_START - X_BITS : 0;
    u64 STOP = std::min<u64>(p_rng, RAW_STOP + u64(2) * X_BITS);

    cout << "searching seeds in [" << START << ", " << STOP << ")\n";

    cpp_int MASK = (cpp_int(1) << X_BITS) - 1;
    cpp_int cur = 0;

    // build
    for (u64 i = 0; i < X_BITS; i++) {
        cur <<= 1;
        cur |= legendre_bit(START + i);
    }

    // slide
    for (u64 s = START; s + X_BITS < STOP; s++) {
        if (s % 10000000 == 0)
            cout << s << '\n';

        if (cur == X_TARGET) {
            u64 nxt = norm(s + X_BITS);

            cout << "BIG WIN\n";
            cout << "prime: " << p_rng << '\n';
            cout << "original seed: " << (long long)(nxt - X_BITS) << '\n';
            cout << "next seed value: " << nxt << '\n';

            return 0;
        }

        cur = ((cur << 1) & MASK) | legendre_bit(s + X_BITS);
    }

    cout << "[-] seed not found\n";
    return 0;
}
