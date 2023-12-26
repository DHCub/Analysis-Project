import streamlit as st
import numpy as np
from MonicPoly3RootFinder import *
from plotter import GetAxes
# import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px

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

def logistic_map(r, x0, n):
    """
    Calculates the first n terms of the logistic map.

    Args:
        r: The bifurcation parameter.
        x0: The initial value.
        n: The number of terms to calculate.

    Returns:
        A NumPy array containing the first n terms of the logistic map.
    """
    x = np.zeros(n)
    x[0] = x0
    for i in range(1, n):
        x[i] = r * x[i-1] * (1 - x[i-1])
        print(f"x{i} = {x[i]}")
    return x

def proyect_1():
    min_r = 0.0
    max_r = 4.0

    r_value = st.slider("R value", value=min_r, max_value=max_r, step=0.000001)
    st.write("value of r:", r_value)
    print(f"{r_value}")

    min_x = 0.0
    max_x = 1.0

    x_value = st.slider("X0 value", value=min_x, max_value=max_x, step=0.000001)
    st.write("value of x0:", x_value)
    print(f"{x_value}")

    n_terms = 100

    def update():
        x = logistic_map(r_value, x_value, n_terms)
        for i in range(100):
            x[i] = x[i]
        line = st.line_chart(x)
    update()

def project_4():
    a = st.number_input("a", min_value=-100.0, max_value=100.0, value=1.0, step=1.0)
    b = st.number_input("b", min_value=-100.0, max_value=100.0, value=2.0, step=1.0)
    c = st.number_input("c", min_value=-100.0, max_value=100.0, value=3.0, step=1.0)
    x = st.number_input("Range to draw around the root", min_value=0, value=10)

    f = lambda x: x**3 + a*x**2 + b*x + c
    r, bisectionXes = MonicPoly3Root(a, b, c)
    X, Y = GetAxes(f, r - x/2, r + x/2)
    st.text(f"f(x) = x^3 + ({a})x^2 + ({b})x + ({c})")
    st.text(f"Root: {r} (red line, error of 1E-9)")
    st.text(f"Starting values for bisection: a = {bisectionXes[0][0]}, b = {bisectionXes[0][1]} (green lines)")
    st.text(f"f(a) = {f(bisectionXes[0][0])}, f(b) = {f(bisectionXes[0][1])}")

    df = pd.DataFrame({'x':X, 'f': Y}).set_index('x')

    chart = px.line(df)
    chart.add_hline(y=0, line=dict(color='white'))
    chart.add_vline(x=bisectionXes[0][0], line=dict(color='green'))
    chart.add_vline(x=bisectionXes[0][1], line=dict(color='green'))
    chart.add_vline(x=r, line=dict(color='red'))
    st.plotly_chart(chart)

# Create a dictionary of page names and corresponding functions
pages = {
    "Home": home,
    "About Us": about,
    "Function Selection": function_selection,
    "Proyecto 1": proyect_1,
    "Proyecto 4": project_4
}

# Create a sidebar to navigate between pages
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(pages.keys()))

# Run the selected page function
pages[selection]()