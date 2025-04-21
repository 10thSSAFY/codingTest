#include <iostream>
using namespace std;

int main() {
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
