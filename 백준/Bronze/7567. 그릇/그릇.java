import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.StringTokenizer;
import java.io.IOException;
 
public class Main {
 
	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		// 자르기
		String s = br.readLine();
		int height = 10;
		for (int i = 1; i <s.length(); i++) {
			if (s.charAt(i) == s.charAt(i-1)) {
				height += 5;
			} else {
				height += 10;
			}
		}
		System.out.println(height);

	}
}