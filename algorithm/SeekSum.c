#include <stdio.h>
//An algorithm that, given a set S of n integers and another integer x,
//determines whether or not there exist two elements in S whose sum is
//exactly x. The set S must be already sorted

//BinSearch(A, first, end, x)
//	while length >= 0
//		inter = (first + end) / 2
//		if x == A[inter]
//			return inter + 1
//		else if x < A[inter]
//			end = inter - 1
//		else
//			first = inter + 1
//		length = end - first
//	return -1
	
int BinSearch(int A[], int first, int end, int x) {
	int length = end - first;
	int inter;
	
	while (length >= 0) {
		inter = (first + end) / 2;
		if (x == A[inter] )
			return inter + 1;
		else if (x < A[inter])
			end = inter - 1;
		else
			first = inter + 1;
		length = end - first;	
	}
	return -1;
}

void SeekSum(int A[], int first, int end, int x) {
	int i;
	int pos;
	
	for (i = first; i < end; i++) 
		if ((pos = BinSearch(A, i + 1, end, x - A[i])) != -1) {
			printf("first = %d,end = %d\n",i + 1, pos);
			break;
		}
}			
			 

void main() {
	int A[10] = {10,2,3,4,15,6,70,7,8,8};
	
	SeekSum(A, 0, 9, 15);
//  printf("%d\n", BinSearch(A, 4,4, 5));
}	
