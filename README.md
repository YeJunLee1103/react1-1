# 이예준 202030227

## 5월 22일 강의

## 5월 8일 강의

Arguments 전달

- 함수를 정의할 때 파라미터 혹은 매개변수, 함수를 사용할 때는 argument 혹은 인수 라고 부름
- 이벤트 핸들러에 매개변수를 전달해야 하는 경우도 있음

실습

- 클릭 이벤트 처리하기
- ConfirmButton 컴포넌트 만들기
- 클래스 필드 문법 사용하기
- 함수 컴포넌트 변경하기

조건부 렌더링

- 조건이란 우리가 알고 있는 조건문의 조건

엘리먼트 변수

- 렌더링해야 될 컴포넌트를 변수처럼 사용하는 방법이 엘리먼트 변수

인라인 조건

- 필요한 곳에 조건문을 직접 넣어 사용하는 방법
- 인라인if
- 인라인 if-else

컴포넌트 렌더링 막기

- 컴포넌트를 랜더링하고 싶지 않을 때는 null을 리턴

## 5월 1일 강의

훅의 두가지 규칙

- 첫 번째 규칙 : 무조건 최상위 레벨에서만 호출해야 함
- 훅은 컴포넌트가 랜더링 될 때마다 같은 순서로 호출
- 두 번째 규칙 : 함수형 컴포넌트에서만 훅을 호출
- 함수형 컴포넌트 or 직접 만든 커스텀 훅에서만 호출 가능

나만의 훅 만들기
- 직접 만들어 훅을 사용할 수 있음 -> 커스텀 훅

커스텀 훅 추출하기
- use로 시작하는 훅을 만들고 내부에서 다른 훅을 호출
- 다른 훅을 호출하는 것은 무조건 커스텀 훅의 최상위 레벨만 해야 함

이벤트 핸들링

이벤트 처리하기

- DOM이나 React에서 클릭 이벤트를 처리하는 예제 코드
- 둘의 차이점은 이벤트 이름이 onclick에서 onClick으로 변경
- 이벤트가 발생했을 때 해당 이벤트를 처리하는 함수를 '이벤트 핸들러'라고 함. 또는 이벤트가 발생하는 것을 계속 듣고 있다는 의미로 '이벤트 리스너'라고 부름


## 4월 17일 강의

-훅(Hook)

Hook이란 state와 생명주기 기능에 갈고리를 걸어 원하는 시점에 정해진 함수를 실행되도록 만든 함수
클래스형 컴포넌트에서는 생성자(constructor)에서 state를 정의하고, setState() 함수를 통해 state를 업데이트
함수형 컴포넌트에서도 state나 생명주기 함수의 기능을 사용하게 해주기 위해 추가된 기능이 바로 훅(Hook)
함수형 컴포넌트도 훅을 사용하여 클래스형 컴포넌트의 기능을 모두 통일하게 구현할 수 있게 됨

-useState

useState는 함수형 컴포넌트에서 state를 사용하기 위한 Hook
useEffect

useState와 함께 가장 많이 사용하는 Hook임
이 함수는 사이드 이펙트를 수행하기 위한 것

-usMemo

useMemo()훅은 Memoized value를 리턴하는 훅
이 훅은 렌더링이 일어나는 동안 실행됨

-useCallback

useCallback() 훅은 useMemo()와 유사한 역할
차이점은 값이 아닌 함수를 반환한다는 점
의존성 배열을 파라미터로 받는 것은 useMemo와 동일함
파라미터로 받은 함수를 콜백이라고 함

-useRef

useRef() 혹은 레퍼런스를 사용하기 위한 훅
레퍼런스란 특정 컴포넌트에 접근할 수 있는 객체를 의미
레퍼런스 객체에는 .current라는 속성이 있는데, 이것은 현재 참조하고 있는 엘리먼트를 의미함

## 4월 3일 강의

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

## 3월 27일 강의

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

## 3월 20일 강의

- 리액트의 장점

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

## GitHub 사용법
