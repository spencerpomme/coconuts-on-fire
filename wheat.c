/* wheat.c -- exponential growth */
#include <stdio.h>
#define SQUARES 64 /* �����ϵķ�����Ŀ */ 
#define CROP 1e15  /* �����Ƶ�����С��������� */

int main(void)
{
	double current, total;
	int count = 1;
	
	printf("%4s %18s %16s %14s\n", "square", "grains added", "total grains", "fraction of");
	total = current = 1.0;
	printf("%6d %16.2e %16.2e %16.2e\n", count, current, total, total/CROP);
	while (count < SQUARES)
	{
		count = count + 1;
		current = 2.0 * current;
		total = total + current;
		printf("%6d %16.2e %16.2e %16.2e\n", count, current, total, total/CROP);
	}
	printf("That's all.\n");
	return 0;
 } 

