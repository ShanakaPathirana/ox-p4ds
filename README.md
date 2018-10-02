# ox-p4ds <img src="notebooks/images/oudce_logo.png"/>
Materials for [Programming for Data Science at Oxford](https://www.conted.ox.ac.uk/courses/programming-for-data-science) - **this page will be updated as the course progresses**.

Download Slack: https://slack.com/get

The class workspace on Slack is https://ox-p4ds.slack.com where you have a dedicated class channel `#mt18`. I encourage you to ask questions should you have them in the Slack channel incase your classmates can help. David (your tutor) and Massi and Ramon (your assistant tutors) will also check Slack and provide support where possible.

To use Jupyter yourself, I recommend you download and install the Anaconda Distribution, a Python Data Science Platform, from: https://www.anaconda.com/download/ Make sure you download the **Python 3** version of Anaconda.

Jupyter/Anaconda and Slack are also available to use in the Computer Teaching Room (CTR) at Rewley House.

You can also run online live versions of the notebooks that are launched by [Binder](https://mybinder.org) by clicking on the `binder` buttons below without having to install anything yourself. Please note that Binder is still in beta testing so may occasionally not work as expected.

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
- Lecture 1: https://s3.eu-west-2.amazonaws.com/ox-p4ds-assets/week1_lecture1.pdf
- Little Women notebook example [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/djcomlab/ox-p4ds/master?filepath=notebooks%2Flittle_women_example.ipynb) or download from https://github.com/djcomlab/ox-p4ds/blob/master/notebooks/little_women_example.ipynb
- Lab Exercise 1: Getting started with Jupyter Notebooks [TODO: Add this notebook (take from Jupyter Project)]

### Week 2

Python Primer.

- Lecture 2: TBC
- Practical exercise on Jupyter and getting started with Python

### Week 3

Playing with Pandas.

- Lecture 3: TBC
- Practical exercise on Python data types and functions, NumPy
- Practical exercise on tabular data with DataFrames, Pandas
- Practical challenge exercise: Mining data about the London 2012 Olympics

### Week 4

Data Visualization.

- Lecture 4: TBC
- Practical exercises on functions and data sisualizations

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

### Week 9

Course recap and Capstone Project.

### Week 10

Remaining time class time will be for working on the Capstone project.

### Capstone Project

Details of the assignment will be made available in Week 9.

*Deadline for assignment submission will be **Friday 14 December 2018, 11.59PM***.

### Links of interest
- Useful links will be added here each week.
