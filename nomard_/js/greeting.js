const loginForm = document.querySelector('#login-form')
const loginInput = document.querySelector('#login-form input')
// const loginButton = document.querySelector('#login-form button')
const greeting = document.querySelector('h1')
const link = document.querySelector('a')

const HIDDEN_CLASSNAME = "hidden"
const USERNAME_KEY = 'username'


function onLoginSubmit(event){
    // 브라우저가 기본 동작을 실행하지 못하게 막기 
    // event object는 preventDefault함수를 기본적으로 갖고 있음
    event.preventDefault(); 
    const userName = loginInput.value
    localStorage.setItem(USERNAME_KEY, userName)
    paintGreeting(userName)
    loginForm.classList.add(HIDDEN_CLASSNAME)
}

function paintGreeting(userName){
    greeting.innerText = `Hello ${userName}`
    greeting.classList.remove(HIDDEN_CLASSNAME)
}

const saveUserName = localStorage.getItem(USERNAME_KEY)

if (saveUserName == null){
    // null 이면 계속진행 있다면 hello name 보여주기
    greeting.classList.add(HIDDEN_CLASSNAME)
    loginForm.classList.remove(HIDDEN_CLASSNAME)
    loginForm.addEventListener("submit", onLoginSubmit)
} else{
    paintGreeting(saveUserName)
  // 이 코드는 이미 name 있을때 *처음* 실행되기에 loginForm은 이미 안보임
    // loginForm.classList.add(HIDDEN_CLASSNAME)
}

