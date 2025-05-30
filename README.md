# Linear Equation Lesson Demo

The project was built in a conda environment using Python 3.9. The only package that was installed was `streamlit` and there are no other dependencies. 

The demo can be accessed [here](https://shifubear-linear-equation-lesson-demo-app-vu7jyt.streamlit.app/demo). The `demo` page contains the requested interactive quiz. 

To run the app locally, use 
```
$ streamlit run demo_app.py 
```

The requested application of an interactive linear equation quiz is contained in the file `demo.py`. I spent some extra time to explore page navigation and an "example" page where the reader learns how to solve the given problem. From opening the project description to have a working quiz took about 75 minutes. In total I spent about three hours on the app. 

`demo.py` has two constant variables `MAX_VAL` and `MIN_VAL` which I thought of as config variables that an instructor would setup before assigning the app to students. These are the upper and lower bounds that can appear for the values a, b, c. The demo correctly generates instances whose solutions are integers, and `MIN_VAL` <= a, b, c <= `MAX_VAL`. 

