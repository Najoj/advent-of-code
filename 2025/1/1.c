#include "stdio.h"
#define MAX ((int)100)

int main(void)
{
    char d = 0;
    int s;

    int zeros = 0;
    int position = MAX/2;

    while(2 == scanf("%c%i\n", &d, &s))
    {
        switch(d)
        {
            case 'L':
                position -= s;
                position = position < 0 ? (position + MAX) % MAX: position;
                while(position < 0)
                {
                    position += MAX;
                }
                while(position >= MAX)
                {
                    position -= MAX;
                }
                if(position == 0)
                    zeros++;
                break;
            case 'R':
                position += s;
                position = position >= MAX ? (position + MAX) % MAX: position;
                while(position < 0)
                {
                    position += MAX;
                }
                while(position >= MAX)
                {
                    position -= MAX;
                }
                if(position == 0)
                    zeros++;
                break;
        }
    }
    printf("\n%d\n", zeros);
    return 0;
}
