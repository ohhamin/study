# this

자바스크립트의 함수는 호출될 때, 매개변수로 전달되는 인자값 이외에, arguments 객체와 this를 암묵적으로 전달 받는다.

```js
function square(number) {

  console.log(arguments);
  console.log(this);

  return number * number;
}

square(2);
```

Java에서의 this : 인스턴스 자신을 가리키는 참조변수 (객체 자신에 대한 참조 값)

javascrip에서의 this : 해당 함수 호출 방식에 따라 this에 바인딩 되는 객체가 달라짐

### 함수 호출 방식과 this 바인딩

함수를 선언할 때 this에 바인딩할 객체가 정적으로 결정되는 것이 아니고, 함수를 호출할 때 함수가 어떻게 호출되었는지에 따라 this에 바인딩할 객체가 동적으로 결정된다.

(함수의 상위 스코프를 결정하는 방식인 렉시컬 스코프(Lexical scope)는 함수를 선언할 때 결정된다.)

함수 호출 방식은 다음과 같다.

> 1. 함수 호출
> 2. 메소드 호출
> 3. 생성자 함수 호출
> 4. apply/call/bind 호출

```js
var foo = function () {
  console.dir(this);
};

// 1. 함수 호출
foo(); // window
// window.foo();

// 2. 메소드 호출
var obj = { foo: foo };
obj.foo(); // obj

// 3. 생성자 함수 호출
var instance = new foo(); // instance

// 4. apply/call/bind 호출
var bar = { name: 'bar' };
foo.call(bar);   // bar
foo.apply(bar);  // bar
foo.bind(bar)(); // bar
```

### 1. 함수 호출

전역 객체는 모든 객체의 유일한 최상위 객체를 의미하며 일반적으로 브라우저사이드에선 window, 서버사이드에선 global 객체를 의미한다.

전역객체는 전역 스코프(Global Scope)를 갖는 전역변수(Global variable)를 프로퍼티로 소유한다. 글로벌 영역에 선언한 함수는 전역객체의 프로퍼티로 접근할 수 있는 전역 변수의 메소드이다.

```js
var ga = 'Global variable';

console.log(ga);
console.log(window.ga);

function foo() {
  console.log('invoked!');
}
window.foo();
```

기본적으로 this는 전역객체에 바인딩 된다. 전역 함수 뿐만 아니라 

1. 내부 함수의 경우

2. 메소드의 내부 함수일 경우

3. 콜백 함수의 경우

도 this는 전역객체에 바인딩 된다.

```js
// 1. 내부 함수의 경우
function foo() {
  console.log("foo's this: ",  this);  // window
  function bar() {
    console.log("bar's this: ", this); // window
  }
  bar();
}
foo();


// 2. 메소드의 내부 함수일 경우
var value = 1;

var obj = {
  value: 100,
  foo: function() {
    console.log("foo's this: ",  this);  // obj
    console.log("foo's this.value: ",  this.value); // 100
    function bar() {
      console.log("bar's this: ",  this); // window
      console.log("bar's this.value: ", this.value); // 1
    }
    bar();
  }
};

obj.foo();

// 3. 콜백 함수의 경우
var value = 1;

var obj = {
  value: 100,
  foo: function() {
    setTimeout(function() {
      console.log("callback's this: ",  this);  // window
      console.log("callback's this.value: ",  this.value); // 1
    }, 100);
  }
};

obj.foo();
```

내부함수는 일반 함수, 메소드, 콜백함수 어디에서 선언되었든 관게없이 this는 전역객체를 바인딩한다. 더글라스 크락포드는 “이것은 설계 단계의 결함으로 메소드가 내부함수를 사용하여 자신의 작업을 돕게 할 수 없다는 것을 의미한다” 라고 말한다. 내부함수의 `this`가 전역객체를 참조하는 것을 회피방법은 that을 사용하거나 apply, call, bind 메소드를 사용하는 것이다.

