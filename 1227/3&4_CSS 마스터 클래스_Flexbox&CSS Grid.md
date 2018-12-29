# #1. Flexbox

## 1.0 Why we need Flexbox

## 1.1 Basics of Flexbox

```css
display: inline block;
```

platform에 따라 diplay의 설정값, 위치가 달라진다.

```css
body{
    display: flex;
}
```

플렉스 컨테이너 규칙을 따른다.

반응형(responsive) 으로 페이지를 구성. display 크기에 상관없이 간격을 같게 맞춘다.

```css
flex-end;
```

오른쪽(end)으로 정렬

```css
flex-start;
```

왼쪽(start)으로 정렬



직접 계산하지 않고 자동으로 웹사이트들이 필요로 하는 기능들을 제공한다.



## 1.2 Main Axis and Cross Axis

```css
align-items: center;
```

flex-end

main axis : justify-content 가 영향을 주는 축

cross axis : align-items 가 영향을 주는 축



display: flex 옵션은 default값으로 방향이 row로 결정되어 있다.

flex-direction: row;   //가로정렬 horizontally

-main axis 는 수평축, cross axis 는 수직축

flex-direction: column;   //세로정렬 vertically

-main axis 는 수직축, cross axis 는 수평축

flex-direnction의 옵션을 변경하면 main-axis와 cross-axis가 서로 바뀌게 됨. - main axis 와 cross axis는 그대로인데, 이것들의 수평/수직 성질이 거꾸로 바뀌게 되는 것이다.

그래서 cross axis 아이템을 움직이려면 align-items, main axis 아이템을 움직이려면 justify-content를 사용한다. 



## 1.3 Flex Wrap and Direction

```css
flex-wrap: wrap;
```

  아이템들 사이에 공간이 없을때 해야 할 행동들을 정의

```css
flex-wrap: nowrap;
```

  아이템들을 최대한 압축해서 한 줄에 모든 아이템들이 들어오도록 한다. default. width를 무시한다.

```css
justify-direction: row-reverse;
```



## 1.4 Align Self and Flexbox Conclusions

align-self : cross-axis에서 각각의 아이템에 대해서 정렬

```css
.box:first-child{
    align-self: flex-end;
}
```

첫번째 item만 flex-end 가 적용된다.



# #2. CSS Grid

## 2.0 Why we need Grid

flexbox는 테이블 시스템의 한계로 인해 Grid 를 사용한다.



## 2.1 Basics CSS Grid

Grid 의 문법은 Flexbox 와 비슷하다.

```css
display: grid;
```

Grid 에는 rows 와 columns 의 개념이 있다.

grid container 에서 rows 와 columns 를 정의할 수 있다.

ex) grid-template-columns,   grid-template-rows

```css
grid-template-columns: 30px;
grid-template-rows: 30px;
```

그리드는 하나의 column과 하나의 row만 가지게 된다.

심플하고 직관적이며 편하다.

```css
grid-gap: 10px;
```

10px 로 간격을 준다.



## 2.2 Auto Rows and Columns

```css
grid-auto-rows: 60px;
```

60px에 맞게 자동으로 rows를 정렬한다.

```css

```

수직정렬

(default 값은 row 이다.)

```css
grid-auto-flow: column;
```

수평정렬



## 2.3 Grid Template Areas

```css

```

width, height, margin, top 등 속성들을 일일이 정해주지 않아도 알아서 제자리를 찾아간다.



## 2.4 fr and repeat()

fr :

fraction (가능한 최대한 공간을 차지하라)

반응형 디자인을 할 때 아무런 계산을 요하지 않는다.

```css

```

첫번째와 세번째 column 은 두번째 네번째 column의 두배의 너비를 차지한다. - 화면의 최대한의 너비를 채운다



repeat

```css
grid-template-columns: repeat(5, 1fr);
```

1fr 만큼의 columns 를 5번 반복하여 지정한다.



## 2.5 minmax, max-content, min-content

minmax : 사용할 object의 maximum 과 minimum 크기를 지정해준다.

```css

```

창에 따라 최소 400px 미만, 최대 2fr 초과로 줄어들거나 늘어나지 않는다.

```css
grid-template-columns: max-content;
```

가능한 가장 크게 자리를 차지한다.

```css
grid-template-columns: min-content;
```

가능한 가장 작게 자리를 차지한다.



## 2.6 auto-fill, auto-fit

```css
grid-template-columns: repeat(auto-fit, 50px)
```

50pixels의 columns를 최대한의 개수로 column을 설정한다.

```css
grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
```

창을 줄이면 350px가 될때까지 column의 크기를 줄이다가 350px보다 작아지면 column을 아래로 내린다.

```css

```

기존에 있는 layout을 빈 칸(ghost grid)으로 채워 가능한 최대한의 cell들이 존재 할 수 있도록 크기를 설정한다.



autofit : content 를 stretch 해서 browser를 꽉 채우는 것

autofill : content가 없더라도 더 많은 columns를 넣기 위해 최대한 모으는 것



## 2.7 Justify Content, Align Content and Place Content

justify-content : 모든 columns(box)를 통째로 이동시킨다. (horizontal)

align-content : box가 포함되어 있는 grid container를 이동시킨다. (vertical)

place-content : align-content 값, justify-content 값

grid 자체를 이동시킬 때 사용한다.



## 2.8 Justify Items, Align Items and Place Items

justify-items : column 안에 있는 item 을 이동한다. grid container 개념처럼 container는 그대로 있고  그 안에 있는 item을 움직이는 것으로 동작한다. (horizontal)

align-items : vertical

place-items : vertical, horizontal



## 2.9 Grid Column, Row Start and End

```css
grid-column: 1 / 3;
```

1에서 시작해서 3이 시작하기전 까지 column을 설정한다.

```css
grid-column-start:1;
grid-column-end:5;
```

1에서 시작해서 5에서 끝나게 한다.



잘리는 곳도 없고, 창을 줄이더라도 변하지 않도록 자동적으로 grid를 확장하면서도 새로운 column 을 추가해준다.



## 2.10 Line Naming and grid-auto-flow

```css
grid-column-start:1;
grid-column-end:-1;
```

1부터 -1까지 이므로 1부터 끝까지 이다.

```css
grid-template-colums: [first-line] 1fr [awesome-line] 1fr [sexy-line] 1fr [nico-line] 1fr [lynn-line] 1fr [line-line];
```

column에 이름(id 값)을 지정해 준다. line naming 에는 빈칸이 있으면 안되서 '-'로 연결되어 있어야 하고, 배열[]로 저장해야 한다.



```css
grid-auto-flow: row dense;
```

빈 칸(ghost columns)이 생기더라도 자동으로 채운다.



## 2.11 Grid Row, Row Start and End

```css

```

`grid-column` 과 같은 방식. column이 아니라 row

```css
grid-row: span 5;
```

5칸을 잡는다.

span : `grid-column` 과 `grid-row` 에서 사용할 수 있으며 시작과 끝을 지정하지 않고 칸 수 개념으로 작동한다.



## 2.12 Grid Area

```css
grid-area: 2 / 1 / 4 / -1;
```

grid-area: row-start / column-start / row-end / column-end ;

grid-area: row / column

span도 적용 가능



## 2.13 Justify, Align, Place Self

```css
justify-self: center;  /*horizontal*/
align-self: center;   /*vertical*/
```

```css
place-self: center center; /*horizontal vertical*/
```

하나의 box에 대한 alignment나 justification , cell 값을 바꾼다.