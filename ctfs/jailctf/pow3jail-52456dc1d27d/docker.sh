#!/bin/bash
docker build -t pow3jail .
docker run -d -p 5000:5000 --privileged --name pow3jail pow3jail
