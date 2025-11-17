class Solution {
public:
    char getMaxOccuringChar(string& s) {
        int freq[26] = {0};  // Frequency array for lowercase letters

        for (int i = 0; i < s.length(); i++) {
            char ch = s[i];
            if (ch >= 'a' && ch <= 'z') {
                freq[ch - 'a']++;
            } else if (ch >= 'A' && ch <= 'Z') {
                freq[ch - 'A']++;
            }
        }

        int maxi = -1, ans = 0;
        for (int i = 0; i < 26; i++) {
            if (freq[i] > maxi) {
                maxi = freq[i];
                ans = i;
            }
        }

        return 'a' + ans;
    }
};