import streamlit as st
import numpy as np
from MonicPoly3RootFinder import *
from plotter import GetAxes
# import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import cmath

def home():
    st.title("Home Page")
    st.write("Welcome to the Home Page!")

def about():
    st.title("About Us")
    st.write("Welcome to the About Us Page!")
    st.write("We are a team of math enthusiasts dedicated to promoting mathematical analysis.")

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

def project_3():
    a = st.number_input("a", value=1.0, step=1.0)
    b = st.number_input("b", value=2.0, step=1.0)
    c = st.number_input("c", value=3.0, step=1.0)
    x = st.number_input("Range to draw function around the root", min_value=0, value=10)

    f = lambda x: x**3 + a*x**2 + b*x + c
    r, bisectionXes = MonicPoly3Root(a, b, c)
    X, Y = GetAxes(f, r - x/2, r + x/2, 10000)
    # st.text(f"f(x) = x^3 + ({a})x^2 + ({b})x + ({c})")
    sign = lambda x: "+" if x > 0 else "-"
    st.latex(f'f(x) = x^3 {sign(a)} {abs(a)}x^2 {sign(b)} {abs(b)}x {sign(c)} {abs(c)}')
    st.text(f"Root: {r} (red line, error of 1E-9)")
    st.text(f"Starting values for bisection: a = {bisectionXes[0][0]}, b = {bisectionXes[0][1]} (green lines)")
    st.text(f"f(a) = {f(bisectionXes[0][0])}, f(b) = {f(bisectionXes[0][1])}")

    
    df = pd.DataFrame({'x':X, 'f': Y}).set_index('x')

    chart = px.line(df).update_layout(xaxis_title='x', yaxis_title="f")
    chart.add_hline(y=0, line=dict(color='white'))
    chart.add_vline(x=bisectionXes[0][0], line=dict(color='green'))
    chart.add_vline(x=bisectionXes[0][1], line=dict(color='green'))
    chart.add_vline(x=r, line=dict(color='red'))
    st.plotly_chart(chart)
    for item in bisectionXes:
        item += [f(item[0]), f(item[1])]
    
    df = pd.DataFrame(bisectionXes, [f"Iteration {x + 1}" for x in range(bisectionXes.__len__())], ['a', 'b', 'f(a)', 'f(b)'])
    st.text("Bisection method data:")
    df.style.format(precision=9)
    st.dataframe(df, column_config={
        'a': st.column_config.NumberColumn(format="%.8f"),
        'b': st.column_config.NumberColumn(format="%.8f"),
        'f(a)': st.column_config.NumberColumn(format="%.8f"),
        'f(b)': st.column_config.NumberColumn(format="%.8f"),
    }, use_container_width=True)

def project_4():
    s1 = st.number_input("$\sigma_1$", min_value=0.0, value=1.0, step=1.0)
    s2 = st.number_input("$\sigma_2$", min_value=0.0, value=2.0, step=1.0)
    a = st.number_input("A", min_value=0.0, value= 1.0, step=1.0)
    x = st.number_input("Range to draw function", min_value=0.0, value=10.0, step=10.0)

    error = False
    if (s1 == 0): 
        st.error("$\sigma_1$ cannot be 0")
        error = True
    if (s2 == 0): 
        st.error("$\sigma_2$ cannot be 0")
        error = True
    if (s1 >= s2): 
        st.error("$\sigma_1$ cannot be $\geq \sigma_2$")
        error = True

    if not error:
        f = lambda x: a*(float(cmath.e)**(-s1*x) - float(cmath.e)**(-s2*x))/(s2 - s1)
        X, Y = GetAxes(f, 0, x, 10000)

        m = (cmath.log(s2/s1)/(s2 - s1)).real

        df = pd.DataFrame({'x': X, 'C': Y}).set_index('x')

        chart = px.line(df).update_layout(xaxis_title='t', yaxis_title="C")
        chart.add_vline(x=m, line=dict(color='red'))

        curlyOpen = r'{'
        curlyClose = r'}'

        st.latex(f'C(t) = \\frac{curlyOpen}{a}{curlyClose + curlyOpen}{s2} - {s1}{curlyClose}(e^{curlyOpen}{-s1}t{curlyClose}-e^{curlyOpen}{-s2}t{curlyClose})')
        st.text(f'Maximum: C({m}) = {f(m)}' if a != 0 else 'Maximum C(0) = 0')

        st.plotly_chart(chart)


# Create a dictionary of page names and corresponding functions
pages = {
    "Home": home,
    "About Us": about,
    "Proyecto 1": proyect_1,
    "Proyecto 3": project_3,
    "Proyecto 4": project_4
}

# Create a sidebar to navigate between pages
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(pages.keys()))

# Run the selected page function
pages[selection]()