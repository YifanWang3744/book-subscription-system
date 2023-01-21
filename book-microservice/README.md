# book-microservice

## Introduction

This is a microservice for book service which

- created a database and a model for books
- developed APIs for book service

## Technologies

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)

## AWS Deployment

The microservice is deployed on [Amazon EC2](https://aws.amazon.com/ec2/?nc1=h_ls), and data is kept in an [AWS RDS](https://aws.amazon.com/rds/) instance.

## APIs

- ```GET /books```
- ```POST /books```
- ```PATCH /books/{id}```
- ```DELETE /books/{id}```
