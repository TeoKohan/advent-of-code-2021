#include<iostream>
#include<fstream>

#include<vector>

using namespace std;

const int bits = 12;

int main() {
    ifstream input ("input");
    
    string line;
    int gamma[12] = {0};
    while (std::getline(input, line))
        for (int i = 0; i < bits; ++i)
            gamma[i] += (std::stoi(line, nullptr, 2) & (1 << i)) ? 1 : -1;

    int gamma_value = 0;
    int epsilon_value = 0;
    for (int i = 0; i < bits; ++i) {
        gamma_value   += (gamma[i] > 0) << i;
        epsilon_value += (gamma[i] <= 0) << i;
    }

    ofstream out;
    out.open ("output");
    out << gamma_value * epsilon_value;
    out.close();
    return 0;
}