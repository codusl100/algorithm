package sort;
import java.util.*;

public class sort10814 {
    public static void main(String[] args){

        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        String[][] arr = new String[N][2];
        for(int i=0; i<N; i++){
            for(int j=0; j<2; j++){
                arr[i][j] = sc.next();
            }
        }

        Arrays.sort(arr, (x, y) ->{
            return Integer.parseInt(x[0]) - Integer.parseInt(y[0]);
        });
        for(int i=0;i<N;i++){
            System.out.println(arr[i][0]+" "+arr[i][1]);
        }

    }
}
