package queue;
import java.io.*;
import java.util.*;

public class queue18258 {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        LinkedList<Integer> q = new LinkedList<>();
        int N = Integer.parseInt(br.readLine()); // 큐 크기
        StringBuilder sb = new StringBuilder();
        StringTokenizer com;

        while(N --> 0){
            com = new StringTokenizer(br.readLine(), " ");
            switch(com.nextToken()) {
                case "push":
                    q.offer(Integer.parseInt(com.nextToken()));
                    break;
                case "back":
                    if (q.size() == 0) {
                        sb.append(-1 + "\n");
                    } else {
                        sb.append(q.peekLast() + "\n");
                    }
                    break;
                case "size":
                    sb.append(q.size() + "\n");
                    break;
                case "empty":
                    if (q.isEmpty()) {
                        sb.append(1 + "\n");
                    } else {
                        sb.append(0 + "\n");
                    }
                    break;
                case "pop":
                    if (q.size() == 0) {
                        sb.append(-1 + "\n");
                    } else {
                        int A = q.poll();
                        sb.append(A + "\n");
                    }
                    break;
                case "front":
                    if (q.size() == 0) {
                        sb.append(-1 + "\n");
                    } else {
                        sb.append(q.peek() + "\n");
                        break;

                    }
            }

        }
        System.out.print(sb);


    }
}
