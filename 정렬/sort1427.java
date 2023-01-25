package sort;
import java.io.IOException;
import java.util.*;

public class sort1427 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
		
		String str = sc.next();
		String[] arr = str.split("");
		Integer[] arr2 = new Integer[str.length()];
		for(int i = 0; i < arr.length;i++) {
			arr2[i] = Integer.parseInt(arr[i]);
		}
		
		Arrays.sort(arr2, Collections.reverseOrder());
		for(int i=0; i<arr2.length;i++) {
			System.out.print(arr2[i]);
		}
    }
}

//이전에 했던 것!
// Scanner sc = new Scanner(System.in);
//         String str = sc.next();
//         int arr[] = new int[str.length()];


//         for (int i = 0; i < arr.length; i++) {
//             arr[i] = str.charAt(i) - '0';
//         }
//         for (int i = 0; i < arr.length-1; i++) {
//             for(int j = i; j < arr.length; j++){
//                 if(arr[i]>arr[j]) {
//                     int temp = arr[j];
//                     arr[j] = arr[i];
//                     arr[i] = temp;
//                 }
//             }
//         }

//         for(int i = 0; i < arr.length; i++){
//             System.out.print(arr[i]);
//         }

/*
* 더 간단하게
*
* BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
* char[] ch = br.readLine().toCharArray();
* //오름차순 정렬
* Arrays.sort(ch);
* //역순으로 출력
* for(int i=ch.length-1;i>=0;i--){
* System.out.print(ch[i]);
* }
*/
