# #3. PostCSS / CSSNext / CSS4

## 3.0 Installing Parcel

```bash
npm init -y
npm install -g parcel-bundler
npm run start

```

이전에는 수정 내역이 file 에 저장되고, file을 다시 열거나 새로고침 해야 했지만 parcel 을 사용하면 서버에 저장되고 서버에서 불러올 수 있다.



## 3.1 PostCSS and Parcel

호환성 문제를 해결하면서 자동으로 코드를 바꾸어 준다.

```bash
npm install postcss-preset-env
```



## 3.2 Functional pseudo-classes

matches : class, id 와 매칭시켜 부분, 일괄적으로 properties를 적용, 미적용 시킬 수 있다.



```css
li:matches(:nth-child(even)), .target){
    background-color: blue;
}
```

li class 의 even(짝수번째) 과 .target 부분을 지정하고, background-color(배경 색)를 blue(파랑색)로 설정한다.



```css
li:not(.target){
    background-color:blue;
}
```

li class 의 .target 부분이 아닌 부분을 지정하고, background-color(배경 색)를 blue(파랑색)로 설정한다.



## 3.3 CSS Variables

css variables : css가 프로그래밍 언어처럼 보이도록 글씨 크기, 글씨체, 글씨 색깔 등을 지정할 수 있다.



```css

```

HTML 문서 자체보다 더 높은 element 인 root에 variable을 '--' 와 '이름' 으로 구체화하여 저장한다.

HTML 문서 상위 단계인 root 에 저장되어 있기 때문에 모든 문서에 적용될 수 있고 #2988b9 라는 색을 --awesomeColor 라는 (전역) 변수에 지정 했기 때문에 프로젝트 단위에서 사용 될 수 있다. 색깔 뿐만 아니라 글씨 크기, 글씨체, 효과 등의 style에 모두 사용 될 수 있다.



custom selector : property 가 아니라 selection of element 이다. 이것 또한 global(전역)하게 지정하는 방식이다.



```css
@custom-selector :--headers h1, h2, h3, h4, h5, h6
    
:headers{
        color:#8e44ad;
}
```

h1, h2, h3, h4, h5, h6 태그에 #8e44ad 의 색을 지정한다.



## 3.4 @custom-media and Media Query Ranges

custom media query : variable 과 비슷하지만 media query 를 위한 것이다.



```css
@custom-media --ipad-size (max-width: 850px);

@media(--ipad-size){
    body{
        background-color: red;
    }
}
```

최대 너비를 850px로 하는 'ipad-size' 라는 미디어를 선언한 후 'ipad-size'(최대 850px의 너비)에서만 background-color 를 red 로 설정한다.

```css
@custom-media --ipad-size (width <= 850px);

@media(--ipad-size){
    body{
        background-color: red;
    }
}
```

width(너비) 가 850px 이하인 것을 ipad-size 라고 선언한다.

max-width : 850px 로 자동 변환 해 준다.



```css
@custom-media --ipad-size (450px <= width < 850px);

@media(--ipad-size){
    body{
        background-color: red;
    }
}
```

min-width : 450px , max-width : 849px 로 자동 변환해준다.



## 3.5 color-mod, gray(), system-ui

color-mod

- alpha : 투명도

- contrast : 강조(글씨 크기)

- hover : 마우스 올렸을때 색 변화 (Link 에 주로 사용)

- blackness, lightness : color code 를 변화시켜 어둡게, 밝게 바꾸어 준다.

- 등등등.. 검색을 통해 찾을 수 있다.



gray(50) : 50퍼센트로 회색의 채도(강도)를 조정



font-family: system-ui;  :  os의 고유(시스템) 폰트를 사용



## 3.6 Nesting Rules

nesting : css 를 더 좋아보이게 만들 수 있고, selector 의 반복을 줄일 수 있다.

```css
main{
background-color: blue;
    & section {
        background-color:red;
    	width: 500px;
        & li {
            background-color: yellow;
            width: 400px;
            & a {
                color: black;
                &:hover {
                    font-size: 30px;
                }
            }
        }
    }
}
```

css가 더 정확해지고 강력해진다.

selection이 더 자세할 수록(들여쓰기의 강도) 더 우위를 가진다.



## 3.7 Conclusions

css grid kiss : 쉬운 방법으로 grid areas 와 grid templates 를 그리게 해준다.

```css
npm install postcss-grid-kiss
```



https://codesandbox.io