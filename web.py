import streamlit as st
import functions

todos = functions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title ("My Todo App") #h1 title
#st.subheader("This is my todo app") h2 title
#st.write("This is a simple todo app to keep track of your tasks.") # h3 title or a simple text

#st.checkbox("Buy groceries") # checkbox

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo) # checkbox key=todo afiseaza toata lista si daca se bifeaza un todo, se schimba starea de la false la true
    if checkbox:
        todos.pop(index) #elimina todo din lista
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun() #reruleaza codul pentru a afisa lista actualizata

st.text_input(label="", placeholder="Add a new todo",
              on_change=add_todo, key="new_todo") # text input 
              #on_change apeleaza functia care contine evenimentul de adaugare
#st.session_state #afiseaza dictionarul de stari
