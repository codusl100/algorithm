package stack;
import java.io.*;
import java.util.*;

public class stack9012 {
    public static void main(String[] args) throws Exception {

        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();

        StringBuilder sb = new StringBuilder();
        Stack<Character> stack = new Stack<>();

        for(int i=0; i<N; i++){
            String str = sc.next();
            for(int j=0; j<str.length(); j++){
                char ch = str.charAt(j);
                if(ch == '(') {
                    stack.push(ch);
                }
                else {
                    if(stack.size()==0){
                        stack.push(ch);
                        break;
                    }
                    else {
                        stack.pop();
                    }
                }
            }
            if(stack.isEmpty()) {
                sb.append("YES\n");
            }
            else{
                sb.append("NO\n");
            }
            stack.clear();
        }
    System.out.print(sb);
    }
}
