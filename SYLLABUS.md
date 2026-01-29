# dtsc330_26

A repository of course materials for Duquesne University's Data Science 330 course, 2026.

In this class, we are a data science team with expectations to match. You are welcome to ask others for help, but at the same time are required to do your own work.

Note that grading is unusual in this course. Given that we are a data science team, you will not receive grades in Canvas. Instead, we will have a Performance Review halfway through the semester and a job interview at the end of the semester. See _Grading_ below.

# Syllabus

Each day we will alternate theory with practice. Practice will involve both my coding in front of you, as well as taking turns coding in front of each other. Given that many job interviews require public coding, this is excellent, if occasionally challenging experience.

Note that we will adapt later weeks of the course to the interests of everyone in the course.

# Grading

It is easy to do well in this course. Seriously. Show up, engage, have fun, take notes, do the homework, and complete the programming homework throughout the semester.

Because we are a data science team, treat this as you would a job. It matters that you show up and that you show interest. I'd much rather work with someone who is engaged than someone who plays on their phone.

As such, you will not receive grades in Canvas. Instead, we will cover your grade during the midterm Performance Review and the final exam Job Interview. You may at any time ask how you are doing.

Grades in this class are based on creating tools that are readable, runnable, and well-documented. 60% of the grade is code quality, 40% is documentation quality.

For the exceptionally few students who need external pressure to show up to class on time, attendance is essential. Grades will decrease exponentially based on the number of days missed (-1%, -2%, -4%, -8%... for 1-4 days respectively).

Ample time will be given for homeworks, and they should be viewed both as a chance to practice and a mechanism of expanding the documented code in your Github (which will help with future jobs). Collaboration is highly valued, but if overly similar code is submitted, I reserve the right to request independent explanations of how the code works and the thought behind its organization. Push commits to Github _before the deadline_. Each deadline is far in the future. If code appears to be duplicated and is committed in a single entry after the commits of matching code, the history of the code becomes clear.

It is worth noting that Github records the time of every file uploaded. That timestamp will be used to determine if the homeworks are submitted on time.

If you are concerned about the final exam, you are welcome to meet with me to do a practice prior to the exam. Whether you've completed the homework and documented it well is obvious. But, if you are concerned with whether or not you are sufficiently participating, you can schedule time to chat about it at any point during the semester, and we can talk about mechanisms of improvement if necessary. Given these open channels of communication, however, requests to change a grade at the end of the semester will not go well. Assume that I am giving you the benefit of the doubt.

## Performance Review

Feb 23 - Mar 14

You can schedule the 1:1 15 minute Performance Review any time in those two weeks. To prepare for the review, please do the following:

1. For each of your assignments up to that day, report the number that were completed _on time_.
   - Is there high-quality documentation?
   - Does the code run?
2. For each day of class, report the number of days that you attended _on time_.
3. Give an assessment of your understanding of the course material.
   - How many times did you use Generate AI assistance?
   - Can you describe machine learning models?
   - How do you choose which ML model to use?

I may ask some questions to determine your understanding. From the performance review, you will receive your current grade. If our assessments align, that provides a small opportunitiy for bonus points.

## Final exam

The final exam will be a mock job interview. It will be comprised of the following portions:

- Evaluation of Github, all of which will be filled in the previous weeks (is there high-quality Python code with functions, documentation, and a cohesive project): 40% (If you cared about your work during the semester and have put substantial effort into your Github, the weight of the coding challenge will decrease and the weight of the Github will increase.)
- Description of previous work: 40%
- Coding challenge: 20%

## Academic Integrity

It seems unnecessary to mention this, but students must submit their own work, not that of other students, associates, or Generative AI Models. Failures in academic integrity will result in a 0 on the assignment and additional testing of the topic area during the final.

### Generative AI

As discussed in class, you can test ideas with Generative AI but you cannot complete your homework with it. Overuse of Gen AI will be apparent if you are unable to pass the coding challenges during the final exam.

## Disability Services

If you have any concerns related to disabilities or accomadations, please contact the Office of Disability Services, 309 Duquesne Union, at 412.396.6658 or disabilityservices@duq.edu and contact me in the first week so that we can work together to meet your accomadations.

