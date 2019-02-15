
#include <stdio.h>

int main()
{
	int i,r;
	for(i=1;i<256;i+=2)
	{
		r = (255*i + 28)%256;

		if(r == 183)
		{
			printf("Este es el número: ");
		}

		printf("%d\n",i);
	}
}
