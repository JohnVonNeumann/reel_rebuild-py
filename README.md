# Reel 
## Marketplace for fishermen, find guides for local spots.

[![Build Status](https://travis-ci.org/JohnVonNeumann/reel_rebuild-py.svg?branch=master)](https://travis-ci.org/JohnVonNeumann/reel_rebuild-py)
[![Coverage Status](https://coveralls.io/repos/github/JohnVonNeumann/reel_rebuild-py/badge.svg?branch=master)](https://coveralls.io/github/JohnVonNeumann/reel_rebuild-py?branch=master)

This project was originally built in Rails whilst at Coder Academy Melbourne going through my bootcamp. I was never proud of the code I wrote, so I'm taking the time to rebuild it in Python, a language I am now working with in a professional manner. I hope to fix up not only the app and the idea, but also the holes in my knowledge.

### To Use:

Create a Python3.6 virutalenv:
> virtualenv -p python3.6 venv-36-reel

Activate venv:
> source venv-36-reel/bin/activate

Git clone the repo:
> git clone https://github.com/JohnVonNeumann/reel_rebuild-py.git

Install requirements:
> pip install -r requirements.txt

Run tests:
> nosetests

View code coverage:
> coverage run --source=reel setup.py test
> coverage report -m

### Decision Points

*SQLAlchemy ORM v Core 
> Decided to get into Core as it is more appropriate for what I'm doing at work and I'd actually rather be closer to the SQL than further away from it, ORMapping sounds great but after doing some research it does appear great and all but there is a large camp of people who believe that fundamentally that is a mismatch between the aims of DB's and OOP, so I've decided to learn core instead. 

> In light of the above point, I have decided to run with Flask-SQLAlchemy for this application, I don't know nearly enough about SQL programming to not do an absolute hatchet job of using something more advanced, the end goal is to use something closer to the SQL, but ultimately, it's better to develop something worthwhile than a half baked botch job.

*Psycopg2
> I'm not going to use it as it appears that it is largely optional and much of the SQLAlchemy Core documentation is written without it's use involved. From what I can gather it offers pooling functionality, (I don't understand the technicals but I think I get it on a very high level) which Core already offers, so this project I'll run without it and see how that impacts my opinion for follow up projects.
