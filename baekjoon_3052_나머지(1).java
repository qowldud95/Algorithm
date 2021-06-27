package test;

import java.util.Scanner;

//백준 나머지 3052
public class Test13 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int[] x = new int[10]; // 입력받은 값의 나머지를 넣을 배열
		int answer = 0;        // 서로 다른 나머지가 몇개있는지

		for (int i = 0; i < 10; i++) {
			x[i] = sc.nextInt() % 42; 
		}
		
		for (int i = 0; i < 10; i++) {
			int temp = 0;      //같은 값이 있을 때 temp에 값을담아줌
			for (int j = i + 1; j < 10; j++) {
				if (x[i] == x[j]) {
					temp ++;
				}
			}
			if(temp == 0) {    //temp가 0이면 같은값이 없다는 뜻
				answer++;
			}
		}
		
		System.out.println("answer : " + answer);
	}
}
