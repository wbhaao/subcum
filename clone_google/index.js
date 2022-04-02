var _id = ''
var _password = ''

const title = document.querySelector("h1");
console.log(title)
function handleTitleClick(){
    title.style.color = "blue";
}
title.addEventListener("click",handleTitleClick);

function changeColor(self){
    alert(_id)
    alert(_password)
    
    backColor = 'None'
    frontColor = 'None'
    // 원래 self 없이 this로 할때 안됐던 이유가
    // this가 button을 가리키고 있지 않아서
    // 2번째에 어떻게 됐냐면 this.value = 'night'로
    // 정의가 오류난 후에 되서
    if (self.value == 'night'){
        backColor = 'black'
        frontColor = 'white'
        self.value = 'day'
    }else{
        backColor = 'white'
        frontColor = 'black'
        self.value = 'night'
    }
    
    document.querySelector('body').style.backgroundColor = backColor;
    document.querySelector('body').style.color = frontColor;

    // 링크는 따로 받아서 바꾸기
    a = document.querySelectorAll('a')
    for (let index = 0; index < a.length; index++) {
        a[index].style.color = frontColor
    }
}

function check_login(){
    const id = document.getElementById('id').value;
    const password = document.getElementById('password').value;

    if (id == _id && password == _password){
        alert('로그인 성공')
    } else{
        alert('아이디나 비밀번호가 맞지 않습니다')
        alert(_id + _password + '1')
    }
}

function check_logup(){
    const password = document.getElementById('password').value;
    const password_r = document.getElementById('password_reconfirm').value;

    if (password == password_r){
        _id = document.getElementById('id').value;
        _password = password;
        alert(_id);
        alert(_password); 
    } else{
        alert('비밀번호가 맞지 않습니다')
    }
}

function input_lnk(){
    const name = document.getElementById('name').value;
    window.open(name);
}