class Solution {
    public double angleClock(int hour, int minutes) {
        double minuteAngle = (double) minutes * 6;
        double hourAngle = ((double) hour % 12) * 30 + ((double) minutes / 2);
        double diff = Math.abs(hourAngle - minuteAngle);
        return Math.min(diff, 360 - diff);
    }
}
