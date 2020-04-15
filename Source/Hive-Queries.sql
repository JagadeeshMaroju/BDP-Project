hive

use hivedb;

create table tweets (user_description string,user_location string,coordinates string,text string,user_name string,user_created string,user_followers string,id_str string,created string,retweet_count string,polarity string,subjectivity string) row format delimited fields terminated by ',' stored as textfile;


load data inpath 'projectfiles/tweets_file.csv' into table tweets;



create database project;
use project;


create table tweets (id int,user_description string,user_location string,coordinates string,text string,user_name string,user_created string,user_followers string,id_str string,created string,retweet_count string,polarity bigint,subjectivity bigint)
 row format delimited
 fields terminated by ',' 
stored as textfile
;


select count(*) from tweets

select count(*) from tweets where text like "%Republican%" or text like '%Republics%' or text like '%GOP%' and polarity>0.5;


select count(*) from tweets where text like "%democratic%" or text like "%Democrats%" and polarity>0.5;


select count(*) from tweets where text like "%trump%" and polarity>0.5;


select count(*) from tweets where text like "%democratic%" or text like "%Democrats%" and subjectivity=1;

select text,user_location,polarity,subjectivity,retweet_count as ct from tweets order by ct desc limit 1;

select user_name,user_followers from tweets order by user_followers desc limit 1;


create table tweets (id int,user_description string,user_location string,coordinates string,text string,user_name string,user_created string,user_followers int,id_str string,created string,retweet_count int,polarity bigint,subjectivity bigint)
 row format delimited
 fields terminated by ',' 
stored as textfile
;





