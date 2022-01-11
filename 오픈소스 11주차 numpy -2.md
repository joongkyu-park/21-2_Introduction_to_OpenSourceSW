# 오픈소스 11주차 numpy -2

2)
![오픈소스 11주차 numpy -2](images/오픈소스%2011주차%20numpy%20-2.png)

3)
universal function
ndarray안에 있는 데이터 원소별로 연산을 수행하는 함수.
하나의 스칼라 값을 받아와서 하나 이상의 스칼라 결과값을 고속으로 수행하는 벡터화 연산.

4)
binary function
두개의 인자를 갖는 ufucntion

5)
다수의 배열을 반환하는 ufunction도 존재
modf함수는 파이썬의 divmod함수와 같은 기능을 하는데
나눗셈 연산을 해서 몫 배열과 나머지 배열을 반환

6)
ufunction에는 out이라고하는 argument가 optional로 존재
out이 주어지면 결과가 out에 저장되고, out은 무조건 첫번째 인자와 같은 크기여야함.

9)
배열지향프로그래밍
numpy배열은 반복문을 사용하지않고 간결한 배열연산을 이용해서 많은 데이터처리를 한꺼번에 처리할 수 있다.
이렇게 반복문 없이 배열연산을 하는 것을 -> vectorization
일반적으로 numpy에서 vertorized된 배열의 대한 산술연산은, 파이썬 연산에 비해서 매우 빠르다(수십배~수백배)
따라서

