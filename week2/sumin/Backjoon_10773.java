package week2.sumin;


import java.io.*;
import java.util.Stack;

public class Backjoon_10773 {
    private static Stack<Integer> stack = new Stack<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int K = Integer.parseInt(br.readLine());

        for (int i = 0; i < K; i++) {
            makeStack(Integer.parseInt(br.readLine()));
        }

        bw.write(String.valueOf(calculateSum()));

        bw.flush();
        bw.close();
        br.close();
    }

    //입력받은 숫자를 기반으로 stack 만들기
    private static void makeStack(int num) {
        if (num != 0) {
            stack.push(num);
        } else {
            stack.pop();
        }
    }

    //stack의 값 계산하기
    private static int calculateSum() {
        int sum = 0;
        int stackSize=stack.size();
        for (int i = 0; i < stackSize; i++) {
            sum+=stack.pop();
        }
        return sum;
    }
}
