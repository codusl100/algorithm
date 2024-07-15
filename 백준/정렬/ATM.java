import java.util.*;
import java.util.Arrays;

public class ATM {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] A = new int[N];
        int[] S = new int[N];
        int sum = 0;

        for (int i = 0; i < N; i++) {
            A[i] = sc.nextInt();
        }
        Arrays.sort(A);
        S[0] = A[0];
        for (int i = 1; i < N; i++) {
            S[i] = S[i-1] + A[i];
        }
        for (int i = 0; i < N; i++) {
            sum += S[i];
        }
        System.out.println(sum);
    }
}

