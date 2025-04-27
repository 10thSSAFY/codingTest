#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

const long long INF = 999999999;;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0), cout.tie(0);

    int N;
    cin >> N;

    vector<int> A(N);
    for (int i = 0; i < N; i++)
        cin >> A[i];

    vector<long long> dp(N, INF);
    dp[0] = 0;

    for (int i = 1; i < N; i++) {
        for (int j = 0; j < i; j++) {
            long long power = max(dp[j], (long long)(i - j) * (1 + abs(A[i] - A[j])));
            dp[i] = min(dp[i], power);
        }
    }

    cout << dp[N - 1] << endl;

    return 0;
}
