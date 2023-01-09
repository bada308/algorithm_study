import java.io.*;
import java.util.Stack;

public class Backjoon_1406 {
    public static void main(String[] args) throws IOException {
        //커서를 기준으로 왼쪽스택, 오른쪽 스택으로 구분함
        Stack<String> leftStack = new Stack<>();
        Stack<String> rightStack = new Stack<>();
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        //초기값은 다 커서보다 왼쪽에 있으니깐 leftStack에 넣기
        String[] array = br.readLine().split("");
        for (int i = 0; i < array.length; i++) {
            leftStack.push(array[i]);
        }

        // 입력할 명령어의 개수
        int M = Integer.parseInt(br.readLine());

        //명령어 실행
        for (int i = 0; i < M; i++) {
            String[] input = br.readLine().split(" ");
            String command = input[0];
            switch (command) {
                case "P":
                    leftStack.push(input[1]);
                    break;
                case "D":
                    if(!rightStack.isEmpty()){
                        leftStack.push(rightStack.pop());
                    }
                    break;
                case "L":
                    if(!leftStack.isEmpty()){
                        rightStack.push(leftStack.pop());
                    }
                    break;
                case "B":
                    if(!leftStack.isEmpty()){
                        leftStack.pop();
                    }
                    break;
            }
        }

        //왼쪽 스택에 있는 문자열을 오른쪽 스택으로 올린다.
        while (!leftStack.isEmpty()) {
            rightStack.push(leftStack.pop());
        }

        //오른쪽 스택에 있는 값을 하나씩 pop해서 문자열을 만든다.
        while (!rightStack.isEmpty()) {
            sb.append(rightStack.pop());
        }

        bw.write(String.valueOf(sb));

        bw.flush();
        bw.close();
        br.close();
    }

}
