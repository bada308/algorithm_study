# 스트림(Stream)

### 스트림이란?
---

스트림은 데이터의 이동 흐름이다.

즉, A수도관에서 B수도관으로 이동하는 물의 흐름이라고 할 수 있다.

프로그래밍에서는 다음과 같은 것들을 스트림이라고 한다.

- HTTP 응답 데이터(브라우저가 요청하고 서버가 응답하는 HTTP 응답 데이터)

<img width="675" alt="스크린샷 2023-01-07 오후 12 39 02" src="https://user-images.githubusercontent.com/88534959/211129615-8e934752-3f4b-4ce9-aa68-e91fb3f5aef0.png">


용도에 따라 입력 스트림(InputStream), 출력 스트림(OutputStream)으로 나뉜다.

```java
BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
```

### InpuStream
---

바이트 단위로 데이터를 처리한다.

```java
import java.io.IOException;
import java.io.InputStream;

public class StreamTest {
    public static void main(String[] args) throws IOException {
        InputStream in=System.in;

        int a;
        a=in.read();

        System.out.println(a);
        
    }
}
```

read()메서드는 1Byte의 int 자료형으로 값을 받는다.

이 int값은 아스키코드 값이기 때문에 숫자를 입력해도 아스키 코드 값으로 출력된다.

```java
1 //입력값
49 //출력값
```

또한, System.in의 타입도 InputStream이다.
<img width="592" alt="스크린샷 2023-01-07 오후 12 12 47" src="https://user-images.githubusercontent.com/88534959/211129556-ae1140a7-d33e-46f9-9b41-e2c954342cab.png">

이 방법만으로는 문자를 받기 힘드니 InputStreamReader를 사용해서 바이트 단위 데이터를 문자 단위로 처리할 수 있게하였다.

### InputStreamReader
---

문자(Character) 단위로 데이터를 처리한다.

InputStream의 데이터를 문자로 변환하는 중개 역할을 한다.

```java
InputStreamReader reader = new InputStreamReader(new InputStream);
```

InputStreamReader은 InputStream 객체를 입력으로 가지고 있어야 한다.
<img width="515" alt="스크린샷 2023-01-07 오후 12 17 28" src="https://user-images.githubusercontent.com/88534959/211129568-27195f96-1456-4922-a4f2-87cea652e819.png">

### BufferedReader
---
버퍼를 두어 문자를 버퍼에 일정 정도 저장해둔 뒤 한 번에 보낸다.

```java
BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
```

```java
InputStream inputstream = System.in;
InputStreamReader sr = new InputStreamReader(inputstream);
BufferedReader br = new BufferedReader(sr);
```

1. **바이트 단위**로 데이터를 처리하는 InputStream를 통해서 데이터를 입력받는다.,
2. 바이트 단위 데이터를 **문자(Character) 단위**로 처리하기 위해서 InputStreamReader로 감싸준다.
3. 버퍼(Buffer)를 이용해 입력받은 문자를 쌓아둔 뒤 한 번에 **문자열(String)**로 보낸다.

[System.in](http://System.in) == InputStream → InputStreamReader → BufferedReader

바이트 단위 → Char 단위 → String 단위