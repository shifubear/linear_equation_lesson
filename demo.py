import streamlit as st
import numpy as np
import pandas as pd
import random

# Instructor or Curriculum defined variables
#   The range of integers allowed both as part of the linear equation and the solution. 
#   In a full app these would be read from a meta file the instructor can edit more easily.
MIN_VAL = -30
MAX_VAL = 30

# Initialize Session Variables
if "feedback_text" not in st.session_state:
    st.session_state.update({
        "feedback_text": "",
        "student_input": 0,
    })

def generate_new_problem():
    del st.session_state.computed

# Generate a new instance of a problem
if "computed" not in st.session_state or not st.session_state.computed:
    def random_sign() -> int:
        return (-1) ** random.randint(0, 2)

    # First, generate x
    x = random_sign() * random.randint(1, int(np.sqrt(MAX_VAL)))

    # Next, generate a such that the product |ax| is at most 2*MAX_VAL 
    a_max = MAX_VAL // abs(x)
    a = random_sign() * random.randint(1, a_max)

    # Next, split the product ax into a sum of two terms -b + c.
    product = a * x
    if product > 0:
        b = random.randint(MIN_VAL, MAX_VAL - product)
    elif product < 0:
        b = random.randint(MIN_VAL - product, MAX_VAL)
    else: 
        raise ValueError("Product is 0")
    c = product + b

    # Sometimes b = 0, so quick fix to avoid that
    if b == 0:
        if c < 0:
            b -= 1
            c += 1
        else: 
            b += 1
            c -= 1

    st.session_state.a = a
    st.session_state.b = b
    st.session_state.c = c
    st.session_state.x = x
    st.session_state.computed = True

# CONTENT

st.write(f"""
         # Practice Problems

         Solve ${st.session_state.a}x {"+" if st.session_state.b >= 0 else "-"} {np.abs(st.session_state.b)} = {st.session_state.c}$""")

with st.form(key="my_form"):
    col1, col2 = st.columns(
        [1, 10],
        gap="small",
        vertical_alignment="center"
    )
    with col1:
        st.write("$x = $")  # Custom label text
    with col2:
        student_input = st.number_input(
            "x = ",
            label_visibility="collapsed",
            min_value=MIN_VAL,
            max_value=MAX_VAL,
            step=1,
            value=None,
            key="student_input"
        )
    

    submit_button = st.form_submit_button("Submit")

if submit_button:
    correct = st.session_state.student_input == st.session_state.x
    if correct:
        st.write("Great job, that is correct!")
    else:
        st.write(f"""
                 That is incorrect. The answer is $x = {st.session_state.x}$. 
                 
                 To solve this problem, we first want to move all terms that don't use $x$ to the right. In this case, we would first {"subtract "+ str(st.session_state.b) + " from" if st.session_state.b >= 0 else "add " + str(st.session_state.b) + " to"} both sides to get 
                 
                 $${st.session_state.a}x = {"" if st.session_state.c - st.session_state.b >= 0 else "-"} {np.abs(st.session_state.c - st.session_state.b)}.$$

                 Then, we divide both sides by {st.session_state.a} to get the answer

                 $x = {st.session_state.x}$
                 """)
          
    # st.write(f"You entered: {st.session_state.student_input}. This is {'Correct' if st.session_state.student_input == st.session_state.x else 'Incorrect'}. The correct answer is {st.session_state.x}")

    reset_button = st.button(
        "Try another problem",
        on_click=generate_new_problem
    )

