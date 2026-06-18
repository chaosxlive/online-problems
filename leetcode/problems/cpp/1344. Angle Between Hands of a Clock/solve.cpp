#include <algorithm>
#include <cmath>

class Solution {
public:
  double angleClock(int hour, int minutes) {
    double minuteAngle = minutes * 6;
    double hourAngle = (hour % 12) * 30 + minutes / 2.0;
    double diff = std::abs(hourAngle - minuteAngle);
    return std::min(diff, 360 - diff);
  }
};