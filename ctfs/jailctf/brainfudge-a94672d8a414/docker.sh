#!/bin/bash
docker build -t brainfudge .
docker run -d -p 5000:5000 --privileged --name brainfudge brainfudge
