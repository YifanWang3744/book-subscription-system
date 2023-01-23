# Cloud Bookstore on AWS

## Project Overview

In this full-stack project, I developed and deployed a full-stack cloud Bookstore comprised of four microservices on AWS, implemented Lambda function, SNS event notification, and OAuth2 authorization.

## Basic Structrue

The project has three parts

- Three microservices built with [FastAPI](https://fastapi.tiangolo.com/), each encapsulating a database
- A composition microservice which implements OAuth2 login and event notification
- A browser application built with [React](https://reactjs.org/)

## Core Functions

### Admin Management

Administrators have full access to users, books, and orders.

![image](https://user-images.githubusercontent.com/93358121/209990779-499de1cf-4086-48dc-aff2-08ac1ef8931f.png)

### Google Identity Services Authorization

Login with Google Account.

### SNS and Lambda Function

Implemented a Lambda function that subscribes to an event and sends me an email when an SNS event triggers the Lambda function.

![8ce239e4164adb030f1620dd100e3ec](https://user-images.githubusercontent.com/93358121/209993309-bec301c5-6add-40f5-9eb1-5fe37ee5c52e.jpg)

## Paths

- ```/```
- ```/login```
- ```/auth```
- ```/books```
- ```/books/{id}```
- ```/orders```
- ```/orders/{id}```
- ```/users```
- ```/users/{id}```
- ```/users/search-by-email```
- ```/users/json```

## AWS Deployment

Browser application is deployed in an S3 bucket and encapsulated with CloudFront, while microservices are encapsulated with API Gateway and deployed on AWS EC2 and Elastic Beanstalk. Data is stored in an AWS RDS instance with three databases.

<img src="https://user-images.githubusercontent.com/93358121/209991405-e6bc4b83-0259-4302-be9a-6591c2cea1cd.png" width=75% height=75%>
