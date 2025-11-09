#!/bin/bash
docker build -t computer-monitor .
docker run -d -p 5000:5000 --privileged --name computer-monitor computer-monitor
