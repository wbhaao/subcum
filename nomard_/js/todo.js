const toDoForm = document.querySelector("#todo-form")
const toDoInput = toDoForm.querySelector("input")
const toDoList = document.querySelector("#todo-list")

const toDos = []
const TODO_KEY = "todos"

function loadToDo() {
    todos = localStorage.getItem(TODO_KEY)
    console.log(todos)
    todos = todos.slice(1, todos.length-1)
    for (let index = 0; index < todos.replace('"', '').length-1; index++) {
        todos = todos.replace('"', '')
    }
    todos = todos.split(",")
    console.log(typeof(todos))
    for (let index = 0; index < todos.length; index++) {
        paintToDo(todos[index])
        console.log(todos[index])
    }
}

function saveToDo() {
    localStorage.setItem(TODO_KEY, JSON.stringify(toDos))
}

function deleteToDo(event) {
    event.target.parentElement.remove()
}

function paintToDo(newToDo){
    const li = document.createElement('li');
    const span = document.createElement('span');
    const button = document.createElement('button');
    button.innerText = "❌"
    button.addEventListener("click", deleteToDo)
    li.appendChild(span);
    li.appendChild(button);
    span.innerText = newToDo;
    toDoList.appendChild(li)
}

function onToDoSubmit(event){
    event.preventDefault(); 
    paintToDo(toDoInput.value)
    toDos.push(toDoInput.value)
    toDoInput.value = ""
    saveToDo();
}

loadToDo();
toDoForm.addEventListener("submit", onToDoSubmit);