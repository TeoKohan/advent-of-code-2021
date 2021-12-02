#include<iostream>
#include<fstream>
#include<vector>

#include<numeric>

#define BOT -1

using namespace std;

int readthree (ifstream& input, int& v) {
    string line;
    vector<int> V;
    for (int i = 0; i < 3 && getline(input, line); ++i)
        V.push_back(stoi(line));
    v = accumulate(begin(V), end(V), 0);
    return V.size() == 3;
}

int main() {
    int n, m;
    ifstream input ("input");
    vector<int> V;
    string line;
    while (getline(input, line))
        V.push_back(stoi(line));
    
    int previous = V[0] + V[1] + V[2];
    int actual;
    int result = 0;
    for (int i = 3; i < V.size(); ++i) {
        actual = previous + V[i] - V[i-3];
        result += actual > previous;
        previous = actual;
    }
    
    cout << result << endl;

    ofstream out;
    out.open ("output");
    out << result;
    out.close();
    return 0;
}