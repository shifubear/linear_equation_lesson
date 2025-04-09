# Linear Equation Lesson Demo

The project was built in a conda environment using Python 3.9. The only package that was installed was `streamlit` and there are no other dependencies. 

To run the app, use 
```
$ streamlit run demo_app.py 
```

The requested application of an interactive linear equation quiz is contained in the file `demo.py`. I spent a little bit of extra time to explore page navigation and an "example" page where the reader learns how to solve the given problem. 

`demo.py` has two constant variables `MAX_VAL` and `MIN_VAL` which I thought of as config variables that an instructor would setup before assigning the app to students. These are the upper and lower bounds that can appear for the values a, b, c. The demo correctly generates instances whose solutions are integers, and all the numbers appearing in the UI are clamped between custom variables. 

