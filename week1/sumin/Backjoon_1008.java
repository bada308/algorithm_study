import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Backjoon_1008 {
    public static void main(String[]args)throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        String str=br.readLine();
        StringTokenizer st=new StringTokenizer(str," ");
        int A=(int) Double.parseDouble(st.nextToken());
        int B=(int) Double.parseDouble(st.nextToken());
        
        System.out.println(A/B);
    }
}
