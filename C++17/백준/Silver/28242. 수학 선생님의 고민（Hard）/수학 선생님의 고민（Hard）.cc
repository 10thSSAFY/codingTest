#include <iostream>
#include <map>
#include <cmath>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL), cout.tie(NULL);
    
    int N;
    cin >> N;
    
    map<int, int> m1;
    map<int, int> m2;
    int a, b, c, d;
    bool flag = false;
    
    for (int i = 1; i <= sqrt(N); i++) {
        if (N % i == 0) {
            m1.insert({ i, N / i });
        }
    }
    
    for (int i = 1; i <= sqrt(N + 2); i++) {
        if ((N + 2) % i == 0) {
            m2.insert({ i, (N + 2) / i });
        }
    }
    
    for (map<int, int>::iterator iter1 = m1.begin(); iter1 != m1.end(); iter1++) {
        for (map<int, int>::iterator iter2 = m2.begin(); iter2 != m2.end() && flag == false; iter2++) {
            a = iter1->first;
            c = iter1->second;
            b = iter2->first;
            d = iter2->second;
            if (a * d - b * c == N + 1) {
                cout << a << " " << -b << " " << c << " " << d << "\n";
                flag = true;
                break;
            }
            else if (b * c - a * d == N + 1) {
                cout << a << " " << b << " " << c << " " << -d << "\n";
                flag = true;
                break;
            }
        }
    }
    if (flag == false) {
        cout << -1 << "\n";
    }
    
    return 0;
}