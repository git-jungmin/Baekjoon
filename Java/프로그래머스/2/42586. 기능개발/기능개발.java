import java.util.*;
class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        ArrayList<Integer> list = new ArrayList<>();
        
        // 초기화
        int dep = (int)Math.ceil((100 - progresses[0])/(float)speeds[0]);;
        int count = 1;
        
        for(int i = 1; i < progresses.length; i++){
            int d = (int)Math.ceil((100 - progresses[i])/(float)speeds[i]);
            
            if(d > dep){
                dep = d;
                list.add(count);
                count = 0;
            }
            count ++;
        }
        
        list.add(count);
        
        // 리스트 > 배열
        int[] answer = new int[list.size()];
        
        if (progresses.length == 0)
            answer[0] = 1;
        
        for(int i = 0; i < list.size(); i++){
            answer[i] = list.get(i);
        }
        
        return answer;
    }
}