# 오픈소스 12주차 - pandas

판다스 - 데이터 처리에 중점
넘파이 - 배열 계산에 중점

2번째 강의
11)
inplace=True를 넣어줘야 원본객체에 변화 있음.
이걸 넣어주지 않으면 그저 출력결과에서만 drop된 결과를 보여줌(원본에는 변경x)

19)
![오픈소스 12주차 - pandas](images/오픈소스%2012주차%20-%20pandas.png)

integer타입으로 indexing이 된 경우,
label-based indexing을 부른건지, integer indexing을 부른건지 모호하므로 error를 반환.

아래와 같이 integer가 아닌 타입으로 indexing한 경우 모호하지 않으므로 error발생 x

20)
따라서 정수로 인덱싱한 경우
라벨인덱싱을 원할경우 -> loc
정수인덱싱을 원할경우 -> iloc

21)
객체간 산술연산
db에서 아우터 조인과 유사

매칭되는 값끼리 연산
![오픈소스 12주차 - pandas-1](images/오픈소스%2012주차%20-%20pandas-1.png)

missing value가 전파된다

23)
공통되는 컬럼이 없는 경우

25)
nan을 채워주기 위해서 add 메서드 사용

26)
각각의 산술연산은 r로 시작하는 짝궁 메서드를 가진다
![오픈소스 12주차 - pandas-2](images/오픈소스%2012주차%20-%20pandas-2.png)

27)
시리즈와 데이터프레임 간의 산술연산
시리즈는 1차원 배열, 데이터프레임은 2차원 배열이라고 볼 수 있다.
따라서 1차원 배열과 2차원 배열간의 연산
numpy에서의 broadcasting과 같다고 볼 수 있다.

31)
판다스 객체에 함수를 사용하는법
numpy의 ufunc을 사용할 수 있다

38)
![오픈소스 12주차 - pandas-3](images/오픈소스%2012주차%20-%20pandas-3.png)

 
—————

3번째 강의

3)
Reductions
시리즈, 데이터프레임의 로우나 컬럼으로부터 생성된 시리즈 객체로부터 하나의 값을 추출하기 위한 메소드
기본적으로 NaN은 무시하고 연산진행
4)
NaN을 연산에 포함시키고싶으면 skipna=False 사용

 5)
describe 메소드 -> summary statistics에 가장 가깝다
non-numeric data와 numeric data가 다른 요약통계!

non-numeric data
count : 총원소의 개수
unique : 유일한 원소 개수
top : 가장 많이 나오는 원소
freq : 가장 많이 나오는 원소의 개수

numeric data
count : Nan이 아닌 숫자의 개수
mean : Nan이 아닌 값의 평균
std : 표준편차
min , max : 최소, 최대값
25,50,75%: : 해당 시리즈에서의 분위수

7)
Correlation : 상관과계
Covariance : 공분산
-> 이를 계산하기 위해선 두 쌍의 데이터 필요

10)
이 함수들의 특징은 1차원 시리즈에 담긴 값의 정보를 추출하는 메소드라는 점

