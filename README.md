# Blog app ![CI - status](https://github.com/czernalex/blog/actions/workflows/ci.yml/badge.svg?branch=main)

The task was to create simple blog application with editable content through administration page.

## Overview
Project consists of two services running in docker containers:
- `db`: Postgres database
- `blog_api`: blog web application
  
## Prerequisites
- `docker`
- `docker-compose`

## Usage
Open your terminal and run following commands in given order:
```
$ git clone git@github.com:czernalex/blog.git
$ cd blog
$ docker-compose up -d --build
```

When both containers successfully start, open your browser [here](http://localhost:8080) to see result.

#### Run tests locally
```
$ docker-compose up -d --build
$ docker exec blog-blog_api-1 pytest ./api/
```
