package week2.sumin;

import java.io.*;
import java.util.*;

public class Backjoon_18528 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();
        Deque<Integer> deq = new LinkedList<>();

        int num = Integer.parseInt(br.readLine());

        for (int i = 0; i < num; i++) {
            String[] command = br.readLine().split(" ");
            switch (command[0]) {
                case "push":
                    deq.add(Integer.parseInt(command[1]));
                    break;
                case "pop":
                    sb.append(deq.isEmpty() ? "-1" : deq.poll());
                    sb.append("\n");
                    break;
                case "size":
                    sb.append((deq.size()));
                    sb.append("\n");
                    break;
                case "empty":
                    sb.append(deq.isEmpty() ? 1 : 0);
                    sb.append("\n");
                    break;
                case "front":
                    sb.append(deq.isEmpty() ? "-1" : String.valueOf(deq.peekFirst()));
                    sb.append("\n");
                    break;
                case "back":
                    sb.append(deq.isEmpty() ? -1 : deq.peekLast());
                    sb.append("\n");
                    break;
            }

        }
        bw.write(String.valueOf(sb));
        bw.flush();

        bw.close();
        br.close();
    }

}
