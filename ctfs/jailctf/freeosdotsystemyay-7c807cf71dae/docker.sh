#!/bin/bash
docker build -t freeosdotsystemyay .
docker run -d -p 5000:5000 --privileged --name freeosdotsystemyay freeosdotsystemyay
