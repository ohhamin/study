# 바벨

##### 필요한 이유

크롬, 사파리, 파이어폭스와 같은 에버그린 브라우저(사용자의 업데이트 없이도 최신 버전으로 자동 업데이트를 수행하는 모던 브라우저)의 ES6(ES2015) 지원 비율은 98%지만 IE의 지원 비율은 11%이다.

따라서 크로스 브라우징을 위해 개발 환경을 구축하는 것이 필요하고, ES6 기능을 제공하지 않는 브라우저에 트랜스파일링을 하여 ES5로 변환시키는 과정이 필요하다.

이때 사용되는 트랜스파일러가 바벨이다.

```js
// ES6 화살표 함수와 ES7 지수 연산자
[1, 2, 3].map(n => n ** n);
```

```js
// ES5
"use strict";

[1, 2, 3].map(function (n) {
  return Math.pow(n, n);
});
```

이처럼 Babel는 최신 사양의 자바스크립트 코드를 IE나 구형 브라우저에서도 동작하는 ES5 이하의 코드로 변환(트랜스파일링)할 수 있다.

##### 바벨 설치

```bash
# package.json 생성
$ npm init -y
# babel-core, babel-cli 설치
$ npm install --save-dev @babel/core @babel/cli
```

바벨의 빌드 3단계는 파싱 - 변환 - 출력 으로 이루어지는데 여기서 바벨은 파싱과 출력만 담당한다. 변환 작업은 플러그인들이 처리하게 되는데 자주 사용되는 여러가지 플러그인을 모아논 것을 프리셋이라고 한다.

##### 프리셋 설치

공식 바벨 프리셋으론

- @babel/preset-env
- @babel/preset-flow
- @babel/preset-react
- @babel/preset-typescript

가 있다.

@babel/preset-env도 공식 프리셋의 하나이며 필요한 플러그인 들을 프로젝트 지원 환경에 맞춰서 동적으로 결정해 준다.

```bash
# env preset 설치
$ npm install --save-dev @babel/preset-env
```

설치가 완료되었으면 프로젝트 루트에 .babelrc 파일을 생성하고 아래와 같이 작성한다. 지금 설치한 @babel/preset-env를 사용하겠다는 의미이다.

```json
{
  "presets": ["@babel/preset-env"]
}
```

##### 트랜스파일링

Babel을 사용하여 ES6+ 코드를 ES5 이하의 코드로 트랜스파일링하기 위해 Babel CLI 명령어를 사용할 수도 있으나 npm script를 사용하여 트랜스파일링할 수 있다.

package.json 파일에 scripts를 추가한다. 완성된 package.json 파일은 아래와 같다.

```json
{
  "name": "es6-project",
  "version": "1.0.0",
  "scripts": {
    "build": "babel src/js -w -d dist/js"
  },
  "devDependencies": {
    "@babel/cli": "^7.7.0",
    "@babel/core": "^7.7.2",
    "@babel/preset-env": "^7.7.1"
  }
}
```

위 npm script는 src/js 폴더(타깃 폴더)에 있는 모든 ES6+ 파일들을 트랜스파일링한 후, 그 결과물을 dist/js 폴더에 저장한다. 사용한 옵션의 의미는 아래와 같다.

-w : 타깃 폴더에 있는 모든 파일들의 변경을 감지하여 자동으로 트랜스파일한다. (--watch 옵션의 축약형)

-d : 트랜스파일링된 결과물이 저장될 폴더를 지정한다. (--out-dir 옵션의 축약형)

##### 폴리필

polyfill은 이전 브라우저에서 기본적으로 지원하지 않는 최신 기능을 제공하는 데 필요한 코드이다.

트랜스파일링은 ES6+ 문법을 ES5로 바꿔주는 것이고, 폴리필은 브라우저가 이해할 수 없는 코드에 대하여, 이해할 수 있는 코드 소스를 제공하는 것이다.

예를 들어, Array.prototype.includes는 ES6 코드지만, 바벨에 의해 변화되지 않기 때문에 폴리필 과정이 필요하다.

```js
if (!Array.prototype.includes) {
  Object.defineProperty(Array.prototype, 'includes', {
    value: function (searchElement, fromIndex) {
      if (this == null) {
        throw new TypeError('"this" is null or not defined');
      }

      var o = Object(this);

      var len = o.length >>> 0;

      if (len === 0) {
        return false;
      }

      var n = fromIndex | 0;

      var k = Math.max(n >= 0 ? n : len - Math.abs(n), 0);

      function sameValueZero(x, y) {
        return x === y || (typeof x === 'number' && typeof y === 'number' && isNaN(x) && isNaN(y));
      }

      while (k < len) {
        if (sameValueZero(o[k], searchElement)) {
          return true;
        }
        k++;
      }

      return false;
    }
  });
}
```

따라서, includes 폴리필을 추가하면, includes 메소드가 Array의 프로토타입에 추가되어 정상적으로 사용할 수 있게 해준다.

###### 폴리필이 필요한 경우

- 새로운 객체 (Promise, Set, Map 등)

- 기존 객체의 새로운 메서드

- 새로운 함수 (fetch)

###### 트랜스파일링이 필요한 경우

- 새로운 문법의 경우
  
  - const, let
  
  - spread operator
  
  - arrow function
  
  - class
