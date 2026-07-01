class Solution {
public:
    int characterReplacement(string s, int k) {


        int res=0;
        int l, maxf=0;
        unordered_map<char,int> cnt;

        for(int r=0;r<s.size();r++){
            cnt[s[r]]++;
            maxf = max(maxf, cnt[s[r]]);

            if((r-l+1)- maxf>k){
                
                cnt[s[l]]--;
                l++;
               
            }
             res= max(res, (r-l+1) );


        
           
        }

        return res;
        
    }
};
