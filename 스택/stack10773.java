package stack;

import java.util.*;

public class stack10773 {
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		
		ArrayList<Integer> arr = new ArrayList<Integer>();
		
		for(int i=0; i<n; i++) {	
			int enter = sc.nextInt();
			if(arr.isEmpty()) {
				if(enter != 0) {
					arr.add(enter);
				}
			}
			else {
				if(enter != 0) {
					arr.add(enter);
				}
				else {
					arr.remove(arr.size()-1);
				}
			}
			
		}
		
		int sum = 0;
		for(int i=0; i<arr.size(); i++) {
			sum += arr.get(i);
		}
		System.out.println(sum);
}
}
