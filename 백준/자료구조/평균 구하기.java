package 백준.자료구조;

public class 평균 구하기 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int A[] = new int[N];
        
        for (int i = 0; i < N; i++) {
            A[i] = sc.nextInt();
        }

        long sum = 0;
        long max = 0;

        for (int i = 0; i < N; i++) {
            if (A[i] > max) max = A[i];
            sum += A[i];
        }

        System.out.prinln(sum * 100.0 / max / N);
    }
}
