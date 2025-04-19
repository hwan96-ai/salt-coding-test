class Solution {
    public int solution(int n, int w, int num) {
        int answer = 1;
        
        /* 전체 택배 상자 셋팅 */
        int row = n / w;
        // 나머지가 있을경우 한줄 추가
        if (n % w != 0 ){
            row += 1;
        } 

        /* 입력된 상자 처리 */

        int first_row = num / w ; // 첫번째 행
        int first_column = num % w; // 첫번째 열
        
        int curr_num = num;

        // 나머지가 없는경우 마지막 수를 의미
        if (first_column != 0){
            first_row += 1;
        }else{
            // 나머지가 0이면 각 행의 w번재 수
            first_column = w;
        }

        //짝수일 경우 
        if (first_row % 2 == 0){
            first_column = w - first_column + 1;
        }


        for(int i = first_row; i < row ; i++){
            //현재 줄이 홀수일경우 왼 -> 오른쪽으로 숫자 증가
            if(i % 2 != 0){
                curr_num = (w - first_column) * 2 + curr_num + 1;
            }else{
                curr_num = (first_column-1) * 2 + curr_num + 1;
            }
            // 현재 추적적인 박스 숫자가 전체 n개를 넘을경우 
            if (curr_num > n){
                break;
            }
            answer+=1;
        }

        
        return answer;
    }
}