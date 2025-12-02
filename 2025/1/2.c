#include "stdio.h"
#define MAX ((int)100)

int main(void)
{
    char d = 0;
    int steps = 0;
    int s;

    int zeros = 0;
    int position = MAX/2;

    while(2 == scanf("%c%i\n", &d, &s))
    {
        printf("%d %c%d", position, d, s);
        switch(d)
        {
            case 'L':
                while(s--) {
                    position--;
                    if (position == 0) {
                        zeros++;
                    } else if (position < 0) {
                        position += MAX;
                    }
                }
                break;
            case 'R':
                while(s--) {
                    position++;
                    if (position == MAX) {
                        zeros++;
                        position = 0;
                    }
                }
                break;
        }
        printf(" %d (%d)\n", position, zeros);
    }
    printf("\n%d\n", zeros);
    return 0;
}
