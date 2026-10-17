class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        used = [False] * len(nums)

        def backtrack():
            if len(path) == len(nums):
                result.append(path[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                path.append(nums[i])
                backtrack()
                path.pop()
                used[i] = False

        backtrack()
        return result


class Solution {
public:
    int numTrees(int n) {
        vector<int> dp(n + 1, 0);
        dp[0] = dp[1] = 1;

        for (int nodes = 2; nodes <= n; nodes++) {
            for (int root = 1; root <= nodes; root++) {
                dp[nodes] += dp[root - 1] * dp[nodes - root];
            }
        }

        return dp[n];
    }
};

class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1

        for nodes in range(2, n + 1):
            for root in range(1, nodes + 1):
                dp[nodes] += dp[root - 1] * dp[nodes - root]

        return dp[n]


#include <string>
using namespace std;

class Solution {
public:
    string countAndSay(int n) {
        string s = "1";
        for (int step = 1; step < n; ++step) {
            string next;
            int i = 0;
            while (i < (int)s.size()) {
                int j = i;
                while (j < (int)s.size() && s[j] == s[i]) ++j;
                next += to_string(j - i);
                next += s[i];
                i = j;
            }
            s = move(next);
        }
        return s;
    }
};

