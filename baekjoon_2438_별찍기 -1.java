package test;

import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		for (int j = 0; j < N; j++) {
			for (int i = 0; i <= j; i++) {
				System.out.print("*");
			}
			System.out.println();
		}
	}

}
