const toDoForm = document.querySelector("#todo-form")
const toDoInput = toDoForm.querySelector("input")
const toDoList = document.querySelector("#todo-list")

var cnt = 0

function paintToDo(newToDo){
    const li = document.createElement('li');
    const span = document.createElement('span');
    const button = document.createElement('button');
    
    li.appendChild(span);
    li.appendChild(button);
    
    span.innerText = newToDo;
    button.innerText = "x";
    button.onclick = deleteToDO()
    li.id = `${cnt}`
    cnt ++
    toDoList.appendChild(li);
}

function deleteToDO(){

}

function onToDoSubmit(event){
    event.preventDefault(); 
    paintToDo(toDoInput.value)
    toDoInput.value = ""
}

toDoForm.addEventListener("submit", onToDoSubmit)