class Solution {
    public int[] solution(int[] sequence, int k) {
        int len = sequence.length;
        int[] answer = {0,len};
        int start = 0;
        int end = 0;
        int total = sequence[0];
        
        while(end < len) {
            if(total == k){
                if(answer[1] - answer[0] > end - start){
                    answer[0] = start;
                    answer[1] = end;
                }
                
                total -= sequence[start];
                start ++;
            } else if(total < k) {
                end ++;
                if(end < len)
                    total += sequence[end];
            } else {
                total -= sequence[start];
                start ++;
            }
        }
        return answer;
    }
}