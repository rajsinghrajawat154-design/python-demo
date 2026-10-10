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
