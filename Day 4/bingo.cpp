#include<iostream>
#include<fstream>

#include<vector>

using namespace std;

const int bits = 12;

struct Bingo {
    int  values[5][5];
    bool marks[5][5] = {{false, false, false, false, false},
                        {false, false, false, false, false},
                        {false, false, false, false, false},
                        {false, false, false, false, false},
                        {false, false, false, false, false}};

    Bingo(vector<int>& numbers) {
        for (int i = 0; i < 25; ++i)
            values[i/5][i%5] = numbers[i];
        numbers.clear();
    }

    bool mark (int n) {
        for (int i = 0; i < 25; ++i)
            if (values[i/5][i%5] == n) {
                marks[i/5][i%5] = true;
                return win(i/5, i%5);
            }
        return false;
    }

    bool win (int i, int j) {
        bool h = true;
        bool v = true;
        for (int k = 0; k < 5; ++k) {
            h &= marks[i][k];
            v &= marks[k][j];
        }
        return h || v;
    }

    int score (int n) {
        int sum = 0;
        for (int i = 0; i < 25; ++i)
            sum += values[i/5][i%5] * !marks[i/5][i%5];
        return sum * n;
    }
};

int winner(const vector<int>& numbers, vector<Bingo> cards) {
    for (int n : numbers)
        for (Bingo& b : cards)
            if (b.mark(n))
                return b.score(n);
    return 0;
}

int loser(const vector<int>& numbers, vector<Bingo> cards) {
    for (int n : numbers) {
        int i = 0;
        while (i < cards.size() && cards.size() > 1)
            if (cards[i].mark(n) && cards.size() > 1)
                cards.erase(begin(cards)+i);
            else
                ++i;
        if (cards.size() == 1 && cards[0].mark(n))
            return(cards[0].score(n));
    }

    return 0;
}

int main() {
    string line;
    
    ifstream in_numbers ("numbers");
    vector<int> numbers;
    
    while (std::getline(in_numbers, line))
        numbers.push_back(stoi(line));

    ifstream in_cards ("cards");
    vector<int> bingo_numbers;
    vector<Bingo> cards;

    int n;
    while (in_cards >> n) {
        bingo_numbers.push_back(n);
        if (bingo_numbers.size() == 25)
            cards.push_back(Bingo(bingo_numbers));
    }

    int winner_score = winner(numbers, cards);
    int loser_score  = loser (numbers, cards);

    ofstream out;
    out.open ("output");
    out << winner_score << '\n' << loser_score << '\n';
    out.close();
    return 0;
}