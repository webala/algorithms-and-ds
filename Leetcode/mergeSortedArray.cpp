#include <vector>
using namespace std;

class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        // Slice nums1 one to remain with m element
        int endIndex = m;
        vector<int> slicedArr;
        for (int i = 0; i < endIndex; i++) {
            slicedArr.push_back(nums1[i]);
        }
        cout << "sliced nums1 \n";
        for (int element: slicedArr) {
            cout << element << endl;
        }
        // add nums2 to nums1
        int i = 0;
        for (int j = 0; j < n; j++) {
            slicedArr.push_back(nums2[j]);
        }

        cout << "Added nums2 to sliced arr \n";

        for (int element: slicedArr) {
            cout << element << endl;
        }

        // sort the array.
        cout << "sorted sliced arr: \n";
        sort(slicedArr.begin(), slicedArr.end());
        for (int element: slicedArr) {
            cout << element << endl;
        }

        nums1 = slicedArr;
    }
};