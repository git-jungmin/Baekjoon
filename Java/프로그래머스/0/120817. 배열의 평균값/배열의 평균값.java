class Solution {
    public double solution(int[] numbers) {
        double sum = 0;
        for (int n : numbers){
            sum += n;
        }
        return (float)sum / numbers.length;
    }
}