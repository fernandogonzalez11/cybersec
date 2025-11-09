#!/bin/bash
docker build -t stupidcplusplus .
docker run -d -p 5000:5000 --privileged --name stupidcplusplus stupidcplusplus
