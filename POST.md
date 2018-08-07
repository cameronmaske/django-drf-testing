## Introduction 

In this post I'm going to compare 3 different hosted continuous integration services for a docker compose project. 

* Fast. I want something that will build and run my tests as fast as possible. I want to minimize time spent waiting for my pull request's check for to green (or red).
* Cost. I'll look at costs involved using the CI tool for an open source project, or a private repo. 
* Setup complexity (and documentation). The less time setting everything up for the better. How fast it takes to get up and running. Good quality tools or documentation that aide the process are definately appreciated. 
* How close I can get the CI suite to make my local and production. Docker takes care of most of this. accurately simulate my production environment. // Maybe cut this.

This post doesn't focus on pushing and publishing docker images, or deploying them as services.
If you have experiences let me know about it in the comments below, or a PR is welcome to the repo in question!

## Our sample project

To compare our CI, I have set up a Python-based Django + Django Rest Framework application that uses Docker Compose for local development. It uses pytest as it's test runner, and needs to run both unit tests and integrations test against a Postgres database. 

## [Codeship Pro](https://codeship.com/features/pro)

### Setup

Codeship needs require two key files to setup your Docker containers and then run the required tests.

#### Codeship Services File `codeship-services.yml`

This file is very similar to a `docker-compose.yml`, in fact, in its absence, Codeship will automatically search for a `docker-compose.yml` file to use in its place.

Differents slightly
* [encrypted_env_file](https://documentation.codeship.com/pro/builds-and-configuration/services/#environment-variables)
* [cached](https://documentation.codeship.com/pro/builds-and-configuration/services/#caching-the-docker-image)
 
* [Some features are unavaible](https://documentation.codeship.com/pro/builds-and-configuration/services/#unavailable-features). 

Codeship Steps.
`codeship-steps.yml` which defines your continuous integration and delivery steps.
Here you control what commands are run.
Or run tests Parallel 
Options to limit to specific branches, 

In this case, I kept it simple.

[Example code]

### Pricing 

Free for Open Source
Free plan
* 100 builds a month
* 1 concurrent build
* 1 parallel test pipeline
* Unlimited projects/users/teams

Pricing starts at $75/month.

Runs on EC2 instances on US-East-1
https://documentation.codeship.com/general/about/vm-and-infrastructure/
2 VCPU 
3.75 gb memory

Docker version at 17.03.1: No control
https://community.codeship.com/t/updated-docker-version-for-codeship-pro/6201


## CircleCI

* 1500 build minutes per month 
* 1 concurrent job 
* Unlimited repos/users

In their [FAQ](https://circleci.com/pricing/#faq-section-linux)

Free for Open Source
For linux, up to 4 containers.
For OSX, up to 1 concurrency

Pricing is $50 a month for each container.

https://circleci.com/docs/2.0/executor-types/#using-machine
2 Cpus @ 2.3 Ghz
8gb ram

Note: Use of machine may require additional fees in a future pricing update.

Docker Layer Caching:
https://circleci.com/docs/2.0/docker-layer-caching/

https://circleci.com/docs/2.0/configuration-reference/#machine

ircleci/classic:201703-01 – docker 17.03.0-ce, docker-compose 1.9.0
circleci/classic:201707-01 – docker 17.06.0-ce, docker-comopse 1.14.0
circleci/classic:201708-01 – docker 17.06.1-ce, docker-compose 1.14.0
circleci/classic:201709-01 – docker 17.07.0-ce, docker-compose 1.14.0
circleci/classic:201710-01 – docker 17.09.0-ce, docker-compose 1.14.0
circleci/classic:201710-02 – docker 17.10.0-ce, docker-compose 1.16.1
circleci/classic:201711-01 – docker 17.11.0-ce, docker-compose 1.17.1


## TravisCI 

https://travis-ci.com/plans

Free tier
First 100 builds are free

Pricing starts at $69 and removes the build minutes limit of the free tier.

1 concurrent job
* Unlimited repos/collaborators 

https://docs.travis-ci.com/user/reference/overview/


## Conclusion
