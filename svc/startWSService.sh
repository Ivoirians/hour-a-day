#!/bin/bash
kill `cat WSServicePid`
gunicorn -w 1 -k "geventwebsocket.gunicorn.workers.GeventWebSocketWorker" -b :8003 -p WSServicePid globalCounter:CounterApplication

