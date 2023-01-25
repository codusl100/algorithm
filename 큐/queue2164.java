package queue;

import java.io.IOException;
import java.util.*;

public class queue2164 {
    public static void main(String[] args) throws IOException {
        LinkedList<Integer> q = new LinkedList<>();
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        for(int i=1; i<=N; i++){
            q.add(i);
        }

        while(q.size()!=1) {q.remove();
                q.add(q.peek());
                q.remove();
            }

        System.out.print(q.peek());
    }
}
