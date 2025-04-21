class Solution {
    public int solution(String num_str) {
        int answer = 0;
        char[] arr = num_str.toCharArray();
        for(char tmp : arr){
            answer += Character.getNumericValue(tmp);
        }
        
        return answer;
    }
}