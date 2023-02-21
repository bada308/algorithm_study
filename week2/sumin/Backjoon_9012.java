package week2.sumin;

import java.io.*;
import java.util.Stack;

public class Backjoon_9012 {
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));

        int T=Integer.parseInt(br.readLine());

        for(int i=0;i<T;i++){
            String input=br.readLine();
            bw.write(isParenthesis(input));
            bw.write("\n");
        }
        bw.flush();
        br.close();
        bw.close();

    }

    private static String isParenthesis(String input) {
        Stack<Character>stack=new Stack<>();

        for(int i=0;i<input.length();i++){
            char c = input.charAt(i);

            //여는 괄호이면 스택에 넣는다.
            if(c=='(') {
                stack.push(c);
            }

            //닫는 괄호일 경우
            if(c==')'){
                if(stack.isEmpty()){
                    return "NO";
                }
                else{
                    stack.pop();
                }
            }
        }

        if(stack.isEmpty()){
            return "YES";
        }
        else{
            return "NO";
        }

    }
}
