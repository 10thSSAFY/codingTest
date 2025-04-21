#include <iostream>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int a, b, c;
    cin >> a >> b >> c;

    int res = a * b * c;
    int count[10] = {};

    while (res != 0) {
        count[res % 10]++;
        res /= 10;
    }

    for (int v : count) {
        cout << v << "\n";
    }

    return 0;
}
