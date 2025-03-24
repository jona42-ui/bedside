#!/bin/bash
cd /opt/render/project/src
exec gunicorn bedside.wsgi:application
