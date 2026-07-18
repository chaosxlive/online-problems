// This should be run on linux env because of the srand behavior

#include <fstream>
#include <string>

using namespace std;

string generateRandomPassword() {
  string res(20, '.');
  for (int i = 0; i < 20; ++i) {
    res[i] = 'a' + rand() % 26;
  }
  return res;
}

int main() {
  int seed = time(0);
  ofstream outputFile("output.txt");

  for (int i = -3000; i <= 3000; i++) {
    srand(seed + i);
    outputFile << "Seed " << i << ": " << seed + i << " - "
               << "Password 1 is: " << generateRandomPassword() << '\n'
               << "Password 2 is: " << generateRandomPassword() << '\n'
               << "Password 3 is: " << generateRandomPassword() << '\n';
  }
  outputFile << '\n';
  return 0;
}