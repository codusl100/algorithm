// 카운팅 정렬
// arr 배열에 담겨 있는 값을 counting 배열의 인덱스에 해당하는 값을 증가시켜준다.
// 그냥 말 그대로 해당 숫자일 때 counting 원소값을 증가시켜주는 것이다.
package sort;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class sort10989 {
    public static void main(String[] args) throws IOException {
    Scanner sc = new Scanner(System.in);
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int arr[] = new int[N];
        StringBuilder sb = new StringBuilder();
        for(int i=0; i<N; i++){
            arr[i]=Integer.parseInt(br.readLine());
        }
        Arrays.sort(arr);
        for(int i=0;i<N;i++){
            sb.append(arr[i]).append('\n');
        }
        System.out.println(sb);


        /* int[] arr = new int[N];
        int[] counting = new int[N+1];
        int[] sorted = new int[N];
        for(int i = 0; i<arr.length;i++){
            arr[i]= sc.nextInt(); // arr에 입력
        }
        for(int i = 0; i<counting.length;i++) {
            counting[arr[i]]++;
        }
        // counting의 각 원소 값은 arr 값이 정렬되어 sorted 배열에 들어갈 인덱스 값이 된다.
        for(int i = 0; i<counting.length;i++) {
            counting[i] += counting[i-1];
        }
        for(int i = arr.length-1; i>=0;i--){
            int index = arr[i];
            counting[index]--;
            sorted[counting[index]]=index;
        } */

    }
}
