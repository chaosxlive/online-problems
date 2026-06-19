#include <vector>

using namespace std;

class Solution {
public:
  int largestAltitude(vector<int> &gain) {
    int altitude = 0;
    int maxAlutitude = 0;
    for (int i = 0; i < gain.size(); i++) {
      altitude += gain[i];
      maxAlutitude = max(maxAlutitude, altitude);
    }
    return maxAlutitude;
  }
};