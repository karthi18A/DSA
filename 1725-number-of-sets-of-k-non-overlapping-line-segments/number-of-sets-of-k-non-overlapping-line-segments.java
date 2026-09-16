
class Solution {
    static final int MOD = 1000000007;

    public int numberOfSets(int n, int k) {
        long[][] dp = new long[n][k + 1];

        // 0 segments can always be selected in 1 way
        for (int i = 0; i < n; i++) {
            dp[i][0] = 1;
        }

        for (int segments = 1; segments <= k; segments++) {
            long sum = 0;

            for (int points = 1; points < n; points++) {

                // Add possibilities where a new segment starts
                sum = (sum + dp[points - 1][segments - 1]) % MOD;

                // Either:
                // 1. Don't end a segment at this point
                // 2. End a segment here
                dp[points][segments] =
                    (dp[points - 1][segments] + sum) % MOD;
            }
        }

        return (int) dp[n - 1][k];
    }
}