## Health and Wellness

Your mental health and wellbeing matter. Our Center for Student Wellbeing provides health services, recreation opportunities, and counseling. From therapeutic services to support your overall wellbeing to therapy services that can help with a specific health, psychological, or spiritual issue, the Center for Student Wellbeing, along with Spiritan Campus Ministry, are here for you.

You can learn more about any of our Center for Student Wellbeing Resources and Services at https://www.duq.edu/life-at-duquesne/health-recreation-wellness/index.php

- Counseling Services
  https://www.duq.edu/life-at-duquesne/health-recreation-and-counseling/counseling-services
- Health Services
  https://www.duq.edu/life-at-duquesne/health-recreation-and-counseling/health-services
- Recreation Services
  https://www.duq.edu/life-at-duquesne/health-recreation-and-counseling/recreation-services
- Oasis Mental Health and Wellbeing App
  The Oasis App is available on the App Store and the Google Play Store. You can also find it by searching for “Oasis Mental Health” in the App Store or Play Store.
- Spiritan Campus Ministry
  https://www.duq.edu/life-at-duquesne/spiritan-campus-ministry

# Code necessities

I highly recommend using a unix-based system for programming-- either dual-boot a windows machine with Ubuntu or use a Mac. The computer lab is fantastic and has computers that can boot into Ubuntu. If necessary, then the easiest way to use Python on a Windows machine is using a combination of Anaconda and Git Bash.

To install Git bash: https://git-scm.com/download/win

(Given that Anaconda was used in DS1, I am assuming that you have already installed Anaconda.)

To ensure that you can use Anaconda from within Git Bash, checkout the first answer to this Stack Overflow question: https://stackoverflow.com/questions/54501167/anaconda-and-git-bash-in-windows-conda-command-not-found

It may seem weird that a course syllabus links to Stack Overflow, but you will find that the professional experience of Data Science often involves using Google for solutions. Installing core Unix components is one of the most frustrating tasks in computing, regardless of operating system, but doing so provides excellent experience.

## SSH Issues

For Github, if you want to use ssh, there are a variety of ways to deal with this.

1. PyCharm: https://www.jetbrains.com/help/pycharm/create-ssh-configurations.html
1. Github more generally: https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent

## Slack

You may have noticed that you've been sent a slack invite. This is never required, but it's an easy way to contact me if you have questions. It's also a great place to ask other folks in the class questions that you might have. There's nothing worse than getting stuck programming, and having others around is key.

## Notes

1. Set up your own Github account
1. Github accounts should include at least one example of Python, with docstrings
1. I recommend using VSCode + poetry (historically venv) for installation
1. Let's use Python 3.8+

# Schedule

## Week 1 - Jan 12

- Discuss everyone's backgrounds
- Discuss each student's desired outcomes from the course
- VSCode/local coding
  - Install VSCode
- Code documentation
  - Fuctions
  - Type hinting
  - Docstrings
  - Libraries versus scripts
  - Colab vs VSCode
- Github
  - Setup
  - READMEs
  - gitignore
  - cloning
  - adding
  - commiting
  - pushing
  - pulling
  - branching
  - diff
- Go over some cool models from industry
  - Spotify
  - ChatGPT, quickly
- Discuss features and labels

Homework 1 due Jan 25:

- Set up Github account, add at least one repository with documentation
- Email the link to your account to me
- Set up VSCode locally

## Week 2 - Jan 26

Dataset for Grants: https://reporter.nih.gov/exporter
Dataset for Articles: https://ftp.ncbi.nlm.nih.gov/pubmed/updatefiles/

- Rules for ChatGPT and why
- CVs/Resumes
  - Focus on projects
  - Improve your Github
  - Match keywords from job descriptions
- Pandas
  - All Pandas, all the time
  - What is Pandas?
    - Numpy-based, which is C-based
  - Comfort and speed
  - Good habits such as apply
  - Bad habits such as for loops
  - Data merging
- Pandas is easy, efficiency is hard
- Numpy/Pandas translation
- Grants data reading function

