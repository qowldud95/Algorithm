package test;

import java.util.HashSet;
import java.util.Scanner;

//백준 나머지 hashSet으로 풀기..

public class Test14 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		HashSet<Integer> h = new HashSet<Integer>();
		
		for(int i=0; i<10; i++) {
			h.add(sc.nextInt() % 42);  // 중복이 있을 경우 add 하지 않고 무시한다
		}
		sc.close();
		System.out.print(h.size());
	}
}
