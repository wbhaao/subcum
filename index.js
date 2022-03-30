function getNum(){
    const NUM1 = Number(prompt('숫자를 입력하세요'));
    const oper = prompt('계산방법을 입력하세요');
    const NUM2 = Number(prompt('숫자를 입력하세요'));
    
    if (oper == "+"){
        document.getElementById('answer').innerText = NUM1 + NUM2
    }
    else if (oper == "-"){
        document.getElementById('answer').innerText = NUM1 - NUM2
    }
    else if (oper == "*"){
        document.getElementById('answer').innerText = NUM1 * NUM2
    }
    else if (oper == "/"){
        document.getElementById('answer').innerText = NUM1 / NUM2
    }
}