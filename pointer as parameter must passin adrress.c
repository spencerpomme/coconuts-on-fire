#include <stdio.h>
int change(const int ar[], int n);
void alter(int *ptr);
int main(void)
{
	int n = 10;
	int sum;
	int ar[10] = {1,2,3,4,5,6,7,8,9,10};
	printf("sum = %d\n", change(ar, n));
	alter(&n); // ����ԭ������ʽ������ָ�����͵ģ������ֵ�����ǵ�ַ 
	printf("new n is %d", n);
	return 0;	
}

int change(const int ar[], int n)
{
	int i;
	int total = 0;
	
	for (i = 0; i < n; i++)
		total += ar[i];
	return total;
}

void alter(int *ptr)
{
	*ptr = 30;
}
