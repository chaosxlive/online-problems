class Solution {
    public int maximumProduct(int[] nums) {
        int min_1 = Integer.MAX_VALUE, min_2 = Integer.MAX_VALUE;
        int max_1 = Integer.MIN_VALUE, max_2 = Integer.MIN_VALUE, max_3 = Integer.MIN_VALUE;

        for (int num : nums) {
            if (num <= min_1) {
                min_2 = min_1;
                min_1 = num;
            } else if (num <= min_2) {
                min_2 = num;
            }
            if (num >= max_1) {
                max_3 = max_2;
                max_2 = max_1;
                max_1 = num;
            } else if (num >= max_2) {
                max_3 = max_2;
                max_2 = num;
            } else if (num >= max_3) {
                max_3 = num;
            }
        }
        return Math.max(min_1 * min_2 * max_1, max_1 * max_2 * max_3);
    }
}