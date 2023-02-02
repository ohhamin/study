# PWA (Progressive Web App)

웹의 장점과 앱의 장점을 결합한 환경

-> 앱 수준과 같은 사용자 경험을 웹에서 제공하는 것이 목적

##### 특징

- 확장성이 좋고, 깊이 있는 앱같은 웹을 만드는 것을 지향한다.

- 웹 주소만 있다면 누구나 접근하여 사용이 가능하고, 스마트폰의 저장공간을 잡아 먹지 않음

- 서비스워커 API가 웹앱의 중요한 부분을 캐싱하여 다음에 열 때 빠르게 로딩하거나 오프라인 상태에서도 열 수 있게 함.

##### 제공 기능

- 프로그래시브 : 점진적 개선을 통해 작성되서 어떤 브라우저든 상관없이 모든 사용자에게 적합

- 반응형 : 데스크톱, 모바일, 테블릿 등 모든 폼 factor에 맞음

- 연결 독립적 : 서비스워커를 사용해 오프라인에서 동작 가능

- 안전 : HTTPS를 통해 제공이 되므로 스누핑이 차단되어 콘텐츠가 변조되지 않음

- 검색가능 : W3C 매니페스트 및 서비스워커 등록 범위 덕분에 앱으로 식별되어 검색이 가능함

- 재참여 가능 : 푸시알람과 같은 기능을 통해 쉽게 재참여가 가능

# 실제 프로젝트

1. public 안에 아이콘과 manifest.json 파일 생성

![](PWA_assets/2023-02-02-12-18-32-image.png)

```javascript
{
    // 테마컬러가 안먹히는데 이유는 모르겠음
  "theme_color": "#467302",
  "background_color": "#467302",
  "display": "standalone",
  "scope": "/",
  "start_url": "/",
  "name": "독초도감",
  "short_name": "독초도감",
  "icons": [
    {
      "src": "icons/icon-192x192.png",
      "sizes": "192x192",
      "type": "image/png",
      "purpose": "any maskable"
    },
    {
      "src": "icons/icon-256x256.png",
      "sizes": "256x256",
      "type": "image/png"
    },
    {
      "src": "icons/icon-384x384.png",
      "sizes": "384x384",
      "type": "image/png"
    },
    {
      "src": "icons/icon-512x512.png",
      "sizes": "512x512",
      "type": "image/png"
    }
  ]
}
```

2. index.html에 추가

```javascript
<link rel="manifest" href="/manifest.json" />
<!-- 주소창 등의 웹 브라우저 UI를 표시하지 않기 -->
<meta name="apple-mobile-web-app-capable" content="yes" />
<!-- 상태 바의 스타일을 지정 -->
<meta
  name="apple-mobile-web-app-status-bar-style"
  content="black-translucent"
/>
<!-- 홈 화면에서 표시되는 앱 이름을 지정 -->
<meta name="apple-mobile-web-app-title" content="독초도감" />
<meta name="theme-color" content="#467302" />
<link
  rel="apple-touch-icon"
  sizes="192x192"
  href="/icons/icon-192x192.png"
/>
<link
  rel="apple-touch-icon"
  sizes="256x256"
  href="/icons/icon-256x256.png"
/>
<link
  rel="apple-touch-icon"
  sizes="384x384"
  href="/icons/icon-384x384.png"
/>
<link
  rel="apple-touch-icon"
  sizes="512x512"
  href="/icons/icon-512x512.png"
/>
```

3. npm 모듈 인스톨

```javascript
npm i register-service-worker
npm i @vue/cli-plugin-pwa
```

4. src 폴더에 registerServiceWorker.js 파일 생성

```javascript
import { register } from 'register-service-worker'

// if (process.env.NODE_ENV === 'development') {
register(`${process.env.BASE_URL}service-worker.js`, {
  ready() {
    console.log(
      'App is being served from cache by a service worker.\n' +
        'For more details, visit https://goo.gl/AFskqB'
    )
  },
  registered() {
    console.log('Service worker has been registered.')
  },
  cached() {
    console.log('Content has been cached for offline use.')
  },
  updatefound() {
    console.log('New content is downloading.')
  },
  updated() {
    console.log('New content is available; please refresh.')
  },
  offline() {
    console.log('No internet connection found. App is running in offline mode.')
  },
  error(error) {
    console.error('Error during service worker registration:', error)
  }
})
```

5. main.js (or .ts)에 import

```javascript
import './registerServiceWorker'
```