```js
// that 사용
var value = 1;

var obj = {
  value: 100,
  foo: function() {
    var that = this;  // Workaround : this === obj

    console.log("foo's this: ",  this);  // obj
    console.log("foo's this.value: ",  this.value); // 100
    function bar() {
      console.log("bar's this: ",  this); // window
      console.log("bar's this.value: ", this.value); // 1

      console.log("bar's that: ",  that); // obj
      console.log("bar's that.value: ", that.value); // 100
    }
    bar();
  }
};

obj.foo();

// apply, call, bind 메소드 사용
var value = 1;

var obj = {
  value: 100,
  foo: function() {
    console.log("foo's this: ",  this);  // obj
    console.log("foo's this.value: ",  this.value); // 100
    function bar(a, b) {
      console.log("bar's this: ",  this); // obj
      console.log("bar's this.value: ", this.value); // 100
      console.log("bar's arguments: ", arguments);
    }
    bar.apply(obj, [1, 2]);
    bar.call(obj, 1, 2);
    bar.bind(obj)(1, 2);
  }
};

obj.foo();
```

### 2. 메소드 호출

함수가 객체의 프로퍼티 값이면 메소드로서 호출된다. 이때 메소드 내부의 this는 해당 메소드를 소유한 객체, 즉 해당 메소드를 호출한 객체에 바인딩된다.

```js
var obj1 = {
  name: 'Lee',
  sayName: function() {
    console.log(this.name);
  }
}

var obj2 = {
  name: 'Kim'
}

obj2.sayName = obj1.sayName;

obj1.sayName(); // Lee
obj2.sayName(); // Kin
```

프로토타입 객체도 메소드를 가질 수 있다. 프로토타입 객체 메소드 내부에서 사용된 this도 일반 메소드 방식과 마찬가지로 해당 메소드를 호출한 객체에 바인딩 된다.

```js
function Person(name) {
  this.name = name;
}

Person.prototype.getName = function() {
  return this.name;
}

var me = new Person('Lee');
console.log(me.getName()); // Lee

Person.prototype.name = 'Kim';
console.log(Person.prototype.getName()); // Kim
```

### 3. 생성자 함수 호출

자바스크립트의 생성자 함수는 말 그대로 객체를 생성하는 역할을 한다. 하지만 자바와 같은 객체지향 언어의 생성자 함수와는 다르게 그 형식이 정해져 있는 것이 아니라 기존 함수에 new 연산자를 붙여서 호출하면 해당 함수는 생성자 함수로 동작한다.

이는 반대로 생각하면 생성자 함수가 아닌 일반 함수에 new 연산자를 붙여 호출하면 생성자 함수처럼 동작할 수 있다. 따라서 일반적으로 생성자 함수명은 첫문자를 대문자로 기술하여 혼란을 방지하려는 노력을 한다.

new 연산자와 함께 생성자 함수를 호출하면 this 바인딩이 메소드나 함수 호출 때와는 다르게 동작한다.

##### 생성자 함수 동작 방식

**1. 빈 객체 생성 및 this 바인딩**

생성자 함수의 코드가 실행되기 전 빈 객체가 생성된다. 이 빈 객체가 생성자 함수가 새로 생성하는 객체이다. 이후 **생성자 함수 내에서 사용되는 this는 이 빈 객체를 가리킨다.** 그리고 생성된 빈 객체는 생성자 함수의 prototype 프로퍼티가 가리키는 객체를 자신의 프로토타입 객체로 설정한다.

**2. this를 통한 프로퍼티 생성**

생성된 빈 객체에 this를 사용하여 동적으로 프로퍼티나 메소드를 생성할 수 있다. this는 새로 생성된 객체를 가리키므로 this를 통해 생성한 프로퍼티와 메소드는 새로 생성된 객체에 추가된다.

**3. 생성된 객체 반환**

- 반환문이 없는 경우, this에 바인딩된 새로 생성한 객체가 반환된다. 명시적으로 this를 반환하여도 결과는 같다.
- 반환문이 this가 아닌 다른 객체를 명시적으로 반환하는 경우, this가 아닌 해당 객체가 반환된다. 이때 this를 반환하지 않은 함수는 생성자 함수로서의 역할을 수행하지 못한다. 따라서 생성자 함수는 반환문을 명시적으로 사용하지 않는다.

```js
function Person(name) {
  // 생성자 함수 코드 실행 전 -------- 1
  this.name = name;  // --------- 2
  // 생성된 함수 반환 -------------- 3
}

var me = new Person('Lee');
console.log(me.name); // Lee
```

##### 생성자 함수에 new 연산자를 붙이지 않고 호출할 경우

생성자 함수를 new 없이 호출한 경우, 함수 Person 내부의 this는 전역객체를 가리키므로 name은 전역변수(window)에 바인딩된다. 또한 new와 함께 생성자 함수를 호출하는 경우에 암묵적으로 반환하던 this도 반환하지 않으며, 반환문이 없으므로 undefined를 반환하게 된다.

