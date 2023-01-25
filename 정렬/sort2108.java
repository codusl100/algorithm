package sort;

import java.io.IOException;
import java.lang.reflect.Array;
import java.util.*;

public class sort2108 {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int arr[] = new int[N];
        int counting[] = new int[8001]; // -4000 ~ 4000 까지 나온 개수 세는 배열
        Random rd = new Random();
        int sum = 0;
        double ans1 = 0;
        int ans2 = 0;
        int ans3 = 0;
        int ans4 = 0;

        // 산술평균 : N개의 수들의 합을 N으로 나눈 값
        for(int i = 0 ; i<N; i++){
            arr[i]=sc.nextInt(); // 절댓값 4000까지 범위
            sum+=arr[i];
        }
        ans1 = Math.round((double)sum / N);

        Arrays.sort(arr);

        // 중앙값 : N개의 수들을 증가하는 순서대로 나열했을 경우 그 중앙에 위치하는 값
        ans2 = arr[N/2];

        // 최빈값 : N개의 수들 중 가장 많이 나타나는 값
        int count = 0;
        int max = -1;
        int mod = arr[0];
        boolean check = false;

        for(int i = 0; i< N-1; i++) {
            if (arr[i] == arr[i+1]) {
                count++;
            }
            else{
                count = 0;
            }
            if (count > max){
                max = count;
                mod = arr[i];
                check = true;
            }
            else if(max == count && check == true){ // 이전에 한번 최빈값이었었음
                mod = arr[i]; // 이걸 최종 최빈값으로 (문제에서 두번째로 작은 값을 최빈값으로)
                check = false; // 다음에 같은 최빈값 나오더라도 false 처리 되어서 다음 if로 넘어감!!
            }
        }

        // 범위 : N개의 수들 중 최댓값과 최솟값의 차이
        ans4 = arr[N-1]-arr[0];

        System.out.println((int)ans1);
        System.out.println(ans2);
        System.out.println(mod);
        System.out.println(ans4);
    }
}
