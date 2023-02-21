package week2.sumin;

import java.io.*;
import java.util.*;

public class Backjoon_1935 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        //피연산자의 개수
        int N = Integer.parseInt(br.readLine());

        //후위 표기식
        char[] array = br.readLine().toCharArray();

        Stack<Double> stack = new Stack<>();
        //피연산자와 실제 숫자 관계 맺기
        Map<Character, Double> map = new HashMap<>();

        //피연산자는 A부터 시작하고, N개의 피연산자를 갖는다.
        char key = 'A';
        for (int i = 0; i < N; i++) {
            map.put(key, Double.parseDouble(br.readLine()));
            key++;
        }
        //후위연산자의 개수만큼 반복한다.
        for (int j = 0; j < array.length; j++) {
            //대문자라면,그에 해당하는 값을 찾아서 스택에 넣는다.
            //대문자 아스키 코드 값... 뭐지
            if (array[j] >= 'A' && array[j] <= 'Z') {
                stack.push(map.get(array[j]));
            }

            //연산자라면 스택에서 피연산자 2개의 값을 꺼내서 연산을 한다.
            else {
                double second = stack.pop();
                double first = stack.pop();
                switch (array[j]) {
                    case '+':
                        stack.push(first + second);
                        break;
                    case '-':
                        stack.push(first - second);
                        break;
                    case '*':
                        stack.push(first * second);
                        break;
                    case '/':
                        stack.push(first / second);
                        break;
                }
            }
        }
        bw.write(String.valueOf(String.format("%.2f",stack.pop())));

        bw.flush();
        bw.close();
        br.close();
    }
}
