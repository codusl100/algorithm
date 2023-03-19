package stack;

import java.util.ArrayList;
import java.util.Scanner;
import java.util.Stack;

public class stack1874 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        Stack<Integer> stack = new Stack<>();
        ArrayList<String> str = new ArrayList<>();
        int[] arr = new int[n];
        int m = 0;

        for(int i = 0; i < n ; i ++) {
            arr[i] = sc.nextInt(); // 4 3 6 8 7 5 2 1
        }
        for (int i = 1; i <= n; i++) {
            stack.push(i); // 1 2 3 4 5 6 7 8
            str.add("+");
            while (!stack.empty()) {
                if(stack.peek() == arr[m]) {
                    stack.pop();
                    str.add("-");
                    m++;
                }
                else{
                    break;
                }
            }
        }


        if (!stack.isEmpty()) {
            System.out.println("NO");
        } else {
            for (String st : str) {
                System.out.println(st);
            }
        }
    }
}