Homework 2 due Feb 1:

- How do you fill in the missing dates from the grants data?
- PI_NAMEs contains multiple names. We can only connect individual people. Can you make it so that we can get "grantees"?
- The dates for Articles are problematic. Can you fix them?

Add your thinking to your README.md file in a section titled `## Homework 2`.

## Week 3 - Feb 2

- Classification introduction
  - Examples of classification in data science
- Create a reusable function for training a classifier
- Create a reusable function for saving a classifier
- Create a reusable function for loading and running a classifier
  - Scikit-learn

## Week 4 - Feb 9

- Talk about the hackathon
- Talk about Semantle
- Decision trees slides
  - Random forest
  - XGBoost
- Download the wine quality dataset: https://archive.ics.uci.edu/dataset/186/wine+quality
  - Use it with an xgboost model
- Natural language processing
  - spacy
  - fasttext
  - nltk
- Download the weekly incremental NPI file: https://download.cms.gov/nppes/NPI_Files.html

## Week 5 - Feb 16

NOTE: Installing fasttext on python 3.12 or higher requires a workaround:

```
poetry add git+https://github.com/cfculhane/fastText
```

- Return to Semantle as an example of word2vec
- Compare on the screen the reader functions submitted by each person
- Use one to load data
- Talk about bias in data
  - Finance field, zip code
  - Amazon hiring
  - Judicial predictions
- Create a function together to produce entity resolution features
- How to create training data
  - Simulation
  - Hand-labeling
  - Recursive
- Recursive model training
  - Bias
  - Bootstrapping + class mislabels

## Week 6 - Feb 23

The day of code

- Talk through everyone's classifier
- Create training data together (20-100 entries only)
- Combine together the functions to be able to train data
- Create sequential training data

The "blocking" problem

- Blocking problem and nearest neighbor indices
- Combine together to create a tool to classify the two datasets

## Week 7 - Mar 9

- How has each person addressed the blocking problem?
- How has each person created a training set?
  - We need more data. Let's use a database

- Why a database?
  - Keeps data in sync between people
  - Designed for fast reading
  - Consistency
- Short database types overview
  - No SQL (e.g. MongoDB)
  - SQL
  - ETL (Extract, Transform, Load)
  - Spark
    - Databricks
- SQL introduction
  - SQLite v MySQL v Postgres
  - CREATE
  - row types
- Data tables
- Bridge tables
  - Relationships between tables

- Create database for our two datasets
- Create bridge table

- Embed and Blocking

## Week 8 - Mar 16

- Each person explains their current state

- Continue with SQL
  - SELECT and INSERT
  - DELETE FROM
  - JOIN
  - WHERE

- NetworkX and connected components
- Store training data in database

## Week 9 - Mar 23

- You know that prep-before-the-midterm thing? That's this week. You've been working hard to get your code organized. We're going to start from scratch and reproduce everything, covering whatever questions you have. We will end with a working implementation of the entire pipeline based on everything we've learned, beginning with a brand-new repository. It is essential that you use this chance to ask all of those burning questions.

## Week 10 - Mar 30

- Finishing up the review from Week 9
- Focus on creating a dataset and training the model
  - Reiterate using edge cases to improve model performance
  - Cover the "blocking" process again
    - Embedding + nearest neighbors
    - By last name

## Week 11 - Apr 13

- Go through the final file-- pushed to week 13
- Autoencoder in tensorflow
- Create our own neural network library

## Week 12 - Apr 20

- Finish the autoencoder in tensorflow, training it on the wine quality dataset
- Finish the neural network library
- Apply tensortango (the NN library) to the wine quality dataset
- Consider how CNNs are a minor variant of what we've built

## Week 13 - Apr 27

This week is a grab-bag based on requests.

- Flask
- AWS
  - EC2
  - RDS
- Google cloud
  - Firebase
- Feature engineering
- TF-IDF
- Tokenization
- Image augmentation
- Standardizing pixels

## Final Exam

Schedule the Final 1:1 over Zoom.

A job interview in which we evaluate your entire Github, as well as ask questions on topics covered throughout the course
