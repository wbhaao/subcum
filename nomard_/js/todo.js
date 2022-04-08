const toDoForm = document.querySelector("#todo-form")
const toDoInput = toDoForm.querySelector("input")
const toDoList = document.querySelector("#todo-list")

let toDos = []
const SUBMIT_KEY = "submit"
const TODO_KEY = "todos"
const CLICK_KEY = "click"
const BEFORE_ID_KEY = "beforeId"
// id로 찾으니까 
// var beforeText = ""


function aaSubmit(event){
    event.preventDefault()
    const span = document.createElement("span");
    const retButton = document.createElement('button');
    beforeId = localStorage.getItem(BEFORE_ID_KEY)
    // 전 text의 id
    toDosId = []
    for (let index = 0; index < toDos.length; index++) {
        toDosId.push(toDos[index].id)
    }

    let idIndex = toDosId.indexOf(beforeId)
    console.log("idIndex:"+idIndex);
    function reTouchFilter(todo){
        return todo.id !== beforeId
    }
    // 전 spanText 제거
    toDos = toDos.filter(reTouchFilter);
    newToDoObg = {
        "id":`${Date.now()}${Math.random() * 100}` ,
        "text":event.target.querySelector("input").value
    }
    // span 텍스트 지정
    span.innerText = newToDoObg.text
    
    retButton.innerText = "✏️";
    retButton.addEventListener(CLICK_KEY, reTouchToDo);
    // 원래 Text Index에 현 textObg 추가
    toDos.splice(idIndex, 0, newToDoObg);
    // 새 span이랑 retouch 버튼 추가
    event.target.parentElement.insertBefore(span, event.target)
    event.target.parentElement.insertBefore(retButton, event.target)
    
    event.target.remove()
    saveToDo()
}
// localStorage에 있는거 빼오는 용도
function loadToDo() {
    storage_todos = localStorage.getItem(TODO_KEY)
    storage_todos = JSON.parse(storage_todos)
    for (let index = 0; index < storage_todos.length; index++) {
        paintToDo(storage_todos[index])
        console.log(storage_todos[index])
    }
}

function saveToDo() {
    localStorage.setItem(TODO_KEY, JSON.stringify(toDos));
}

function reTouchToDo(event) {
    li = event.target.parentElement;
    const input = document.createElement('input');
    const form = document.createElement('form');
    
    input.required = true;
    input.maxLength = 70;
    input.type = "text";
    input.placeholder = "what's your toDo";
    form.addEventListener(SUBMIT_KEY, aaSubmit);
    
    form.appendChild(input);
    const span_ = li.querySelector("span");
    // 삭제 될떄 저장하기
    localStorage.setItem(BEFORE_ID_KEY, li.id);
    console.log(localStorage.getItem(BEFORE_ID_KEY));
    console.log("hgl");
    li.insertBefore(form, span_);
    event.target.remove();
    
    span_.remove();
}

function deleteToDo(event) {
    li = event.target.parentElement;
    toDos = toDos.filter((todo) => todo.id !== li.id);
    saveToDo();
    li.remove();
}

function paintToDo(newToDoObg){
    const li = document.createElement('li');
    const span = document.createElement('span');
    const delButton = document.createElement('button');
    const retButton = document.createElement('button');
    delButton.innerText = "❌";
    delButton.addEventListener(CLICK_KEY, deleteToDo);
    retButton.innerText = "✏️";
    retButton.addEventListener(CLICK_KEY, reTouchToDo);
    li.appendChild(span);
    li.appendChild(retButton);
    li.appendChild(delButton);
    li.id = newToDoObg.id;

    span.innerText = newToDoObg.text;
    toDoList.appendChild(li)
}

// 현재 list를 저장

function onToDoSubmit(event){
    event.preventDefault(); 
    newToDoObg = {
        "id":`${Date.now()}${Math.random() * 100}` ,
        "text":toDoInput.value
    }
    paintToDo(newToDoObg)
    toDos.push(newToDoObg)
    toDoInput.value = ""
    // 현재 list를 저장
    saveToDo();
}

toDoForm.addEventListener(SUBMIT_KEY, onToDoSubmit);
  
const savedToDos = localStorage.getItem(TODO_KEY);
// 얘도 localStorage에 있는거 빼오는 용도
if (savedToDos !== null) {
  const parsedToDos = JSON.parse(savedToDos);
  toDos = parsedToDos
  parsedToDos.forEach((item) => paintToDo(item));
}