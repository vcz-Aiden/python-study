#include<cstdio>

using namespace std;
int result[10001] = {0,};

int main() {
	int num, temp;
	scanf("%d", &num);
	
	for (int i = 0; i < num; i++) {
		scanf("%d", &temp);
		result[temp] += 1;
	}
	
	for (int i = 0; i < 10001; i++) {
		for (int j = 0; j < result[i]; j++) {
			printf("%d\n", i);
		}
	}
}
