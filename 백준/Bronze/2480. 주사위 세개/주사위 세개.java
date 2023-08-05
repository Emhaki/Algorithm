import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.StringTokenizer;
import java.io.IOException;
 
public class Main {
 
	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		// 자르기
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		
		int a, b, c;
		// 하나씩 파싱
		a = Integer.parseInt(st.nextToken());
		b = Integer.parseInt(st.nextToken());
		c = Integer.parseInt(st.nextToken());

		// 3개가 다 다를경우
		if (a != b && b != c && c != a) {
			// 3개 중 가장 큰 수
			int max = Math.max(a, Math.max(b, c));
			System.out.println(max * 100);
		}
		// 3개가 다 같은경우
		else if (a == b && c == a) {
			System.out.println(10000 + a * 1000);
		}
		else if (a == b || a == c) {
			System.out.println(1000 + a * 100);
		}
		else {
			System.out.println(1000 + b * 100);
		}
	}
}