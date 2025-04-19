package practice;
import java.util.Scanner;

public class Solution2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int number = sc.nextInt();
        int answer = 0;
        
        System.out.println(String.valueOf(number).length()/2);
        
        for(int i = 0; number > 0; i++){
            System.out.println("==========");
            System.out.println(number);
            answer += number % 100;
            number /= 100;
        }
        System.out.println("정답");
        System.out.println(answer);
    }
}



