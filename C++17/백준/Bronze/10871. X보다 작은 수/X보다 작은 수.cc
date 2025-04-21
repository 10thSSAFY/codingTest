#include <iostream>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    int X;
    cin >> N >> X;

    int val;
    for (int i = 0; i < N; i++) {
        cin >> val;
        if (val < X) {
            cout << val << " ";
        }
    }

    return 0;
}
