import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

class BackJoon_3033{
    public static void main(String[] args) throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        String input=br.readLine();
        StringTokenizer st=new StringTokenizer(input," ");
        BufferedWriter bw= new BufferedWriter(new OutputStreamWriter(System.out));
        int king = Integer.parseInt(st.nextToken());
        int queen=Integer.parseInt(st.nextToken());
        int rook=Integer.parseInt(st.nextToken());
        int bishop=Integer.parseInt(st.nextToken());
        int knight=Integer.parseInt(st.nextToken());
        int pawn=Integer.parseInt(st.nextToken());

        bw.write(Integer.toString(1-king)+" ");
        bw.write(Integer.toString(1-queen)+" ");
        bw.write(Integer.toString(2-rook)+" ");
        bw.write(Integer.toString(2-bishop)+" ");
        bw.write(Integer.toString(2-knight)+" ");
        bw.write(Integer.toString(8-pawn)+" ");

        bw.flush();
        bw.close();
    }
}