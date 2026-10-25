def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Assume the current position holds the minimum
        min_idx = i
        # Find the actual minimum in the remaining unsorted part
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum with the first unsorted element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Example usage
numbers = [64, 25, 12, 22, 11]
sorted_numbers = selection_sort(numbers)
print(sorted_numbers)  # Output: [11, 12, 22, 25, 64]




class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows == 1 || numRows >= (int)s.size()) return s;

        vector<string> rows(numRows);
        int row = 0;
        int dir = 1;  // +1 moving down, -1 moving up

        for (char c : s) {
            rows[row] += c;
            // bounce at the top and bottom rows
            if (row == 0) dir = 1;
            else if (row == numRows - 1) dir = -1;
            row += dir;
        }

        string result;
        for (const string& r : rows) result += r;
        return result;
    }
};




class Solution {
public:
    int myAtoi(string s) {
        int i = 0, n = s.size();

        // 1. Skip leading whitespace
        while (i < n && s[i] == ' ') i++;

        // 2. Determine sign
        int sign = 1;
        if (i < n && (s[i] == '+' || s[i] == '-')) {
            if (s[i] == '-') sign = -1;
            i++;
        }

        // 3. Read digits, clamping on overflow
        int result = 0;
        while (i < n && isdigit(s[i])) {
            int digit = s[i] - '0';

            // Check overflow BEFORE result * 10 + digit
            if (result > INT_MAX / 10 || (result == INT_MAX / 10 && digit > 7)) {
                return sign == 1 ? INT_MAX : INT_MIN;
            }

            result = result * 10 + digit;
            i++;
        }

        return sign * result;
    }
};


class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int n = nums.size();

        for (int lo = 0, hi = n; lo < hi; ) {
            int mid = lo + (hi - lo) / 2;
            if (nums[mid] < target) lo = mid + 1;
            else hi = mid;

            if (lo >= hi) return lo;
        }
        return n;   // only reached when n == 0
    }
};

class Solution {
public:
    int lengthOfLastWord(string s) {
        int len = 0;

        for (int i = s.size() - 1; i >= 0; i--) {
            if (s[i] != ' ') {
                len++;                  // inside the last word
            } else if (len > 0) {
                break;                  // hit the space before the last word
            }                           // else: still skipping trailing spaces
        }
        return len;
    }
};




//  * Definition for singly-linked list.
//  * struct ListNode {
//  *     int val;
//  *     ListNode *next;
//  *     ListNode() : val(0), next(nullptr) {}
//  *     ListNode(int x) : val(x), next(nullptr) {}
//  *     ListNode(int x, ListNode *next) : val(x), next(next) {}
//  * };
 
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode dummy;                 // placeholder node before the real head
        ListNode* tail = &dummy;

        while (list1 && list2) {
            if (list1->val <= list2->val) {
                tail->next = list1;
                list1 = list1->next;
            } else {
                tail->next = list2;
                list2 = list2->next;
            }
            tail = tail->next;
        }

        tail->next = list1 ? list1 : list2;   // attach whatever remains

        return dummy.next;
    }
};


class Solution {
public:
    int divide(int dividend, int divisor) {
        // only overflow case: -2^31 / -1 = 2^31
        if (dividend == INT_MIN && divisor == -1) return INT_MAX;

        bool negative = (dividend < 0) != (divisor < 0);
        long long a = llabs((long long)dividend);
        long long b = llabs((long long)divisor);

        long long quotient = 0;
        for (int i = 31; i >= 0; i--) {
            if ((a >> i) >= b) {      // b * 2^i fits into what is left of a
                a -= b << i;
                quotient += 1LL << i;
            }
        }
        return negative ? -quotient : quotient;
    }
};

#include <bits/stdc++.h>
using namespace std;
 
void mergeSort(vector<int>& a, int l, int r) {
    if (l >= r) return;
    int m = (l + r) / 2;
    mergeSort(a, l, m);
    mergeSort(a, m + 1, r);
    inplace_merge(a.begin() + l, a.begin() + m + 1, a.begin() + r + 1);
}
 
int main() {
    vector<int> a = {38, 27, 43, 3, 9, 82, 10};
    mergeSort(a, 0, a.size() - 1);
    for (int x : a) cout << x << " ";
}








class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.empty()) return 0;

        int k = 1;                           // nums[0..k-1] holds the unique values
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] != nums[k - 1]) {    // found a new value
                nums[k] = nums[i];
                k++;
            }
        }
        return k;
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
    int strStr(string haystack, string needle) {
        int n = haystack.size(), m = needle.size();

        for (int i = 0; i + m <= n; i++) {       // every possible start position
            int j = 0;
            while (j < m && haystack[i + j] == needle[j])
                j++;
            if (j == m) return i;                // whole needle matched
        }
        return -1;
    }
}; 




##Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
##solution
class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> res;
        string cur;
        build(res, cur, 0, 0, n);
        return res;
    }

private:
    void build(vector<string>& res, string& cur, int open, int close, int n) {
        if (cur.size() == 2 * n) {          // used all n pairs
            res.push_back(cur);
            return;
        }
        if (open < n) {                     // can still add '('
            cur.push_back('(');
            build(res, cur, open + 1, close, n);
            cur.pop_back();                 // backtrack
        }
        if (close < open) {                 // can add ')' only if it closes something
            cur.push_back(')');
            build(res, cur, open, close + 1, n);
            cur.pop_back();                 // backtrack
        }
    }
};


