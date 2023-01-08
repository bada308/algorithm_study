package stack;

import java.io.*;
import java.util.Stack;

public class Backjoon_10828 {
    private static Stack<Integer> integerStack = new Stack<>();
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        for (int i = 0; i < N; i++) {
            String[] input = br.readLine().split(" ");
            calculateStack(input);
        }

        bw.flush();
        bw.close();
        br.close();
    }

    private static void calculateStack(String[] input) throws IOException {
        String command = input[0];

        if (command.equals("push")) {
            integerStack.push(Integer.parseInt(input[1]));
        }

        if (command.equals("top")) {
            if (integerStack.size() != 0) {
                bw.write(String.valueOf(integerStack.peek()));
                bw.write("\n");
            } else {
                bw.write(String.valueOf(-1));
                bw.write("\n");
            }
        }

        if (command.equals("size")) {
            bw.write(String.valueOf(integerStack.size()));
            bw.write("\n");
        }

        if (command.equals("empty")) {
            if (integerStack.isEmpty()) {
                bw.write(String.valueOf(1));
                bw.write("\n");
            } else {
                bw.write(String.valueOf(0));
                bw.write("\n");
            }
        }

        if (command.equals("pop")) {
            if (integerStack.size() != 0) {
                bw.write(String.valueOf(integerStack.pop()));
                bw.write("\n");
            } else {
                bw.write(String.valueOf(-1));
                bw.write("\n");
            }

        }
    }
}
