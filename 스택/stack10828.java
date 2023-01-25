package stack;
import java.util.*;


import java.io.*;

public class stack10828 {
    public static void main(String[] args) {
        ArrayList<Integer> arr = new ArrayList<>();
        StringBuilder sb = new StringBuilder();
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        for(int i=0; i<N; i++){
            String str = sc.next();
            if ("push".equals(str)) {
                arr.add(sc.nextInt());
            }
            if ("top".equals(str)){
                if(arr.size()==0){
                    sb.append(-1+"\n");
                }else {
                    sb.append(arr.get(arr.size() - 1)+"\n");
                }
            }
            if ("size".equals(str)){
                sb.append(arr.size()+"\n");
            }
            if ("empty".equals(str)){
                if(arr.size()==0){
                    sb.append(1+"\n");
                }
                else{
                    sb.append(0+"\n");
                }
            }
            if("pop".equals(str)){
                if(arr.size()==0){
                    sb.append(-1+"\n");
                }
                else {
                    int A = arr.get(arr.size()-1);
                    arr.remove(arr.size()-1);
                    sb.append(A+"\n");
                }
            }
        }
        System.out.print(sb);
    }
}