# Promise

자바스크립트 비동기 처리에 사용되는 객체

주로 서버에서 받아온 데이터를 화면에 표시할 때 사용하는데 데이터를 받아오기 전에 데이터를 화면에 표시하려 하면 오류가 발생하거나 빈 화면이 뜨는 것을 해결하기 위한 방법.

```javascript
function getData(callback) {
  // new Promise() 추가
  return new Promise(function(resolve, reject) {
    $.get('url 주소/products/1', function(response) {
      // 데이터를 받으면 resolve() 호출
      resolve(response);
    });
  });
}

// getData()의 실행이 끝나면 호출되는 then()
getData().then(function(tableData) {
  // resolve()의 결과 값이 여기로 전달됨
  console.log(tableData); // $.get()의 reponse 값이 tableData에 전달됨
});
```

### Promise의 3가지 State

- Pending(대기) : 비동기 처리 로직이 아직 완료되지 않은 상태

- Fulfilled(이행) : 비동기 처리가 완료되어 프로미스가 결과값을 반환해준 상태

- Rejected(실패) : 비동기 처리가 실패하거나 오류가 발생한 상태

##### Pending


