package queue;

import java.io.IOException;
import java.util.LinkedList;
import java.util.Scanner;

public class queue11866 {
    public static void main(String[] args) throws IOException {
        LinkedList<Integer> q = new LinkedList<>();
        Scanner sc = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();

        int N = sc.nextInt(); // 7
        int K = sc.nextInt(); // 3

        sb.append("<");

        for (int i = 1; i <= N; i++) {
            q.add(i);
        }

        while (q.size() != 1) {
            for(int i = 0; i < K - 1; i++){
                q.add(q.poll());
            }
                sb.append(q.poll()+", ");
        }

        sb.append(q.poll()+">");

        System.out.println(sb);
    }
}