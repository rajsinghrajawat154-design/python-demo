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
