package sort;
import java.util.*;

public class sort18870 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = sc.nextInt();
        }
        int[] arr2 = arr.clone();

        Arrays.sort(arr2);

        Map<Integer, Integer> map = new HashMap<>();
        int id = 0;
        for(int n : arr2){
            if(!map.containsKey(n))
                map.put(n, id++);
        }
//        for(int n : arr) { // 좌표 순위 출력
//            System.out.print(map.get(n)+" ");
//        }
        StringBuilder sb = new StringBuilder();
        for(int key : arr) {
            int ranking = map.get(key);	// 원본 배열 원소(key)에 대한 value(순위)를 갖고온다.
            sb.append(ranking).append(' ');
        }

        System.out.println(sb);

    }
}
