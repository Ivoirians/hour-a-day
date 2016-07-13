#!/bin/bash
kill `cat WSServicePid`
gunicorn -b :8002 -p WSServicePid websockets:websocket_app

