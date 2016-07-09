#!/bin/bash
kill `cat prodServicePid`
gunicorn -b :8000 -p prodServicePid ivoiriansAPI:start 
