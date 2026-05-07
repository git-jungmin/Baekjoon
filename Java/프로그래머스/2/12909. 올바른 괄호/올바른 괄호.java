class Solution {
    boolean solution(String s) {
        int find = 0;
        int n = s.length();
        
        for(int i = 0; i < n; i++){
            
            if(s.charAt(i) == '(')
                find ++;
            else
                find --;
            
            if(find < 0)
                return false;
        }
        
        return find == 0;
    }
}   