/*** 
 * @Author: 560130
 * @Date: 2022-04-13 14:23:25
 * @LastEditTime: 2022-04-13 15:53:32
 * @LastEditors: 560130
 * @Description: 
 * @FilePath: /bell_C++/bell.cpp
 */

#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main()
{
    vector<string> msg {"Hello", "C++", "World", "from", "VS Code", "and the C++ extension!"};

    for (const string& word : msg)
    {
        cout << word << " ";
    }
    cout << endl;
}
