package sort;
import java.util.*;

public class sort1181 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        String[] str = new String[N];
        for(int i=0; i<str.length; i++){
            str[i] = sc.next();
        }
        // Stream distinct()를 활용하여 중복 제거
        str = Arrays.stream(str).distinct().toArray(String[]::new);
        Arrays.sort(str, (String str1, String str2) -> {
                    if (str1.length() == str2.length()) {
                        return str1.compareTo(str2);
                    } else {
                        return str1.length() - str2.length();
                    }
                }
                );

        for(int i=0;i<str.length;i++){
            System.out.println(str[i]);
        }
    }
}
