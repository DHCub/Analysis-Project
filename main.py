import streamlit as st

def home():
    st.title("Home Page")
    st.write("Welcome to the Home Page!")

def about():
    st.title("About Us")
    st.write("Welcome to the About Us Page!")
    st.write("We are a team of math enthusiasts dedicated to promoting mathematical analysis.")

def function_selection():
    st.title("Function Selection")

    st.write("Welcome to the Function Selection Page!")
    st.write("Select the functions you want to use.")

    functions = {
        "Función 1: División de Polinomios": function1,
        "Función 2: División de Logaritmo y Polinomio": function2,
        "Función 3: División de Seno y Polinomio": function3,
        "Función 4: División de Polinomio y Exponencial": function4,
        "Función 5: División de Arcotangete y Polinomio": function5
    }

    selected_functions = st.multiselect("Seleccione la función", list(functions.keys()))

    for function in selected_functions:
        functions[function]()

def function1():
    st.title("Función 1")

    st.write("Welcome to Function 1!")
    st.write("Enter the parameters for Function 1 below:")

    param1 = st.text_input("Parameter 1:")
    param2 = st.text_input("Parameter 2:")

    # Add your function 1 code here
    if param1 and param2:
        st.write("Function 1 Result:")
        st.write("Parameter 1:", param1)
        st.write("Parameter 2:", param2)
        # Add your function 1 logic here

def function2():
    st.title("Function 2")

    st.write("Welcome to Function 2!")
    st.write("Enter the parameters for Function 2 below:")

    param1 = st.text_input("Parameter 1:")
    param2 = st.text_input("Parameter 2:")

    # Add your function 2 code here
    if param1 and param2:
        st.write("Function 2 Result:")
        st.write("Parameter 1:", param1)
        st.write("Parameter 2:", param2)
        # Add your function 2 logic here

def function3():
    st.title("Function 3")

    st.write("Welcome to Function 3!")
    st.write("Enter the parameters for Function 3 below:")

    param1 = st.text_input("Parameter 1:")
    param2 = st.text_input("Parameter 2:")

    # Add your function 3 code here
    if param1 and param2:
        st.write("Function 3 Result:")
        st.write("Parameter 1:", param1)
        st.write("Parameter 2:", param2)
        # Add your function 3 logic here

def function4():
    st.title("Function 4")

    st.write("Welcome to Function 4!")
    st.write("Enter the parameters for Function 4 below:")

    param1 = st.text_input("Parameter 1:")
    param2 = st.text_input("Parameter 2:")

    # Add your function 4 code here
    if param1 and param2:
        st.write("Function 4 Result:")
        st.write("Parameter 1:", param1)
        st.write("Parameter 2:", param2)
        # Add your function 4 logic here

def function5():
    st.title("Function 5")

    st.write("Welcome to Function 5!")
    st.write("Enter the parameters for Function 5 below:")

    param1 = st.text_input("Parameter 1:")
    param2 = st.text_input("Parameter 2:")

    # Add your function 5 code here
    if param1 and param2:
        st.write("Function 5 Result:")
        st.write("Parameter 1:", param1)
        st.write("Parameter 2:", param2)
        # Add your function 5 logic here


# Create a dictionary of page names and corresponding functions
pages = {
    "Home": home,
    "About Us": about,
    "Function Selection": function_selection
}

# Create a sidebar to navigate between pages
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(pages.keys()))

# Run the selected page function
pages[selection]()