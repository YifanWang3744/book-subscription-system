# user-microservice

## Introduction

This is a microservice for user service which

- created a database and a model for users
- developed APIs for user service

## Technologies

- [FastAPI](https://fastapi.tiangolo.com/)
- [sqlalchemy](https://www.sqlalchemy.org/)

## AWS Deployment

The microservice is deployed on [AWS EC2](https://aws.amazon.com/ec2/), and data is kept in an [AWS RDS](https://aws.amazon.com/rds/) instance.

## APIs

- ```GET /users```
- ```POST /users```
- ```GET /users/{id}```
- ```PATCH /users/{id}```
- ```DELETE /users/{id}```
- ```POST /users/json```
- ```POST /users/search-by-email```
