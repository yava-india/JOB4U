# JOB4U
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
![GitHub repo size](https://img.shields.io/github/repo-size/yava-india/JOB4U)
![GitHub issues](https://img.shields.io/github/issues-raw/yava-india/JOB4U)

## About
This repository is source code of www.job4u.info website. The aim is to build a website for college training and placement company called Job4U. It is mostly comprised of registeration pages for on-campus placement drives and webinars, placement results,etc. It has an custom admin panel with authentiaction system to access database. It uses MySQL as database.

### Prerequisites
* Python 3.0+
* Django 2.0+
* MySQL 5.0+

### Installing

Get the project up and running locally in just 3 easy steps.

1. Create a personal Fork of this repository.

2. **Clone** the fork with HTTPS, using your local terminal to a preferred location, and **cd** into the project.

```bash
git clone https://github.com/yava-india/JOB4U.git
remote: Enumerating objects: 113, done.
remote: Counting objects: 100% (113/113), done.
remote: Compressing objects: 100% (80/80), done.
Receiving objects: 100% (2845/2845), 12.52 MiB | 5.21 MiB/s, done.
```
step3 : Run requirements.txt(inside project) file to create supporting environments

    pip install -r requirements.txt
step4 :	Update environment variables by adding the path of MySQL

step5 :	Open mysql in cmd

step6 : Create database in mysql and edit database file with your database username , password 

	create database mydatabase;
		
## Deployment:


	python3 manage.py makemigrations (to find the changes to be made to database)

	python3 manage.py migrate  (appy the changes to database)

	python3 manage.py runserver 
