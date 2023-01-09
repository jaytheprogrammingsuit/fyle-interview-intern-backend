# Fyle Backend Challenge

### Install requirements

```
virtualenv env --python=python3.8
source env/bin/activate
(I used the window so this command not work, I used :- '.\env\Scripts\activate.ps1' for activating the environment)
pip install -r requirements.txt
```
### Reset DB

```
export FLASK_APP=core/server.py (In window we used ‘set’ instead of ‘export’)
rm core/store.sqlite3 (In window we used rmdir)
$env:FLASK_APP="core/server.py"  (Set the environment variable for windows user)
flask db upgrade -d core/migrations/  (This is used for database migrations)
```
### Start Server

```
bash run.sh (for windows -> 'flask run')
```
### Run Tests

```
pytest -vvv -s tests/

# for test coverage report
# pytest --cov
# open htmlcov/index.html
```


### Few steps for explanations
```
#Step1 : Fork this repository to my GitHub account ( https://github.com/jaytheprogrammingsuit/ ).
#Step2 : Clone the forked repository and install all the required tools and technologies.
#Step3 : I didn't know anything about flask before that, so 1st, I learned some required things about it, and I did some work on Django sometime before so it could help me.
#Step4 : In the entire project following are the List of files in which I have made some changes or modification :
1)server.py
(-> Register new blueprint for Teacher)

2)models/assignment.py	
(-> Create a new method for fetching teachers' associate assignments details through teacher_id.
-> Create a new method graded() for the Teacher to grade the assignments.)

3) assignment/__init__.py

4) assignment/schema.py	
( -> Add new class for Assignment Grading through Teacher. )

5)assignment/teacher.py
( -> List ##all the assi Completed :gnments associated with the Teacher.
-> Teacher graded the assignment )
```


### Missing APIs Completed :
```
1) GET /teacher/assignments
List all assignments submitted to this teacher
```

![fm1](https://user-images.githubusercontent.com/92263485/211387365-5f375f27-bbb1-4653-a546-52e44cf22b7c.JPG)

```
2) POST /teacher/assignments/grade
Grade an assignment
```

![fm2](https://user-images.githubusercontent.com/92263485/211387566-7f8c8349-79d1-4b85-9753-6eda6cb80903.JPG)



### Test Coverage :
```
I have yet to work on Flask. So I learned Flask first then I created the missing APIs. So I would appreciate it if you considered my task and gave me the opportunity to join you.
```

![f1](https://user-images.githubusercontent.com/92263485/211391101-b7020ec9-720a-4b3f-9ebc-4ebad842745c.JPG)

![ftest](https://user-images.githubusercontent.com/92263485/211391181-ea0c88a3-e4b9-434f-985f-5982ac78a33a.JPG)


### About me :

  I am Jay Bhatt, and currently pursuing M.Sc. I.T. from Dhirubhai Ambani Institute of Information and Communication Technology.

  I have good knowledge of information technology. Well-versed in technology and writing code to create reliable and user-friendly systems. Strategic thinker, innovative creator, and self-motivated to work.

  I would appreciate your consideration of my application for this profile.
