import streamlit as st

# Initialize Session Variables

if "section1_complete" not in st.session_state:
  st.session_state.section1_complete = False
if "section2_complete" not in st.session_state:
  st.session_state.section2_complete = False
if "section3_complete" not in st.session_state:
  st.session_state.section3_complete = False
if "section1_last_words" not in st.session_state:
  st.session_state.section1_last_words = ""

# Utility functions for navigation

def quiz_1_completed():
  if st.session_state.quiz1 == "$2x - 3 = y$":
    st.session_state.section1_last_words = "That one is linear, but it has two variables. Try again!"
  elif st.session_state.quiz1 == "$4x + 3 = 11$":
    st.session_state.section1_last_words = "That is correct! Let's keep going."
    st.session_state.section1_complete = True
  elif st.session_state.quiz1 == "$x^2 - 10 = 15$":
    st.session_state.section1_last_words = "That one has only one variable, but it is not linear. Try again!"

def section2_completed():
  st.session_state.section2_complete = True

def section3_completed():
  st.session_state.section3_complete = True


# Content
## Section 1

st.write("""
# Linear Equations in One Variable 

In this section we will learn how to solve linear equations with a single variable. An equation is linear if all of its variables have order 1, and we will start with the case where there is only one such variable.
         """)

with st.form("quiz1"):
  quiz_1_answer = st.radio(
    "Select the linear equation in one variable.",
    ["$2x - 3 = y$", "$4x + 3 = 11$", "$x^2 - 10 = 15$"],
    key="quiz1",
    disabled=st.session_state.section1_complete
  )

  quiz_1_button = st.form_submit_button(
    on_click=quiz_1_completed
  )

st.write(st.session_state.section1_last_words)

## Section 2

if st.session_state.section1_complete:
  st.write("""
           To begin, we will focus on equations of the form 
           $a x + b = c$
           where $x$ is the variable we are solving for, and $a$, $b$, and $c$ are integers. 

           An example of this is the equation 
  
           $$2x - 5 = 7$$. 
           
           The goal of these problems is to rearrange the equation so that we have an expression of the form $x = m$ for some value $m$. Let's see how we might do this in our example.


  """)

  section2_complete_button = st.button(
    "Show me how",
    on_click=section2_completed
  )

## Section 3

if st.session_state.section2_complete:
  st.write("""
           The first thing we want to do is move all terms that don't involve $x$ to the right hand side. We can do this in our example by adding 5 to each side, giving us 

           $$(2x - 5) + 5 = 7 + 5$$

           $$2x = 12$$
           
           Next, we divide both sides by the coefficient of our variable $x$ which is 2 in this example. After dividing both sides by 2, we get 

           $$x = 6$$.
           """)

  section3_complete_button = st.button(
    "Great! Am I done?",
    on_click=section3_completed
  )

## Section 4

if st.session_state.section3_complete:
  st.write("""
           It's always a good idea to make sure that you have the right answer by plugging in your solution to the first equation. Let's try this together. 

           If we plug in our solution of $x = 6$ to the first equation, we have 

           $$2 \cdot 6 - 5 = 7$$

           $$12 - 5 = 7$$

           $$ 7 = 7 $$

           which is a true statement! It looks like we solved the linear equation correctly. Great job! Can you solve the practice problems? 
           """)
  
  if st.button("Practice"):
    st.switch_page("demo.py")
