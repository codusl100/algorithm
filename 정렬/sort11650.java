package sort;
import java.util.*;
public class sort11650 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int[][] xy = new int[N][2];
        int tmp = 0;
        int tmp2 = 0;

        for(int i = 0; i<N; i++){
            for(int j = 0; j<2; j++){
                xy[i][j] = sc.nextInt();

            }
        }

        Arrays.sort(xy, (x, y)->{
            if(x[0]==y[0]) {
                return x[1]-y[1];
            }
            else {
                return x[0]-y[0];
            }
        });


        for(int i = 0; i<N; i++){
            System.out.println(xy[i][0]+" "+xy[i][1]);

        }

    }
}
