class Solution {
    public int largestAltitude(int[] gain) {
        int altitude = 0;
        int maxAlutitude = 0;
        for (int i = 0; i < gain.length; i++) {
            altitude += gain[i];
            if (altitude > maxAlutitude) {
                maxAlutitude = altitude;
            }
        }
        return maxAlutitude;
    }
}