# 이예준 202030227

5월 1일 강의



4월 17일 강의

훅이란 무엇인가
- 클래스형 컴포넌트에서는 생성자에서 state를 정의하고 setState() 함수를 통해 state를 업데이트
- Hook이란 'state와 생명주기 기능에 갈고리를 걸어 원하는 시점에 정해진 함수를 실행되도록 만든 함수'
- useState
- useEffect
- useMemo
- useCallback
- useRef
- 훅의 규칙

4월 3일 강의

컴포넌트 만들기

- 컴포넌트의 종류
- 리액트 초기 버전에는 클래스형 컴포넌트를 주요 사용했고 이후 Hook이라는 개념이 나오면서 최근에는 함수형 컴포넌트를 주로 사용
- 함수형 컴포넌트
- 클래스형 컴포넌트

컴포넌트 추출

- 1개의 컴포넌트에 하나의 기능만 사용하도록 설계(실무)

state

- state는 리액트 컴포넌트의 상태를 의미
- 상태의 의미는 컴포넌트의 변경 가능한 데이터를 의미

state의 특징

- 리액트 만의 특별한 형태가 아닌 단지 자바스크립트 객체 
- state는 변경 가능하다고 했지만 직접 수정은 안 됨
- state를 변경하고자 할 때는 setstate() 함수를 사용

3월 27일 강의

JSX 소개(ch03)

- JSX는 JS에서 XML을 추가한 확장 문법
- 결국 JSX는 가독성을 높여 주는 역할(JSX의 장점)

JSX 사용법

- 모든 자바스크립트 문법을 지원
- 자바스크립트 문법에 XML과 HTML을 섞어서 사용
- 자바스크립트 코드를 사용하고 싶으면 {}괄호를 사용

엘리먼트(ch04)

- 엘리먼트는 리액트 앱을 구성하는 요소를 의미
- 공식페이지에는 '엘리멘트는 리액트 앱의 가장 작은 빌딩 블록들'이라고 설명
- 리액트 엘리먼트는 자바스크립트 객체의 형태로 존재
- 리액트 엘리먼트의 가장 큰 특징은 불변성
- 내용을 바꾸려면 컴포너트를 통해 새로운 엘리먼트를 생성하고 이전 엘리먼트와 교체를 하는 방법
- 교체하는 작업을 하기 위해서는 Virtual DOM을 사용
- 엘리먼트 랜더링


3월 20일 강의

* 리액트의 장점
1. 빠른 업데이트 
2. 렌더링 속도 
- 이것을 가능하게 만드는건 Virture DOM이다.
  Virture DOM은 DOM조작이 변화하지 않는 것까지 생각하여 고안한 방법이다.

* 리액트의 단점
1. 방대한 학습량
- 자바스크립트를 공부한 경우 빠르게 학습 가능

2. 높은 상태 관리 복잡도
- state, component life cycle 등의 개념이 있지만, 그리 어렵지 않다.

Chapter 2 리액트 시작하기

create-react-app

## 3월 13일 강의 내용
### GitHub 사용법