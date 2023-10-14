class Solution {
public:
    int strStr(string haystack, string needle) {
        
        string myString = "";

        //Loop through the haystack starting from neeldeSize index.
        for (int i = needle.length(); i <= haystack.length(); i++) {
            //Construct a string from the haystack
            for (int j = needle.length(); j > 0; j--) {
                myString += haystack[i - j];
            }
           
            //Check if string matches needle, return index if it does
            if (myString == needle) {
                return i - needle.length();
            }
            myString = "";
        }
        //If the loop exits, return -1
        return -1;
    }
};