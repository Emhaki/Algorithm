import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main{
    public static void main(String[]args) throws IOException {
        
        try {
            InputStreamReader i_num = new InputStreamReader (System.in);
            BufferedReader s_br = new BufferedReader(i_num);
            
            String text[] = s_br.readLine().split(" ");
            int a = Integer.parseInt(text[0]);
            int b = Integer.parseInt(text[1]);
            
            System.out.println(a+b);
            
        }
        catch(IOException e) {
            
        }
    }
}