import streamlit as st
from streamlit.errors import DuplicateWidgetID
import functions
import time

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"]+ "\n"
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ''


st.title("My Todo App")
st.subheader("This is Daniel's todo app built to increase productivity")

for index, todo in enumerate(todos):
    try:
        checkbox = st.checkbox(todo, key=todo)
    except DuplicateWidgetID:
        info_message = st.empty()
        info_message.info("This todo is already on the todo list.")
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        time.sleep(1)
        info_message.empty()
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label="", placeholder="Add new todo...", 
            on_change=add_todo, key="new_todo",
            value=st.session_state.get('new_todo', ''))