```js
function Person(name) {
  // new없이 호출하는 경우, 전역객체에 name 프로퍼티를 추가
  this.name = name;
};

// 일반 함수로서 호출되었기 때문에 객체를 암묵적으로 생성하여 반환하지 않는다.
// 일반 함수의 this는 전역객체를 가리킨다.
var me = Person('Lee');

console.log(me); // undefined
console.log(window.name); // Lee
```

### apply/call/bind 호출

```js
var Person = function (name) {
  this.name = name;
};

var foo = {};

// apply 메소드는 생성자함수 Person을 호출한다. 이때 this에 객체 foo를 바인딩한다.
Person.apply(foo, ['name']);

console.log(foo); // { name: 'name' }
```

빈 객체 foo를 apply() 메소드의 첫번째 매개변수에, argument의 배열을 두번째 매개변수에 전달하면서 Person 함수를 호출하였다. 이때 Person 함수의 this는 foo 객체가 된다. Person 함수는 this의 name 프로퍼티에 매개변수 name에 할당된 인수를 할당하는데 this에 바인딩된 foo 객체에는 name 프로퍼티가 없으므로 name 프로퍼티가 동적 추가되고 값이 할당된다.

apply() 메소드의 대표적인 용도는 arguments 객체와 같은 유사 배열 객체에 배열 메소드를 사용하는 경우이다. arguments 객체는 배열이 아니기 때문에 slice() 같은 배열의 메소드를 사용할 수 없으나 apply() 메소드를 이용하면 가능하다.

```js
function convertArgsToArray() {
  console.log(arguments);

  // arguments 객체를 배열로 변환
  // slice: 배열의 특정 부분에 대한 복사본을 생성한다.
  var arr = Array.prototype.slice.apply(arguments); // arguments.slice
  // var arr = [].slice.apply(arguments);

  console.log(arr);
  return arr;
}

convertArgsToArray(1, 2, 3);
```

`Array.prototype.slice.apply(arguments)`는 “Array.prototype.slice() 메소드를 호출하라. 단 this는 arguments 객체로 바인딩하라”는 의미가 된다. 결국 Array.prototype.slice() 메소드를 arguments 객체 자신의 메소드인 것처럼 `arguments.slice()`와 같은 형태로 호출하라는 것이다.

call() 메소드의 경우, apply()와 기능은 같지만 apply()의 두번째 인자에서 배열 형태로 넘긴 것을 각각 하나의 인자로 넘긴다.

apply()와 call() 메소드는 콜백 함수의 this를 위해서 사용되기도 한다.

```js
function Person(name) {
  this.name = name;
}

Person.prototype.doSomething = function(callback) {
  if(typeof callback == 'function') {
    // --------- 1
    callback();
  }
};

function foo() {
  console.log(this.name); // --------- 2
}

var p = new Person('Lee');
p.doSomething(foo);  // undefined
```

1의 시점에서 this는 Person 객체이다. 그러나 2의 시점에서 this는 전역 객체 window를 가리킨다. 콜백함수를 호출하는 외부 함수 내부의 this와 콜백함수 내부의 this가 상이하기 때문에 문맥상 문제가 발생한다. 따라서 콜백함수 내부의 this를 콜백함수를 호출하는 함수 내부의 this와 일치시켜 주어야 하는 번거로움이 발생한다.

```js
function Person(name) {
  this.name = name;
}

Person.prototype.doSomething = function (callback) {
  if (typeof callback == 'function') {
    callback.call(this);
  }
};

function foo() {
  console.log(this.name);
}

var p = new Person('Lee');
p.doSomething(foo);  // 'Lee'
```

Function.prototype.bind는 함수에 인자로 전달한 this가 바인딩된 새로운 함수를 리턴한다. 즉, Function.prototype.bind는 Function.prototype.apply, Function.prototype.call 메소드와 같이 함수를 실행하지 않기 때문에 명시적으로 함수를 호출할 필요가 있다.

```js
function Person(name) {
  this.name = name;
}

Person.prototype.doSomething = function (callback) {
  if (typeof callback == 'function') {
    // callback.call(this);
    // this가 바인딩된 새로운 함수를 호출
    callback.bind(this)();
  }
};

function foo() {
  console.log('#', this.name);
}

var p = new Person('Lee');
p.doSomething(foo);  // 'Lee'
```
