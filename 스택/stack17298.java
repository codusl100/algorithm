package stack;
import java.util.*;
public class stack17298 {

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        Stack<Integer> stack = new Stack<>(); // 첫번째 숫자보다 큰 수
        int[] seq = new int[n];	// 처음 입력받은 배열값
        // ex) 9 5 4 8

        for(int i = 0; i < n; i++) {
            seq[i] = sc.nextInt();
        }

        for(int i = 0; i < seq.length; i++) {
            while(!stack.empty() && seq[stack.peek()] < seq[i]) { // 스택 empty X & 스택 top이 현재 원소보다 작을 경우
                seq[stack.pop()] = seq[i]; // 해당 인덱스의 값을 현재 원소로 변경
            }

            stack.push(i); // 조건 해당 안하면 push
        }

        // 위 반복문이 끝나면 스택에 있는 모든 요소들을 pop하면서 -1로 초기화한다.
        while(!stack.empty()) {
            seq[stack.pop()] = -1;
        }
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < n; i++) {
            sb.append(seq[i]).append(' ');
        }

        System.out.println(sb);
    }
}
