/*
 * Program to calculate the number of cards in the shoe.
 * This code is released under the Vegas Public License.
 * (c)2020, The College Blackjack Team.
 */
#include <stdio.h>

int main()
{
    int decks;
    puts("Enter a number of decks");
    scanf("%i", &decks);
    if (deck < 1) {
        puts("That is not a valid numbers of decks");
        return 1;
    }
    printf("There are %i cards\n", (decks * 52));
    return 0;
}