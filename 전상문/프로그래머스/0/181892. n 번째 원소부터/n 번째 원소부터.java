class Solution {
    public int[] solution(int[] num_list, int n) {
        int n_idx = n - 1;
        int[] answer = new int[num_list.length - n_idx]; //
        for(int i = 0; i < num_list.length - n_idx ; i++){
            answer[i] = num_list[n_idx+i]; //인덱스는 0부터 시작하므로 
        }
        return answer;
    }
}