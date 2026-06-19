class Solution {
    public int jump(int[] nums) {
        int n = nums.length;
        if (n <= 1) {
            return 0;
        }

        int steps = 1;
        int farthest = 0;
        int checkEnd = 0;
        for (int i = 0; i < n - 1; i++) {
            farthest = Math.max(i + nums[i], farthest);
            if (farthest >= n - 1) {
                break;
            }
            if (i == checkEnd) {
                steps++;
                checkEnd = farthest;
            }
        }
        return steps;
    }
}