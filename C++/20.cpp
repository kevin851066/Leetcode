class Solution {
public:
    bool isValid(string s) {
        '''
        :type: s: str
        :rtype: bool
        '''
        map<char, char> par_map = {{'(', ')'}, {'{', '}'}, {'[', ']'}};
        stack<char> stk; 
        for (int i = 0; i < s.length(); i++) {
            if (s[i] == '(' || s[i] == '{' || s[i] == '[') 
                stk.push(s[i]);
            else { // close par
                if (stk.empty()) // no corresponding par 
                    return false;
                else {
                    if (s[i] != par_map[stk.top()])
                        return false;
                    else 
                        stk.pop();
                }
            }
        }
        return stk.empty();
    }
};