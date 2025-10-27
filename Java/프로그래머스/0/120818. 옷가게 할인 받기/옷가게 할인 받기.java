class Solution {
    public int solution(int price) {
        double disc = 0;
        if (price >= 500000) {
            disc = 0.80;
        }
        else if (price >= 300000) {
            disc = 0.90;
        }
        else if (price >= 100000) {
            disc = 0.95;
        }
        else {
            return price;
        }
        return (int)(price * disc);
    }
}