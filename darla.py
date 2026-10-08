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
