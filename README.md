# ox-p4ds <img src="oudce_logo.png" align="right"/>

Materials for [Programming for Data Science at Oxford](https://www.conted.ox.ac.uk/courses/programming-for-data-science) - **this page will be updated as the course progresses**.

The class workspace on **Slack** is https://ox-p4ds.slack.com where you have a dedicated class channel `#ht19`. I encourage you to ask questions should you have them in the Slack channel incase your classmates can help. David and Massi (your tutors) and Ramon (your teaching assistant) will also check Slack and provide support where possible. Download Slack from: https://slack.com/get


To use **Jupyter** yourself, I recommend you download and install **Anaconda**, a Python Data Science Platform, from: https://www.anaconda.com/download/ Make sure you download the **Python 3** version of Anaconda. You can also install Jupyter if you have a standard Python distribution installed. Ask your tutors for assistance if you need to install Jupyter on your own machine.

To get the contents of this repository I recommend that you install **Git SCM**, a source code management software, that will help you keep up-to-date with the repository. I will be adding content as the course progresses and Git will allow you to pull new material as it becomes available.

**Jupyter/Anaconda, Slack and Git are available to use in the Computer Teaching Room (CTR) at Rewley House.**

You can also run online live versions of the notebooks that are launched by **[Binder](https://mybinder.org)** by clicking on the `binder` buttons below without having to install anything yourself. Please note that Binder is still in beta testing and is hosted by *University of California, Berkeley* so may occasionally not work as expected (but is quite reliable). 

### Cloning this repository to use at home

If you want to run the notebooks on your own computer at home, apart from installing Jupyter/Anaconda as per above, you will need to install **Git**, which is a source code management software, from [here](https://git-scm.com/downloads). Once installed, you need to open up the command-line ("Command Prompt" on Windows or "Terminal" on Mac OSX) to run some commands.

Change directory to somewhere sensible, such as `My Documents` or similar on Windows or `Documents` on Mac OSX. Assuming you're using `Documents`:

```
cd Documents
```

Then ask Git to clone this repository with the following command.
```
git clone https://github.com/djcomlab/ox-p4ds/
```

This will create a subdirectory called `ox-p4ds` in your `Documents` folder. When you need to update the content at some later time after I have added some new files to the repository, you will need to open up the command-line again and do the following commands.
```
cd Documents/ox-p4ds
git pull
```
What this does is to ask Git to check if there are any new changes in the online repository and to download those new files or updates to the existing files.

Either some lines of stuff should whizz by, or it will say `Already up to date.` if there are no new changes.

If this doesn't work, you may need to force the update, which will overwrite your local files. To do this (make sure any of your own work is renamed or moved outside of the `ox-p4ds` folder first):
```
git fetch --all
git reset --hard origin/master
```

### Week 1

Introduction to Data Science.
- Lecture 1 handouts: https://goo.gl/Q3iD7p
- Exercise 1: Jupyter Notebook Basics [![nbviewer](notebooks/images/render_nbviewer_button.png)](https://nbviewer.jupyter.org/github/djcomlab/ox-p4ds/blob/master/notebooks/Ex01_Notebook_Basics.ipynb) (run on local Jupyter installation)
- Exercise 2: Running Code [![nbviewer](notebooks/images/render_nbviewer_button.png)](https://nbviewer.jupyter.org/github/djcomlab/ox-p4ds/blob/master/notebooks/Ex02_Running_Code.ipynb) [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/djcomlab/ox-p4ds/master?filepath=notebooks%2FEx02_Running_Code.ipynb)
- Exercise 3: Working with Markdown cells [![nbviewer](notebooks/images/render_nbviewer_button.png)](https://nbviewer.jupyter.org/github/djcomlab/ox-p4ds/blob/master/notebooks/Ex03_Working_With_Markdown_Cells.ipynb) [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/djcomlab/ox-p4ds/master?filepath=notebooks%2FEx03_Working_With_Markdown_Cells.ipynb)
- Exercise 4: Notebook Exercises [![nbviewer](notebooks/images/render_nbviewer_button.png)](https://nbviewer.jupyter.org/github/djcomlab/ox-p4ds/blob/master/notebooks/Ex04_Notebook_Exercises.ipynb) [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/djcomlab/ox-p4ds/master?filepath=notebooks%2FEx04_Notebook_Exercises.ipynb)
- Little Women notebook example [![nbviewer](notebooks/images/render_nbviewer_button.png)](https://nbviewer.jupyter.org/github/djcomlab/ox-p4ds/blob/master/notebooks/Week1_Little_Women.ipynb) [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/djcomlab/ox-p4ds/master?filepath=notebooks%2FWeek1_Little_Women.ipynb)

### Week 2

Python Primer.

- Lecture 2 handouts: https://tinyurl.com/ycvncsup
- Exercise 5: Getting started with Python, numbers, and functions: [![nbviewer](notebooks/images/render_nbviewer_button.png)](https://nbviewer.jupyter.org/github/djcomlab/ox-p4ds/blob/master/notebooks/Ex05_Expressions.ipynb) [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/djcomlab/ox-p4ds/master?filepath=notebooks%2FEx05_Expressions.ipynb)
- Exercise 5: Expressions (complete) [![nbviewer](notebooks/images/render_nbviewer_button.png)](https://nbviewer.jupyter.org/github/djcomlab/ox-p4ds/blob/master/notebooks/Ex05_Expressions_complete.ipynb) [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/djcomlab/ox-p4ds/master?filepath=notebooks%2FEx05_Expressions_complete.ipynb)

### Week 3

Playing with Pandas.

- Lecture 3 handouts: https://goo.gl/H51dVE
- Exercise 6: Data Types [![nbviewer](notebooks/images/render_nbviewer_button.png)](https://nbviewer.jupyter.org/github/djcomlab/ox-p4ds/blob/master/notebooks/Ex06_Data_Types.ipynb) [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/djcomlab/ox-p4ds/master?filepath=notebooks%2FEx06_Data_Types.ipynb)
- Exercise 7: Tables [![nbviewer](notebooks/images/render_nbviewer_button.png)](https://nbviewer.jupyter.org/github/djcomlab/ox-p4ds/blob/master/notebooks/Ex07_Tables.ipynb) [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/djcomlab/ox-p4ds/master?filepath=notebooks%2FEx07_Tables.ipynb)
- Exercise 8: Data Cleaning and Analysis (challenge) [![nbviewer](notebooks/images/render_nbviewer_button.png)](https://nbviewer.jupyter.org/github/djcomlab/ox-p4ds/blob/master/notebooks/Ex08_Data_Cleaning_and_Analysis.ipynb) [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/djcomlab/ox-p4ds/master?filepath=notebooks%2FEx08_Data_Cleaning_and_Analysis.ipynb)
- Week 3 Live notebook [![nbviewer](notebooks/images/render_nbviewer_button.png)](https://nbviewer.jupyter.org/github/djcomlab/ox-p4ds/blob/master/notebooks/Week3_Live.ipynb) [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/djcomlab/ox-p4ds/master?filepath=notebooks%2FWeek3_Live.ipynb)
- Week 3 Live notebook 2 [![nbviewer](notebooks/images/render_nbviewer_button.png)](https://nbviewer.jupyter.org/github/djcomlab/ox-p4ds/blob/master/notebooks/Week3_Live2.ipynb) [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/djcomlab/ox-p4ds/master?filepath=notebooks%2FWeek3_Live2.ipynb)
- Link to evaluation form: https://goo.gl/forms/H2KKr2acQDetDhbl1

### Week 4

Data Visualization.

- Lecture 4: TBC
- Practical exercises on functions and data visualizations

### Week 5

Big Data.

- Lecture 5: TBC
- Practical excersises on data formatting and MapReduce

### Week 6

Getting data from public sources.

- Lecture 6: TBC
- Practical exercises on getting data from Twitter

### Week 7

Machine Learning.

- Lecture 7: TBC
- Practical exercise on a simple Machine Learning
- Practical exercises on Sentiment Analysis

### Week 8

Sharing analyses.

- Lecture 8: TBC
- Practical exercises on documentation in notebooks using Markdown
- Practical exercise on publishing your work on GitHub and Binder

### Week 9

Course recap and Capstone Project.

### Week 10

Remaining time class time will be for working on the Capstone project.

### Capstone Project

Details of the assignment will be made available in Week 6.

*Deadline for assignment submission will be **TDB April 2019, 11.59PM***.

### Links of interest
- [Project Gutenberg](www.gutenberg.org/ebooks/). A free resources of public domain ebooks; nice source of natural language data to play with.
- [Python for Everybody (online book)](https://www.py4e.com/html3/). An excellent introduction to the core parts of Python 3 programming. Chapters 1-9 are most relevant.
- [A simple overview of Python variables, expressions and statements](https://www.pythonlearn.com/html-008/cfbook003.html).
- Useful links will be added here each week.
