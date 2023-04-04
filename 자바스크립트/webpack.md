# Webpack

##### 필요한 이유

1. 자바스크립트는 모듈을 지원하지 않았다(ES5). 하지만 ES6가 나오며 모듈을 지원하게 되었다.
   
   그런데 ES6를 지원하지 않는 브라우저는 모듈화를 지원하지 않는다. 따라서 브라우저 버전에 상관 없이 모듈 시스템을 사용할 수 있게 만든 툴이 웹팩이다. ([참고](https://ingg.dev/webpack/))

2. 웹 사이트 진입시 브라우저는 서버로부터 해당 어플리케이션의 자원(HTML, CSS, JS, Image,,)들을 다운로드 한다. 이때 번들러인 웹팩을 사용하게 되면 여러개의 자원을 하나 이상의 파일로 병합시켜줘서 네트워크 요청 자체가 줄어들게 되고, 부하를 줄일 수 있다.
   
   또한 모든 리소스를 한번에 다운로드하는 SPA의 단점을 보완하기 위해 Lazy-loading과 code splitting 기능을 함께 제공한다.

3. HTML, css, js 압축, 이미지 압축, scss -> css 변환과 같은 작업들을 웹팩이 자동으로 관리해준다.

##### 기본 개념

###### 1. 엔트리

엔트리는 의존성 그래프의 시작점을 의미한다. 엔트리 파일을 의존하는 파일은 없고, 엔트리가 A를 의존, A가 B, C를 의존 하는 식으로 모듈이 연결된다.

```js
// webpack.config.js
module.exports = {
    entry: {
        main: './src/main.js',
    }
}
```

###### 2. 아웃풋

엔트리에 설정한 자바스크립트 파일을 시작을, 의존되어 있는 모듈을 하나로 묶어서 내보낸다(번들링). 결과물이 나오는 위치는 output 키에 기록한다.

```js
// webpack.config.js
module.exports = {
    output: {
        filename: 'bundle.js', 
        path: '.dist'
    }
}
```

###### 3. 로더

웹팩은 이미지, 폰트, 스타일시트까지 모듈로 관리한다. 웹팩은 자바스크립트밖에 모르기 때문에 자바스크립트가 아닌 파일들을 웹팩이 이해하도록 변경해야하는데, 이를 로더가 해준다.

```js
//webpack.config.js 
//css 로더 예시
//test에 로딩할 파일 지정
//use에 사용할 로더
module.exports = {
    module: {
        rules: [{            
            test: /\.css$/,
            use: ['style-loader', 'css-loader']
        }]
    }
}
```

###### 4. 플러그인

로더는 번들되기 전 파일 단위를 처리하고, 플러그인은 번들된 결과물을 추가로 처리한다.

```js
// webpack.config.js
// 번들링된 파일에 배너(텍스트)를 달아주는 플러그인
module.exports = {
  plugins: [
    new webpack.BannerPlugin({
      banner: `
        Build Date :: ${new Date().toLocaleString()}
        Commit Version :: ${removeNewLine(
          childProcess.execSync("git rev-parse --short HEAD")
        )}
        Auth.name :: ${removeNewLine(
          childProcess.execSync("git config user.name")
        )}
        Auth.email :: ${removeNewLine(
          childProcess.execSync("git config user.email")
        )}
  `,
    }),
  ],
}
```
