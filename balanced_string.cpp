class Solution {
public:
    int balancedStringSplit(string s) {
        int r_counter = 0;
        int l_counter = 0;
        int total_count = 0;
        
        for(int i = 0;i<s.length();i++){
            if(s[i]=='R'){
                r_counter++;
            }
            else{
                l_counter++;
            }
            if(r_counter == l_counter){
                total_count++;
            }
            }
        return total_count;
        }
        
    };
