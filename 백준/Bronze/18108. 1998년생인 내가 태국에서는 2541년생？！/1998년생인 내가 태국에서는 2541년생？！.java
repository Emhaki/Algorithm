import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
 
public class Main {
 
	public static void main(String[] args) throws IOException {
		     
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String year = br.readLine();
		int number = Integer.parseInt(year);

		System.out.println(number - 543);
	}
 
}