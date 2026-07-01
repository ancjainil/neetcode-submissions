class Solution {
public:
    int maxProfit(vector<int>& prices) {

        int maxProf=0;

        int l=0;
        int r=1;

        while(r<prices.size()){
            if(prices[l]< prices[r]){
                int currprof= prices[r]-prices[l];
                maxProf = max( maxProf, currprof);
            }
            else{
                l=r;
            }

            r++;
        }

        return maxProf;


        
    }
};
