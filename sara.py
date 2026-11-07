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



#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> res;
        vector<int> cur;
        vector<bool> used(nums.size(), false);
        backtrack(nums, used, cur, res);
        return res;
    }

private:
    void backtrack(const vector<int>& nums, vector<bool>& used,
                   vector<int>& cur, vector<vector<int>>& res) {
        if (cur.size() == nums.size()) {
            res.push_back(cur);
            return;
        }
        for (int i = 0; i < (int)nums.size(); ++i) {
            if (used[i]) continue;
            // skip duplicates: only use nums[i] if its equal predecessor is already used
            if (i > 0 && nums[i] == nums[i - 1] && !used[i - 1]) continue;
            used[i] = true;
            cur.push_back(nums[i]);
            backtrack(nums, used, cur, res);
            cur.pop_back();
            used[i] = false;
        }
    }
};


class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        auto cmp = [](ListNode* a, ListNode* b) { return a->val > b->val; };
        priority_queue<ListNode*, vector<ListNode*>, decltype(cmp)> pq(cmp);

        for (ListNode* node : lists)
            if (node) pq.push(node);

        ListNode dummy(0);
        ListNode* tail = &dummy;

        while (!pq.empty()) {
            ListNode* node = pq.top();
            pq.pop();
            tail->next = node;
            tail = node;
            if (node->next) pq.push(node->next);
        }

        return dummy.next;
    }
};




class Solution {
public:
    vector<int> targetIndices(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());

        vector<int> ans;

        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] == target) {
                ans.push_back(i);
            }
        }

        return ans;
    }
};


class Solution:
    def minOperations(self, s):
        n = len(s)
        t = sorted(s)
        if list(s) == t:
            return 0
        if n == 2:
            return -1
        if s[0] == t[0] or s[-1] == t[-1]:
            return 1
        interior = s[1:-1]
        if t[0] in interior or t[-1] in interior:
            return 2
        return 3
        




class Solution(object):
    def minMoves(self, nums):
        return len(nums) * max(nums) - sum(nums)



class Solution(object):
    def sumCounts(self, nums):
        n = len(nums)
        s = [0] * (4 * n)
        q = [0] * (4 * n)
        lz = [0] * (4 * n)

        def apply(o, l, r, v):
            ln = r - l + 1
            q[o] += 2 * v * s[o] + ln * v * v
            s[o] += v * ln
            lz[o] += v

        def push(o, l, r):
            if lz[o]:
                m = (l + r) // 2
                apply(2 * o, l, m, lz[o])
                apply(2 * o + 1, m + 1, r, lz[o])
                lz[o] = 0

        def update(o, l, r, ql, qr, v):
            if ql <= l and r <= qr:
                apply(o, l, r, v)
                return
            push(o, l, r)
            m = (l + r) // 2
            if ql <= m:
                update(2 * o, l, m, ql, qr, v)
            if qr > m:
                update(2 * o + 1, m + 1, r, ql, qr, v)
            s[o] = s[2 * o] + s[2 * o + 1]
            q[o] = q[2 * o] + q[2 * o + 1]

        last = {}
        res = 0
        for j, x in enumerate(nums):
            p = last.get(x, -1)
            update(1, 0, n - 1, p + 1, j, 1)
            res += q[1]
            last[x] = j
        return res % (10**9 + 7)

class Solution(object):
    def minOperations(self, nums, x, k):
        n = len(nums)
        vals = sorted(set(nums))
        rank = {}
        for i, v in enumerate(vals):
            rank[v] = i + 1
        m = len(vals)
        cnt = [0] * (m + 1)
        sm = [0] * (m + 1)

        def add(i, c, v):
            while i <= m:
                cnt[i] += c
                sm[i] += v
                i += i & -i

        def prefix(i):
            c = 0
            s = 0
            while i > 0:
                c += cnt[i]
                s += sm[i]
                i -= i & -i
            return c, s

        top = 1
        while top * 2 <= m:
            top *= 2

        def kth(rem):
            pos = 0
            step = top
            while step:
                nxt = pos + step
                if nxt <= m and cnt[nxt] < rem:
                    pos = nxt
                    rem -= cnt[nxt]
                step >>= 1
            return pos + 1

        cost = [0] * (n - x + 1)
        total = 0
        for i in range(n):
            add(rank[nums[i]], 1, nums[i])
            total += nums[i]
            if i >= x:
                add(rank[nums[i - x]], -1, -nums[i - x])
                total -= nums[i - x]
            if i >= x - 1:
                r = kth(x // 2 + 1)
                med = vals[r - 1]
                cl, sl = prefix(r)
                cost[i - x + 1] = (med * cl - sl) + ((total - sl) - med * (x - cl))

        INF = float('inf')
        prev = [0] * (n + 1)
        for j in range(1, k + 1):
            cur = [INF] * (n + 1)
            for i in range(x, n + 1):
                best = cur[i - 1]
                cand = prev[i - x] + cost[i - x]
                cur[i] = cand if cand < best else best
            prev = cur
        return prev[n]


from bisect import bisect_left

class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        arr2.sort()
        m = len(arr2)
        res = 0
        for a in arr1:
            i = bisect_left(arr2, a)
            ok = True
            if i < m and arr2[i] - a <= d:
                ok = False
            if i > 0 and a - arr2[i - 1] <= d:
                ok = False
            if ok:
                res += 1
        return res


class Solution(object):
    def countServers(self, n, logs, x, queries):
        logs.sort(key=lambda l: l[1])
        order = sorted(range(len(queries)), key=lambda i: queries[i])
        cnt = [0] * (n + 1)
        active = 0
        lo = hi = 0
        m = len(logs)
        res = [0] * len(queries)

        for qi in order:
            q = queries[qi]
            while hi < m and logs[hi][1] <= q:
                s = logs[hi][0]
                if cnt[s] == 0:
                    active += 1
                cnt[s] += 1
                hi += 1
            while lo < hi and logs[lo][1] < q - x:
                s = logs[lo][0]
                cnt[s] -= 1
                if cnt[s] == 0:
                    active -= 1
                lo += 1
            res[qi] = n - active
        return res



import heapq

class Solution(object):
    def assignTasks(self, servers, tasks):
        free = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(free)
        busy = []  # (free_time, weight, index)
        ans = []
        t = 0

        for j, duration in enumerate(tasks):
            t = max(t, j)

            # If no server is free, wait for the earliest one to finish
            if not free:
                t = max(t, busy[0][0])

            # Release all servers that are free by time t
            while busy and busy[0][0] <= t:
                _, w, i = heapq.heappop(busy)
                heapq.heappush(free, (w, i))

            w, i = heapq.heappop(free)
            ans.append(i)
            heapq.heappush(busy, (t + duration, w, i))

        return ans


if __name__ == "__main__":
    print Solution().assignTasks([3, 3, 2], [1, 2, 3, 2, 1, 2])  # [2, 2, 0, 2, 1, 2]

