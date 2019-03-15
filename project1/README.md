## Project 1 - SQL Reporting ##

### Overview

This project is a representation of basic SQL reporting using postgres, docker, and python.
The database is a barebones postgres container that you can build locally.  Docker, psql, 
and python are required locally for the build to work and OS X or Linux will likely provide
a better experience.

### Setup

The included Makefile will assist in setting up the environment for testing.  The following
options are supported:

  * make build - build postgres container locally
  * make run - start local postgres container and import db files including custom views
  * make clean - tear down the postgres environment

### Usage

Once the container is running, report.py can be used to answer the following questions:

  * What are the most popular three articles of all time?
  * Who are the most popular article authors of all time?
  * On which days did more than 1% of requests lead to errors?

Run report.py without options to see usage.

### Design

All of the heavy lifting here is done via sql views.  To see the queries used to create these views
check out database/views.sql.

Note that you will have to pull down the repository to inspect the sql files since they use git lfs.
