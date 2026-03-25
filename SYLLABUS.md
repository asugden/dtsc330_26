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
   - How many times did you use Generative AI assistance?
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
- What are LLMs?
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
- Grants data reading class
- Articles reading class

Homework 2 due Feb 1:

- How do you fill in the missing dates from the grants data?
- PI_NAMEs contains multiple names. We can only connect individual people. Can you make it so that we can get "grantees"?
- The dates for Articles are problematic. Can you fix them?

Add your thinking to your README.md file in a section titled `## Homework 2`.

## Week 3 - Feb 2

Sign up for the Grefenstette Hackathon! https://www.duq.edu/research/centers-and-institutes/grefenstette-center/hacking4humanity.php

- There is _no better way_ to learn about coding than to do it
- Use your DTSC220 and 330 skill for an amazing goal
- Win $1000

Dataset: https://physionet.org/content/sleep-accel/1.0.0/labels/#files-panel

- Download the ZIP file
- This will take 30 minutes

- Code review of example answers
- Reiterate file structure found in README.md
- Classification introduction
  - Reminder of features vs labels
  - Examples of classification in data science
- Create a reusable function for training a classifier
- Create a reusable function for saving a classifier
- Create a reusable function for loading and running a classifier
  - Scikit-learn
- Time permitting, a discussion of why we choose the models we do
  - Black box vs open box
  - Parameters
  - Complexity

Homework 3 due Feb 8

- Create the best possible classifier of sleep from acceleration and heart rate
  - If we have not finished the associated readers by the end of class, you will have to complete these readers yourself
- The classifier should be written using the technique used in class:
  1. Code should have docstrings
  1. The outermost code you write should be in a script that imports and uses reusable_classifier (or a specific version thereof)
  1. The code should also import and use any necessary readers
  1. Any transformations to the raw data should be done in the reader
- As before, please add a short description to your README that returns the performance of your model and no more than one paragraph on why you chose the features you did

## Week 4 - Feb 9

- Discuss Homework 3
  - How did you let the algorithm understand "baseline"?
  - Train-test split in temporal data
  - Strictly reference the layout in this repository:
    - No `__init__.py` in `scripts/`
    - Only file readers in `readers/`
    - Scripts vs libraries
  - Come up with other uses for this kind of classifier 
- ChatGPT and the Brain
- Decision trees slides
  - Random forest
  - XGBoost
- Semantle as an introduction to Natural Language Processing (NLP)
  - https://semantle.com/
- Natural language processing
  - nltk
    - tokenization
  - spacy
    - noun phrases
  - fasttext
    - We will use this the most and this is the secret to LLMs

Homework 4:
- Add XGBoost to your reusable classifier
- For those who did not structure the assessment to be between people (instead using a simple train_test_split), refactor your code to be between people. You can reference my code.
- Compare the performance of XGBoost with Random Forest and add the difference (one sentence) to your README.md.
- Install `fasttext` and embed a single word.
- Referencing what we've discussed throughout the course up to this point, create an explanation of machine learning.
  - You can eventually adapt this into a Medium or LinkedIn post to help prepare for a job search
  - Nothing shows understanding better than teaching
  - This should be about one page and must include both a diagram and a description. The weight of one vs the other is up to you. The diagram _MUST_ be your own-- it cannot be taken from the internet. Similarly, I would prefer a wrong answer over one created by a large language model. Think of this as preparation for the Performance Review (Midterm) and Job Interview (Final Exam).
  - Must be in the form of a Markdown (.md) file with an imported image (note that this is a markdown file. As is your README.md file)
    - Add the diagram to your repository
    - Insert the diagram using: `![description](relative/path/to/image.png)`
  - I would recommend covering the key concepts:
    - Features
    - Labels
    - Classification vs regression
    - Parameters
    - Black box vs open box
    - Different models that we've discussed and how to choose from amongst them
    - Data vs features
    - Training data requirements
    - Anything else that's interesting

## Week 5 - Feb 16

NOTE: Installing fasttext on python 3.12 or higher requires a workaround:

```
poetry add git+https://github.com/cfculhane/fastText
```

- How is everyone feeling?
- Go over classifiers one last time
- Talk about bias in data
  - Finance field, zip code
  - Amazon hiring
  - Judicial predictions
  - LLMs are pleasing
- fasttext vs word2vec
- Create a function together to produce entity resolution features
  - People will take turns adding lines on my computer
- How to create training data
  - Simulation
  - Hand-labeling
  - Recursive
- Recursive model training
  - Bias
  - Bootstrapping + class mislabels

Homework 5:
- Create entity resolution training data via simulation
  - The number of rows is up to you
  - As are error styles
  - Should include forename, surname
  - Can include initials, affiliations
- Add 2-3 sentences to your README.md answering the following _WITH NO LLM/GOOGLE HELP_:
  - What is the simplest way you can think of to limit the phonebook-to-phonebook matching problem such that you do not have to do an all-to-all comparison?
    - You can do this. You don't need any information other than thinking of a phone book.
    - You have first name, last name, address, and phone number in each.
    - You must compare two phone books with the above information.
    - You cannot propose a solution that compares every entry in phone book 1 to every entry in phone book 2.


## Week 6 - Feb 23


- How to create training data
  - Simulation
  - Hand-labeling
  - Recursive
- Recursive model training
  - Bias
  - Bootstrapping + class mislabels

- Talk through training data approaches
- Create our dataset cross-product file
- Create our data to features mapping file

The "blocking" problem

- Blocking problem and nearest neighbor indices
- Combine together to create a tool to classify the two datasets

