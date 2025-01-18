#include <cstdio>
#include <iostream>
#include <vector>
using namespace std;

int main(void) {
    cin.tie(0);
    vector<string> nouns;
    vector<string> verbs;

    string s;
    cin >> s;

    if (s != "Nouns:")
        return -1;

    cin >> s;

    while (s != "Verbs:") {
        nouns.push_back(s);
        cin >> s;
    }

    while (cin) {
        cin >> s;
        verbs.push_back(s);
    }

    for (string &noun1: nouns) {
        for (string &noun2: nouns) {
            for (string &verb: verbs) {
                cout << noun1 << " " << verb << " " << noun2 << "\n";
            }
        }
    }

    cout << flush;

    return 0;
}
