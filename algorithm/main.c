#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
	//int pow1(int, unsigned);
	//int pow1(int, unsigned);
	//int num = atoi(argv[1]);
	//int exp = atoi(argv[2]);	
//	
	//printf("%d\n", pow2(num, exp));
	//printf("%d\n", pow1(num, exp));
	void matrix_exp(int *, int *, int, int);
	int A[16] = {-1, 1, 1, -1, 1, -1, -1, 1, 1, -1, -1, 1, -1, 1, 1, -1};
	int B[16];
	int C[4] = {1, 0, 0, 1};
	int E[9] = {1, 0, 0, 1, 0, 1, 0, 1, 0};
	int D[9];
	int i, j;
	int n = 3;
	matrix_exp(E, D, n, atoi(argv[1]));
	for (i = 0; i < n; i++) {
         for (j = 0; j < n; j++)
              printf("%d\t", *(D + n * i + j));
          printf("\n");
      }

	return 0;
}
