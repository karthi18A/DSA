class Solution {
    public int minimumDeletions(int[] nums) {

        int n = nums.length;

        int min = 0;
        int max = 0;

        for (int i = 1; i < n; i++) {

            if (nums[i] < nums[min]) {
                min = i;
            }

            if (nums[i] > nums[max]) {
                max = i;
            }
        }

        int a = Math.min(min, max);
        int b = Math.max(min, max);

        int front = b + 1;

        int back = n - a;

        int both = (a + 1) + (n - b);

        return Math.min(front, Math.min(back, both));
    }
}