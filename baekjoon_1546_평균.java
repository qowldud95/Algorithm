package test;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Test2 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();  //시험 본 과목의 개수
		double sum = 0;           //조작된 과목들의 sum
		
		ArrayList<Integer> currentScore = new ArrayList<>(); //현재성적
		
		for(int i = 0 ; i < N; i++) {
			currentScore.add(sc.nextInt());
		}
		
		ArrayList<Double> changeScore = new ArrayList<>();  //조작성적
		Collections.sort(currentScore); //정렬 : 최댓값 구하기 위해
		
		double M = currentScore.get(currentScore.size()-1); //자기점수중에 최댓값
		
		for(int i = 0; i < currentScore.size(); i++) {
			changeScore.add( currentScore.get(i) / M * 100 );
		} 
		for(int i = 0; i < changeScore.size(); i++) {
			sum += changeScore.get(i);
		}
		System.out.println(sum / N);
	}
}