Homework 6 due _this friday_, Feb 27:
- Set up Performance Review. 
- Create a new repository. You should come up with your own names for any files and copy in the entity resolution project as it exists right now. Add a README. This should be structured EXACTLY as laid out in the README, except with unique names. This is a repository to show off your coding skill.

# Spring Break

## Week 7 - Mar 9

- Download Beekeeper Studio: https://www.beekeeperstudio.io/

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
- Map/reduce
- SQL introduction
  - SQLite v MySQL v Postgres
  - CREATE
  - row types
- Data tables
- Bridge tables
  - Relationships between tables

Homework 7:
- Create a SQLite database for our datasets
- Create tables for Articles and Grants
- Create bridge table
- Add a function to insert data from Articles and Grants into the database via SQLAlchemy and Pandas

## Week 8 - Mar 16

- We will go through people's tables. You will be asked to come up and write the table creation statement on the board.

- Graphs
  - One to one
  - One to many
  - Many to many

- Continue with SQL
  - SELECT `SELECT col FROM table`
  - * (stands for all columns, like Python)
  - COUNT `COUNT * FROM table`
  - DISTINCT `SELECT DISTINCT col FROM table`
  - INSERT `INSERT INTO table VALUES (val1, val2, val3)`
  - WHERE `WHERE col=val` (`=` is one comparitor. Others, such as `<`, `>`, `<>` exist)
  - DELETE FROM `DELETE ROM table WHERE col=val` 
  - UPDATE `UPDATE table SET col=val WHERE date < '2025'`
  - JOIN `SELECT * FROM table1 JOIN table2 ON table1.col = table2.col`
  - AS (aliasing)
  - GROUP BY (`GROUP BY col` at the end, before ORDER BY)
  - ORDER BY (`ORDER BY col` at the end, before LIMIT)
  - LIMIT (`LIMIT 2` at the end)
  - subqueries `SELECT col FROM table WHERE col2 IN (SELECT col3 FROM table2)` or `WITH temptab AS (SELECT * FROM table) SELECT * FROM temptab`
  - HAVING - know that having exists, but it is much less widely used. The idea of having is to filter a groupby. `GROUP BY col HAVING count(*) > 1`

- Using NO LLMs, in class, solve the following problems:
  1. Select 100 rows from a table, including all columns.
  2. Select only the forenmae or title column from a table.
  3. Return the unique set of last names from a table.
  4. Find all columns in which the forename is 'John'.
  5. List employees alphabetically by last name.
  6. Insert a new person or article into a table.
  7. Then, change that person's forename.
  8. Finally, delete that person.
  9. Join together tables on forename, surname or on organization.
    - Only find identical matches
    - Find all possible matches for a single surname
    - If you don't have names in your db, you can either put them in or extract the first word of each title and treat it as a "name" `SELECT substr(sentence, 1, instr(sentence, ' ') - 1) AS first_word FROM your_table;`
  10. How many unique surnames do you have? If not surnames, affiliations?
  11. Find everyone who works at the same organization as a person named John (requires subqueries).
  12. Find all people who work at an organization that appears more than once in the table (subqueries and cleverness)
  13. If you complete this, what are the pandas equivalents for each?

- Download https://mbta-massdot.opendata.arcgis.com/datasets/mbta-rapid-transit-stop-distances/explore
- NetworkX, graphs, pagerank, and connected components

Homework 8: NO LLMs ARE ACCEPTABLE. 
- You may not ask any questions of an LLM. You may ask as many questions as you want from me. You may ask some questions of your peers, but if any of them are "what's the answer for..." that's not allowed.
- This is another homework to build intuition. We have been talking about entity resolution. As of this week, we have covered everything that makes up an entity resolution pipeline.
- What is entity resolution?
- Relate every single week's work up to now to entity resolution. The first few weeks will be the hardest, because they are more abstractly related.
- You should be able to relate the human activity recognition dataset to entity resolution. Not directly, but rather you should understand that we were learning a core conept about machine learning. What was it?
- The output should be in the form of a markdown (.md) file. Graphics are optional.
- The output should be either paragraphs or a bulleted list. 
- If I believe that you've used an LLM to write this, 1. you are wasting an opportunity and 2. I will ask you to explain entity resolution directly to me in greater depth. If you cannot answer to my satisfaction, the homework will be marked uncompleted and will directly affect your grade.

## Week 9 - Mar 23

- Review Homework 8-- each person describes a week
- Use everything we learned to finish entity resolution
  - Reminder of to_db
  - Reminder of bridge tables
  - Reminder of readers, reusable classifier
  - Reminder of distance class
  - Focus on creating a dataset and training the model
    - Reiterate using edge cases to improve model performance
    - Cover the "blocking" process again
      - Embedding + nearest neighbors
      - By last name

Homework 9:
- Fix up your entity resolution repository
  - If it is already perfect, great
  - This repository CANNOT mention "homework", "class", or any similar wording
  - The most recent commit of the repository also cannot mention these terms (really, no commit should but I don't want to make you redo it)
  - The repository must have the complete pipeline that we have worked through
  - Your description of entity resolution should live here. 
  - REMEMBER: This is your opportunity to improve your chances of getting a job. Don't do this halfway
- Create a neural network via https://teachablemachine.withgoogle.com/
  - In your class repository, add one paragraph discussing the training data, the quality of the output, and why you think that a classifier like this can perform well with only a small number of training examples

## Week 10 - Mar 30

- Autoencoder in tensorflow
  - Train it on the wine quality dataset
- Create our own neural network library

## Week 11 - Apr 13

- Discuss the neural network library
- Apply the NN library to the wine quality dataset
- Consider Neural Network variants
  - CNNs
    - Resnet
  - Transformers

## Week 12 - Apr 20

- Coding with LLMs

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
