print ( "sania is my best friend" )

class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int i = m - 1;         
        int j = n - 1;          
        int k = m + n - 1;
             
        while (j >= 0) {
            if (i >= 0 && nums1[i] > nums2[j])
                nums1[k--] = nums1[i--];
            else
                nums1[k--] = nums2[j--];
        }
    }
};


class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int k = 0;                       // next position for a kept element
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] != val) {
                nums[k] = nums[i];
                k++;
            }
        }
        return k;
    }
};



class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        bool row[9][9] = {}, col[9][9] = {}, box[9][9] = {};

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (board[i][j] == '.') continue;

                int d = board[i][j] - '1';       // digit 1-9 -> index 0-8
                int b = (i / 3) * 3 + j / 3;     // which 3x3 box

                if (row[i][d] || col[j][d] || box[b][d]) return false;
                row[i][d] = col[j][d] = box[b][d] = true;
            }
        }
        return true;
    }
};




class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
            result.append(str(total % 2))
            carry = total // 2

        return "".join(reversed(result))






class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [float('inf')] * n
        dp[0] = 0

        for i in range(m):
            dp[0] += grid[i][0]
            for j in range(1, n):
                dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]

        return dp[-1]
        
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [float('inf')] * n
        dp[0] = 0

        for i in range(m):
            dp[0] += grid[i][0]
            for j in range(1, n):
                dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]

        return dp[-1]


class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> result;
        backtrack(nums, 0, result);
        return result;
    }

private:
    void backtrack(vector<int>& nums, int start, vector<vector<int>>& result) {
        if (start == nums.size()) {
            result.push_back(nums);
            return;
        }
        for (int i = start; i < nums.size(); i++) {
            swap(nums[start], nums[i]);
            backtrack(nums, start + 1, result);
            swap(nums[start], nums[i]);
        }
    }
};




/**
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */

class Solution {
public:
    int guessNumber(int n) {
        int low = 1, high = n;

        while (low <= high) {
            int mid = low + (high - low) / 2;
            int res = guess(mid);

            if (res == 0) return mid;
            if (res == -1) high = mid - 1;   // guess too high, go lower
            else low = mid + 1;              // guess too low, go higher
        }

        return -1;
    }
};


/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> result;
        stack<TreeNode*> st;
        TreeNode* curr = root;

        while (curr || !st.empty()) {
            while (curr) {
                st.push(curr);
                curr = curr->left;
            }
            curr = st.top();
            st.pop();
            result.push_back(curr->val);
            curr = curr->right;
        }

        return result;
    }
};







class Solution:
    def isInterleave(self, s1, s2, s3):
        n, m = len(s1), len(s2)
        if n + m != len(s3):
            return False

        dp = [False] * (m + 1)
        dp[0] = True
        for j in range(1, m + 1):
            dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]

        for i in range(1, n + 1):
            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]
            for j in range(1, m + 1):
                dp[j] = ((dp[j] and s1[i - 1] == s3[i + j - 1]) or
                         (dp[j - 1] and s2[j - 1] == s3[i + j - 1]))
        return dp[m]

class Solution:
    def sortPermutation(self, nums):
        ans = -1  # all bits set
        for i, v in enumerate(nums):
            if v != i:
                ans &= v
        return 0 if ans == -1 else ans



class Solution:
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def day_of_year(d):
            m, dd = int(d[:2]), int(d[3:])
            return sum(days[:m - 1]) + dd

        start = max(day_of_year(arriveAlice), day_of_year(arriveBob))
        end = min(day_of_year(leaveAlice), day_of_year(leaveBob))
        return max(0, end - start + 1)


class Solution:
    def grayCode(self, n):
        return [i ^ (i >> 1) for i in range(1 << n)]
