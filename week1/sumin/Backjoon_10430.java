import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

class Backjoon_10430{
    public static void main(String[]args)throws IOException{
        BufferedReader bf=new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st=new StringTokenizer(bf.readLine()," ");
        
        int a=Integer.parseInt(st.nextToken());
        int b=Integer.parseInt(st.nextToken());
        int c=Integer.parseInt(st.nextToken());
       
        bw.write((a+b)%c+"\n");
        bw.write(((a%c)+(b%c))%c+"\n");
        bw.write((a*b)%c+"\n");
        bw.write(((a%c)*(b%c))%c+"\n");

        bw.flush();
        bw.close();
    }
}