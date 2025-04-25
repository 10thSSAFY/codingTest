#include <iostream>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	
	int price;
	cin >> price;
	
	for (int i = 0; i < 9; i++) {
		int n;
		cin >> n;
		price -= n;
	}
	
	cout << price;
	return 0;
}