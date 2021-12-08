#include<iostream>
#include<fstream>

#include<vector>

using namespace std;
typedef vector<int> List;

const int bits = 12;

int most_common(const List& L, int bit) {
    int count = 0;
    for (int i = 0; i < L.size(); ++i)
        count += ((L[i] & (1 << bit)) ? 1 : -1);
    return (count >= 0);
}

int epsilon_gamma(const List& L) {
    string line;
    int gamma[12] = {0};
    for (int l : L)
        for (int i = 0; i < bits; ++i)
            gamma[i] += l & (1 << i) ? 1 : -1;

    int gamma_value = 0;
    int epsilon_value = 0;
    for (int i = 0; i < bits; ++i) {
        gamma_value   += (gamma[i] > 0) << i;
        epsilon_value += (gamma[i] <= 0) << i;
    }

    return gamma_value * epsilon_value;
}

int life_support(const List& L) {

    auto O2  = L;
    auto CO2 = L;

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

    return O2[0] * CO2[0];
}

int main() {
    ifstream input ("input");
    string line;
    List L;
    while (std::getline(input, line))
        L.push_back(std::stoi(line, nullptr, 2));

    ofstream out;
    out.open ("output");
    out << epsilon_gamma(L) << '\n' << life_support(L) << '\n';
    out.close();
    return 0;
}