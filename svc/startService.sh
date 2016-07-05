#!/bin/bash
gunicorn -b :8000 ivoiriansAPI:start