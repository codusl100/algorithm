package stack;

import java.util.Scanner;
import java.util.Stack;

public class stack4949 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();

        Stack<Character> str = new Stack<>();


        while (true) {
            String a = sc.nextLine();
            if(a.equals(".")) {
                break;
            }

            for (int i = 0; i < a.length(); i++) {
                char word = a.charAt(i);
                if (word == '(' || word == '[') {
                    str.push(word);
                } else if (word == ')') {
                    if (str.isEmpty() || str.peek() != '(') {
                        str.push(word);
                    } else
                        str.pop();
                } else if (word == ']') {
                    if (str.isEmpty() || str.peek() != '[') {
                        str.push(word);
                    } else
                        str.pop();
                }
            }
                if (str.empty()) {
                    sb.append("yes\n");
                } else {
                    sb.append("no\n");
                }
                str.clear();
            }

            System.out.print(sb);
        }
    }

