package test;

public class Main {
	public static void main(String[] args) {
		
		String[] seoul = {"Jin","Kim"};
		
		String answer = "";
		
		for (int i = 0; i < seoul.length; i++) {
			if (seoul[i].equals("Kim")) {
				answer = "김서방은 " + i + "에 있다";
			}
		}
		System.out.println(answer);
		
	}
}