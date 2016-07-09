#!/bin/bash
kill `cat devServicePid`
gunicorn -b :8001 -p devServicePid ivoiriansAPI:start

