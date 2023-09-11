### Hexlet tests and linter status:
[![Actions Status](https://github.com/Georgyphyton/python-project-52/workflows/hexlet-check/badge.svg)](https://github.com/Georgyphyton/python-project-52/actions)
[![Actions Status](https://github.com/Georgyphyton/python-project-52/workflows/Django%20CI/badge.svg)](https://github.com/Georgyphyton/python-project-52/actions)
[![Test Coverage](https://api.codeclimate.com/v1/badges/00b7b9fa15df2f76d97d/test_coverage)](https://codeclimate.com/github/Georgyphyton/python-project-52/test_coverage)

# Task Manager

_Register, create, delete and edit tasks, labels and statuses, assign executors to tasks. Filter tasks by tags, statuses, and executors, or filter only your created tasks._

# DEMO

Just click and try to use DEMO on [Render](https://task-manager-ygzh.onrender.com)

P.S.: You will need to register to try all the features in demo.

## Installation

Clone the repository:

`git clone https://github.com/M1RRoN/python-project-52.git`

Go to the project folder:

`cd python-project-52`

Install dependencies with Poetry:

(If you don't have Poetry, follow this guide to install it: [Install Poetry](https://python-poetry.org/docs/#installing-with-the-official-installer))

`make install`

## Settings

Create an ".env" file in the root project directory: 

`cp .env.sample .env`

Write following constants to the .env file:

1. `SECRET_KEY='your_Django_secret_key'` 

You can generate one with `make secretkey` command.

2. `DATABASE_URL='your_database_url_path'` 

To use simple sqlite database use this record: 

`DATABASE_URL='sqlite:///db.sqlite3'`

## Database preparation

`make migration`

`make migrate`

`make createsuperuser`

## Start project

`make runserver`

Use this app in browser on http://localhost:8080

---
Good Luck!
