# tpo_website
step1 : Install GitHub Desktop
	
	https://desktop.github.com/
step2 : Clone tpo_website repo using GitHub Desktop

step3 : Run requirements.txt(inside project) file to create supporting environments

    pip install -r requirements.txt
step4 :	Update environment variables by adding the path of MySQL

step5 :	Open mysql in cmd

step6 : Create database in mysql and edit database file with your database username , password 

	create database mydatabase;
step6 :run project by(should be inside myproject directory):

	python manage.py makemigrations (to find the changes to db)

	python manage.py migrate  (appy the changes to db)

	python manage.py runserver 
