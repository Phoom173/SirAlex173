from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from typing import List, Dict, Optional

app = FastAPI()

templates = Jinja2Templates(directory="templates")

# Temporary storage for todos (in-memory)
todos: List[Dict[str, str]] = []
next_id: int = 1

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "todos": todos})

@app.post("/create-todo")
def create_todo(item: str = Form(...)):
    global next_id
    todo_item = {"id": str(next_id), "item": item, "owner": owner.lower()}
    todos.append(todo_item)
    next_id += 1
    return RedirectResponse("/", status_code=303)

@app.put("/todos/{todo_id}")
    request_owner = owner.lower()
    