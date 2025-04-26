#include <iostream>
#include <string>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL), cout.tie(NULL);
    
    int T;
    cin >> T;
    
    for (int i = 0; i < T; i++) {
        string S;
        cin >> S;
        int curr = 0, score = 0;
        
        for (int j = 0; j < S.length(); j++) {
            if (S[j] == 'O') {
                curr++;
                score += curr;
            } else {
                curr = 0;
            }
        }
        
        cout << score << endl;
    }
    
    return 0;
}