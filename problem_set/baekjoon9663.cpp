#include <iostream>
#include <cmath>

using namespace std;

int board[14];
int n;
int cnt;

void path(int y) {
	// y는 현재 몇개의 퀸이 배치되었는지를 의미하는 변수다.
	int ko;
	if( y == n ) {
		// n개의 퀸이 배치가 되었다면 이 경우는 답이다.
		cnt++;
		return;
	}
	for( int i=0; i<n; i++ ) {
		// ko는 퀸이 배치될 수 있는지를 저장하는 플래그다.
		ko = 1;
		for( int j=0; j<y; j++ ) {
			// 이미 배치가 끝난 퀸을 참고해서 i번째 칸에 퀸을 설치할 수 있는지를 확인한다.
			if( board[j] == i || abs(y-j) == abs(i-board[j]) ) {
				// j번째 줄에 있는 퀸과 같은 칸에 있거나, 대각선에 같은 곳에 있다면, i번째 칸에 대한 탐색을 중단한다.
				ko = 0;
				break;
			}
		}
		if( ko ) {
			// 여기까지 왔다면 y번째 줄에 i번째 칸에 퀸을 놔두는 것이 가능하다.
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
