#include<iostream>
#include<fstream>
#include<vector>

using namespace std;
typedef vector<int> List;

List windows(const List& L) {
    List M;
    for (int i = 0; i < L.size() - 2; ++i)
        M.push_back(L[i]+L[i+1]+L[i+2]);
    return M;
}

int descending(const List& L) {
    int sum = 0;
    for (int i = 0; i < L.size() - 1; ++i)
        sum += L[i+1] > L[i];
    return sum;
}

int main() {
    ifstream input ("input");
    List L;
    int n;
    while (input >> n)
        L.push_back(n);

    ofstream out;
    out.open ("output");
    out << descending(L) << '\n' << descending(windows(L)) << '\n';
    out.close();
    return 0;
}