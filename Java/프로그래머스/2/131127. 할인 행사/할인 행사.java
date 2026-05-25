import java.util.*;
class Solution {
    public int solution(String[] want, int[] number, String[] discount) {
        int answer = 0;
        
        for(int i = 0; i <= discount.length - 10; i++){
            Map<String, Integer> map = new HashMap<>();
            
            for(int j = i; j < i + 10; j++){
                if(!map.containsKey(discount[j]))
                    map.put(discount[j],0);
                map.put(discount[j], map.get(discount[j]) + 1);
            }
            
            boolean check = true;
            
            for(int k = 0; k < want.length; k++){
                if(number[k] != map.getOrDefault(want[k],0)){
                    check = false;
                    break;
                }
            }
            if(check)
                answer++;
        }
        return answer;
    }
}