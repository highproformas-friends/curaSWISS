#!/bin/bash
docker exec backend python3 manage.py loaddata role_fixture
