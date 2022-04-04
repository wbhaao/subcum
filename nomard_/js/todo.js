const toDoForm = document.querySelector("#todo-form")
const toDoInput = toDoForm.querySelector("input")
const toDoList = document.querySelector("#todo-list")

let toDos = []
const TODO_KEY = "todos"

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
    localStorage.setItem(TODO_KEY, JSON.stringify(toDos))
}

function deleteToDo(event) {
    li = event.target.parentElement
    ind = li.querySelector("span").innerText
    console.log("ind:"+ind)
    for (let index = 0; index < toDos.length; index++) {
        if (toDos[index].id === li.id){
            toDos.splice(index, 1);
        }
    }
    saveToDo();
    li.remove()
}

function paintToDo(newToDoObg){
    const li = document.createElement('li');
    const span = document.createElement('span');
    const button = document.createElement('button');
    button.innerText = "❌"
    button.addEventListener("click", deleteToDo)
    li.appendChild(span);
    li.appendChild(button);
    li.id = newToDoObg.id

    span.innerText = newToDoObg.text;
    toDoList.appendChild(li)
}

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