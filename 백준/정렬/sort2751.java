// 시간 제약 -> ArrayList.sort() 사용
package sort;
import java.util.*;
public class sort2751 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();
        int n = sc.nextInt();

        ArrayList<Integer> list = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            list.add(sc.nextInt());
        }

        Collections.sort(list);

        for(Integer x:list){
            sb.append(x).append("\n");
        }
        System.out.println(sb);

    }
}
/*
*
*
// BufferReader, BufferWriter 사용
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader; // byte 단위 데이터를 문자 단위 데이터로 처리할 수 있도록 변환환
iport java.io.OutputStreamWriter; // 문자열 처리 가능
import java.util.ArrayList;
import java.util.Collections;

...
BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

int N = Integer.parseInt(br.readLine());
ArrayList<Integer> arr = new ArrayList<>();
for(int i = 0; i<N; i++) {
    arr.add(Integer.parseInt(br.readline());
}

Collections.sort(arr);

StringBuilder sb = new StringBuilder();
for (int i = 0; i< N; i++){
    sb.append(arr.get(i) + "\n");
}
bw.flush();
bw.close();
br.close();
...
*
* */
