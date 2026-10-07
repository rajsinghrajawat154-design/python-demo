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












""
Travelling Salesman Problem (TSP)
 
Two exact solutions:
  1. Brute force   - tries every permutation, O(n!)
  2. Held-Karp DP  - bitmask dynamic programming, O(n^2 * 2^n)
 
Both return the minimum tour cost and the tour itself (starting and ending at city 0).
"""
 
from itertools import permutations
 
INF = float("inf")
 
 
def tsp_brute_force(dist):
    n = len(dist)
    best_cost = INF
    best_tour = None
 
    # Fix city 0 as the start, permute the rest
    for perm in permutations(range(1, n)):
        cost = dist[0][perm[0]]
        for i in range(len(perm) - 1):
            cost += dist[perm[i]][perm[i + 1]]
        cost += dist[perm[-1]][0]
 
        if cost < best_cost:
            best_cost = cost
            best_tour = [0] + list(perm) + [0]
 
    return best_cost, best_tour
 
 
def tsp_held_karp(dist):
    n = len(dist)
    FULL = 1 << n
 
    # dp[mask][i] = min cost to start at 0, visit exactly the cities in mask, end at i
    dp = [[INF] * n for _ in range(FULL)]
    parent = [[-1] * n for _ in range(FULL)]
    dp[1][0] = 0  # only city 0 visited, standing at city 0
 
    for mask in range(FULL):
        if not (mask & 1):  # every valid mask must contain city 0
            continue
        for last in range(n):
            if not (mask & (1 << last)) or dp[mask][last] == INF:
                continue
            for nxt in range(n):
                if mask & (1 << nxt):
                    continue
                new_mask = mask | (1 << nxt)
                new_cost = dp[mask][last] + dist[last][nxt]
                if new_cost < dp[new_mask][nxt]:
                    dp[new_mask][nxt] = new_cost
                    parent[new_mask][nxt] = last
 
    # Close the tour by returning to city 0
    best_cost = INF
    last_city = -1
    for i in range(1, n):
        cost = dp[FULL - 1][i] + dist[i][0]
        if cost < best_cost:
            best_cost = cost
            last_city = i
 
    # Rebuild the path by walking the parent pointers backwards
    tour = [0]
    mask = FULL - 1
    cur = last_city
    path = []
    while cur != -1:
        path.append(cur)
        prev = parent[mask][cur]
        mask ^= 1 << cur
        cur = prev
    tour = [0] + path[::-1][1:] + [0] if path[-1] == 0 else [0] + path[::-1] + [0]
 
    return best_cost, tour
 
 
def main():
    # Example: 4 cities, symmetric distance matrix
    dist = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0],
    ]
 
    print("Distance matrix:")
    for row in dist:
        print(row)
 
    cost, tour = tsp_brute_force(dist)
    print("\nBrute force:")
    print("  Minimum cost:", cost)
    print("  Tour:", " -> ".join(map(str, tour)))
 
    cost, tour = tsp_held_karp(dist)
    print("\nHeld-Karp DP:")
    print("  Minimum cost:", cost)
    print("  Tour:", " -> ".join(map(str, tour)))
 
 
if __name__ == "__main__":
    main()
 
 
