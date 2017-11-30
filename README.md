# My-UD-Database-Analysis

This project is part of mine full stack web development course on Udacity. I am having three SQL queries to solve my questions.
There were three queries which is as following

1. What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.

2. Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.

3. On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser. 

## Getting Started

For running this project clone having address, https://github.com/AnkurBegining/My-UD-Database-Analysis/ from my repo and go to the terminal type the following command.
      python news.py

### Prerequisites

What things you need to install the software and how to install them
1. python

2. psycopg2
for downloading psycopg2 run this command
       pip install psycopg2
3. Postgres Sql
4. you need to have news.sql which you can download from this link https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip

for downloading psycopg2 run this command
       pip install psycopg2
### examples
I have provided output.txt file which you can refer to your matching output

### Working

To run after installing connect to Postgres through command sudo -i -u postgres and run the command psql to run the queries on terminal run command /dt to see the tables and exit using the command /q or ctrl-d
