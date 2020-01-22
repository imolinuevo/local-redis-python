# Local Redis (Rejson) Python
Local Redis (Rejson) docker example with python connection.

## Installation
> The following steps guide you through the installation in an **ubuntu** system.

1. Install **docker**  
(https://docs.docker.com/install/linux/docker-ce/ubuntu/)
2. Install **docker compose**  
(https://docs.docker.com/compose/install/)
3. Install **redis** tools using **apt**  
`$ sudo apt install redis-tools`
4. Install **pip**  
`$ sudo apt install python-pip`
5. Install **virtualenv** using **pip**  
`$ pip install virtualenv`
6. Initialize **virtualenv** in python folder  
`$ cd python`  
`$ virtualenv venv`
7. Activate **virtualenv**  
`$ source venv/bin/activate`
8. Install dependencies using **pip**  
`$ pip install -r requirements.txt`

## How to use this project

First of all, start redis container using **docker compose** from the project root  
`$ docker-compose up -d`

Once the **docker** container for **redis** is up, you can access it from your operative system using **redis cli**  
`$ redis-cli`

> This will connect you automaticly since the basic configuration is set wit custom values (**host**=localhost, **port**=6379). You can change redis configuration using the `redis/redis.conf` file

Finally, you can execute the python scripts from the `/python` folder, there is one for loading a `json` into redis and another from consuming that `json` from redis into a python `dict`.