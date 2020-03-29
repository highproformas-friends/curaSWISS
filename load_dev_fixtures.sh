#!/bin/bash
docker exec backend python3 manage.py loaddata role_fixture
docker exec backend python3 manage.py loaddata skill_fixture
docker exec backend python3 manage.py loaddata location_fixture
