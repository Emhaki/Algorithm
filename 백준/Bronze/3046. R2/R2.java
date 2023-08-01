import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.io.IOException;
 
public class Main {
 
	public static void main(String[] args) throws IOException {

		Scanner sc = new Scanner(System.in);
		int R1 = sc.nextInt();
		int S = sc.nextInt();

		int R2 = (S * 2) - R1;
		System.out.println(R2);
	}
 
}