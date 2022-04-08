const toDoForm = document.querySelector("#todo-form")
const toDoInput = toDoForm.querySelector("input")
const toDoList = document.querySelector("#todo-list")

let toDos = []
const TODO_KEY = "todos"
var beforeId = -1
var beforeText = ""


function aaSubmit(event){
    event.preventDefault()
    const span = document.createElement("span");
    const retButton = document.createElement('button');
    
    idIndex = toDos.indexOf(beforeId)
    function reTouchFilter(todo){
        return todo.id !== beforeId
    }
    
    toDos = toDos.filter(reTouchFilter);
    newToDoObg = {
        "id":`${Date.now()}${Math.random() * 100}` ,
        "text":event.target.querySelector("input").value
    }
    span.innerText = newToDoObg.text
    
    retButton.innerText = "✏️";
    retButton.addEventListener("click", reTouchToDo);
    toDos.splice(idIndex, 0, newToDoObg);
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
    
    input.required = true
    input.maxLength = 70
    input.type = "text"
    input.placeholder = "what's your toDo"
    form.addEventListener("submit", aaSubmit);
    
    form.appendChild(input)
    // const button = document.createElement('button');
    // button.innerText = "✅"
    const span_ = li.querySelector("span")
    beforeId = li.id
    beforeText = span_.innerText
    console.log(span_)
    console.log(beforeText)
    // li.insertBefore(button, event.target)
    li.insertBefore(form, span_)
    event.target.remove()
    
    span_.remove()
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
    delButton.addEventListener("click", deleteToDo);
    retButton.innerText = "✏️";
    retButton.addEventListener("click", reTouchToDo);
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

toDoForm.addEventListener("submit", onToDoSubmit);
  
const savedToDos = localStorage.getItem(TODO_KEY);
// 얘도 localStorage에 있는거 빼오는 용도
if (savedToDos !== null) {
  const parsedToDos = JSON.parse(savedToDos);
  toDos = parsedToDos
  parsedToDos.forEach((item) => paintToDo(item));
}