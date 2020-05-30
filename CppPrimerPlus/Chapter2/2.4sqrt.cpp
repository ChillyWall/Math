//
// Created by Administrator on 2020/5/18.
//

#include <iostream>
#include <cmath>

int main()
{
    using namespace std;

    double area;
    cout << "Enter the floor area, in square feet, of your home: ";
    cin >> area;
    double side;
    side = sqrt(area);
    cout << "That's the equivalent of a square " << side
         << " feet to the side." << endl;
    cout << "How fascinating!" << endl;
    double squareRoot = pow(5.0, 10.0);
    cout << squareRoot;
    return 0;
}