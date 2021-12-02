#include<iostream>
#include<fstream>

#include<vector>

using namespace std;

int main() {
    int n, m;
    ifstream input ("input");
    
    int result = 0;
    int count = 1;
    input >> n;
    while (input >> m && count < 191) {
        if (m > n)
            ++result;
        n = m;
        ++count;
    }
    cout << n << endl;
    cout << count << endl;
    cout << result << endl;

    ofstream out;
    out.open ("output");
    out << result;
    out.close();
    return 0;
}