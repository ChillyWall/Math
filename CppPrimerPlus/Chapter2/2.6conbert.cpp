//
// Created by Administrator on 2020/5/20.
// convert.cpp -- convert stone to pounds

#include <iostream>
#include <string>
int stonetolb(int);             // function prototype
int main()
{
    using namespace std;
    string timer = "continue";
    while (timer == "continue")
    {
        int stone;
        cout << "Enter the weight in stone: "
             << "(Enter 'quit to quit)"
             << endl;
        string usedVar;
        cin >> usedVar;
        if (usedVar == "quit")
        {
            break;
        } else {
            stone = stoi (usedVar);
        }
        int pounds = stonetolb(stone);
        cout << stone << " stone = ";
        cout << pounds << " pounds." << endl;
    }

    return 0;
}

int stonetolb(int sts)
{
    return 14 * sts;
}