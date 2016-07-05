#!/bin/bash
gunicorn -b :8001 ivoiriansAPI:start

