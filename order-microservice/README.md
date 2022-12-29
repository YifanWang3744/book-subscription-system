# order-microservice

## Introduction

This is a microservice for order service which

- created a database and a model for orders
- developed APIs for order service

## Technologies

- [FastAPI](https://fastapi.tiangolo.com/)
- [sqlalchemy](https://www.sqlalchemy.org/)

## AWS Deployment

The microservice is deployed on [AWS Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/), and data is kept in an [AWS RDS](https://aws.amazon.com/rds/) instance.

## APIs

- ```GET /orders```
- ```POST /orders```
- ```PATCH /orders/{id}```
- ```DELETE /orders/{id}```
