#!/bin/bash
kill `cat WSServicePid`
gunicorn -k "geventwebsocket.gunicorn.workers.GeventWebSocketWorker" -b :8002 -p WSServicePid websockets:websocket_app

