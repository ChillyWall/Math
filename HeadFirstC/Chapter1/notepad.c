/*
 * Program to calculate the number of cards in the shoe.
 * This code is released under the Vegas Public License.
 * (c)2020, The College Blackjack Team.
 */
#include <stdio.h>
#include <stdlib.h>
int main()
{
    int decks;
    puts("Enter a number of decks");
    scanf("%i", &decks);
    if (decks < 1) {
        puts("That is not a valid numbers of decks\n");
        return 1;
    }

    printf("There are %i cards\n", (decks * 52));
	/*暂停一下，用于观察运行结果*/
	
    return 0;
}