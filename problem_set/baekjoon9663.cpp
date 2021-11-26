#include <iostream>
#include <cmath>

using namespace std;

int board[14];
int n;
int cnt;

void path(int y) {
	// y�� ���� ��� ���� ��ġ�Ǿ������� �ǹ��ϴ� ������.
	int ko;
	if( y == n ) {
		// n���� ���� ��ġ�� �Ǿ��ٸ� �� ���� ���̴�.
		cnt++;
		return;
	}
	for( int i=0; i<n; i++ ) {
		// ko�� ���� ��ġ�� �� �ִ����� �����ϴ� �÷��״�.
		ko = 1;
		for( int j=0; j<y; j++ ) {
			// �̹� ��ġ�� ���� ���� �����ؼ� i��° ĭ�� ���� ��ġ�� �� �ִ����� Ȯ���Ѵ�.
			if( board[j] == i || abs(y-j) == abs(i-board[j]) ) {
				// j��° �ٿ� �ִ� ���� ���� ĭ�� �ְų�, �밢���� ���� ���� �ִٸ�, i��° ĭ�� ���� Ž���� �ߴ��Ѵ�.
				ko = 0;
				break;
			}
		}
		if( ko ) {
			// ������� �Դٸ� y��° �ٿ� i��° ĭ�� ���� ���δ� ���� �����ϴ�.
			board[y] = i;
			path(y+1);
		}
	}
}

int main() {
	cin >> n;
	cnt = 0;
	path(0);
	cout << cnt;

	return 0;
}
