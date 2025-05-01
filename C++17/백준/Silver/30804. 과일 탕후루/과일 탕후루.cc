#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0), cout.tie(0);

    int N;
    cin >> N;

    vector<int> V(N);
    for (int i = 0; i < N; i++) {
        cin >> V[i];
    }

    int left = 0;
    unordered_map<int, int> D;
    int result = 0;

    for (int i = 0; i < N; i++) {
        int f = V[i];

        if (D.find(f) != D.end()) {
            D[f]++;
        }
        else {
            D[f] = 1;
        }

        while (D.size() > 2) {
            int r = V[left];
            D[r]--;

            if (D[r] == 0) {
                D.erase(r);
            }

            left++;
        }

        result = max(result, i - left + 1);
    }

    cout << result << endl;

    return 0;
}
