#!/bin/bash
docker exec --env PYTHONPATH="/curaSWISS-backend:$PYTHONPATH" backend django-admin makemessages
docker exec --env PYTHONPATH="/curaSWISS-backend:$PYTHONPATH" backend django-admin compilemessages
docker exec backend python3 manage.py collectstatic --no-input
docker exec backend python3 manage.py migrate
