class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.empty()) { //No unique elements
            return 0;
        }

        int k = 1; //Initialize the count of unique elements to 1

        //Loop from the second element (index 1);
        for ( int i = 1; i < nums.size(); i++) {
            if (nums[i] != nums[i-1]) { //Check if consecutive numbers are not equal
                nums[k] = nums[i]; //Overwrite the next unique element
                k++;
            }
        }

        return k;
    }
};