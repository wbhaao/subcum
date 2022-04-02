const title = document.querySelector("div.hello:first-child h1");
console.dir(title)
function handleTitleClick(){
    title.style.color = "blue"; 
    console.log('helloworld')
}
function handleCopy(){
    alert('복사하지마!')
}
function handleCut(){
    alert('자르지마')
}
function handleOnline(){
    alert('인터넷이 좋다')
}
function handleOffline(){
    alert('인터넷이 나쁘다')
}

title.addEventListener("click",handleTitleClick);
window.addEventListener("copy",handleCopy);
window.addEventListener("cut",handleCut);
window.addEventListener("online",handleOnline);
window.addEventListener("offline",handleOffline);