/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        ListNode dummy(0, head);
        ListNode* prev = &dummy;

        while (prev->next && prev->next->next) {
            ListNode* a = prev->next;       // first node of the pair
            ListNode* b = a->next;          // second node of the pair

            a->next = b->next;              // a points past the pair
            b->next = a;                    // b points back to a
            prev->next = b;                 // previous part points to b

            prev = a;                       // a is now the tail of the swapped pair
        }
        return dummy.next;
    }
};







class Solution {
public:
    int climbStairs(int n) {
        int a = 1, b = 1;              // ways to reach step 0 and step 1
        for (int i = 2; i <= n; i++) {
            int c = a + b;             // ways(i) = ways(i-1) + ways(i-2)
            a = b;
            b = c;
        }
        return b;
    }
};




class Solution {
public:
    int mySqrt(int x) {
        int lo = 0, hi = x, ans = 0;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if ((long long)mid * mid <= x) {   // mid could be the answer
                ans = mid;
                lo = mid + 1;                  // try a bigger one
            } else {
                hi = mid - 1;                  // too big
            }
        }
        return ans;
    }
};




class Solution {
public:
    vector<vector<string>> solveNQueens(int n) {
        vector<vector<string>> res;
        vector<string> board(n, string(n, '.'));
        vector<bool> col(n), d1(2 * n), d2(2 * n);
        solve(0, n, board, col, d1, d2, res);
        return res;
    }

private:
    void solve(int r, int n, vector<string>& board, vector<bool>& col,
               vector<bool>& d1, vector<bool>& d2, vector<vector<string>>& res) {
        if (r == n) { res.push_back(board); return; }   // all rows filled
        for (int c = 0; c < n; c++) {
            if (col[c] || d1[r + c] || d2[r - c + n]) continue;   // attacked

            board[r][c] = 'Q';                                    // place
            col[c] = d1[r + c] = d2[r - c + n] = true;

            solve(r + 1, n, board, col, d1, d2, res);             // next row

            board[r][c] = '.';                                    // undo
            col[c] = d1[r + c] = d2[r - c + n] = false;
        }
    }
};



class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        for (int i = digits.size() - 1; i >= 0; i--) {
            if (digits[i] < 9) {       // no carry needed, done
                digits[i]++;
                return digits;
            }
            digits[i] = 0;             // 9 becomes 0, carry moves left
        }
        digits.insert(digits.begin(), 1);   // all digits were 9
        return digits;
    }
};


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
    void recoverTree(TreeNode* root) {
        TreeNode *first = nullptr, *second = nullptr, *prev = nullptr;
        inorder(root, first, second, prev);
        swap(first->val, second->val);
    }

private:
    void inorder(TreeNode* node, TreeNode*& first, TreeNode*& second, TreeNode*& prev) {
        if (!node) return;
        inorder(node->left, first, second, prev);
        if (prev && prev->val > node->val) {
            if (!first) first = prev;
            second = node;
        }
        prev = node;
        inorder(node->right, first, second, prev);
    }
};


class Solution:
    def sortableIntegers(self, nums):
        n = len(nums)
        s = sorted(nums)
        total = 0
        for k in range(1, n + 1):
            if n % k:
                continue
            ok = True
            for i in range(0, n, k):
                b = nums[i:i + k]
                if sorted(b) != s[i:i + k]:
                    ok = False
                    break
                descents = sum(b[j] > b[(j + 1) % k] for j in range(k))
                if descents > 1:
                    ok = False
                    break
            if ok:
                total += k
        return total


class Solution:
    def minSwaps(self, nums):
        n = len(nums)

        def ds(x):
            s = 0
            while x:
                s += x % 10
                x //= 10
            return s

        target = sorted(nums, key=lambda x: (ds(x), x))
        pos = {v: i for i, v in enumerate(target)}

        visited = [False] * n
        swaps = 0
        for i in range(n):
            if visited[i] or pos[nums[i]] == i:
                continue
            j = i
            length = 0
            while not visited[j]:
                visited[j] = True
                j = pos[nums[j]]
                length += 1
            swaps += length - 1
        return swaps

class Solution:
    def closedIsland(self, grid):
        m, n = len(grid), len(grid[0])

        def fill(r, c):
            stack = [(r, c)]
            grid[r][c] = 1
            while stack:
                x, y = stack.pop()
                for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 0:
                        grid[nx][ny] = 1
                        stack.append((nx, ny))

        # remove islands touching the border
        for i in range(m):
            for j in range(n):
                if (i in (0, m - 1) or j in (0, n - 1)) and grid[i][j] == 0:
                    fill(i, j)

        # count the remaining (closed) islands
        count = 0
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if grid[i][j] == 0:
                    count += 1
                    fill(i, j)
        return count

class Solution:
    def subsets(self, nums):
        res = [[]]
        for x in nums:
            res += [cur + [x] for cur in res]
        return res

from collections import Counter

class Solution:
    def findSubstring(self, s, words):
        if not s or not words:
            return []
        w, m = len(words[0]), len(words)
        need = Counter(words)
        res = []

        for offset in range(w):
            left = offset
            count = 0
            seen = {}
            for right in range(offset, len(s) - w + 1, w):
                word = s[right:right + w]
                if word in need:
                    seen[word] = seen.get(word, 0) + 1
                    count += 1
                    while seen[word] > need[word]:
                        lw = s[left:left + w]
                        seen[lw] -= 1
                        count -= 1
                        left += w
                    if count == m:
                        res.append(left)
                        lw = s[left:left + w]
                        seen[lw] -= 1
                        count -= 1
                        left += w
                else:
                    seen.clear()
                    count = 0
                    left = right + w
        return res
        
        
