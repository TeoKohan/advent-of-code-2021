#include<iostream>
#include<fstream>

#include<vector>

using namespace std;

const int bits = 12;

int most_common(const vector<int>& V, int bit) {
    int count = 0;
    for (int i = 0; i < V.size(); ++i)
        count += ((V[i] & (1 << bit)) ? 1 : -1);
    return (count >= 0);
}

int main() {
    ifstream input ("input");
    string line;
    vector<int> O2;
    while (std::getline(input, line))
        O2.push_back(std::stoi(line, nullptr, 2));
    auto CO2 = O2;

    for (int bit = bits - 1; bit >= 0 && O2.size() > 1; --bit) {
        int value = most_common(O2, bit);
        for (int i = 0; i < O2.size() && O2.size() > 1; ++i)
            while (i < O2.size() && O2.size() > 1 && ((O2[i] & (1 << bit)) > 0 != value))
                O2.erase(begin(O2)+i);
    }

    for (int bit = bits - 1; bit >= 0 && CO2.size() > 1; --bit) {
        int value = most_common(CO2, bit);
        for (int i = 0; i < CO2.size() && CO2.size() > 1; ++i)
            while (i < CO2.size() && CO2.size() > 1 && ((CO2[i] & (1 << bit)) > 0 == value))
                CO2.erase(begin(CO2)+i);
    }

    ofstream out;
    out.open ("output");
    out << O2[0] * CO2[0];
    out.close();
    return 0;
}