#!/bin/bash
/Applications/Postgres.app/Contents/Versions/9.5/bin/psql -U postgres -c "DROP DATABASE sanic_example;"
/Applications/Postgres.app/Contents/Versions/9.5/bin/psql -U postgres -c "CREATE DATABASE sanic_example;"
/Applications/Postgres.app/Contents/Versions/9.5/bin/psql -U postgres -c "CREATE USER sanic_user WITH PASSWORD 'sanic';"
/Applications/Postgres.app/Contents/Versions/9.5/bin/psql -U postgres -c "ALTER DATABASE sanic_example OWNER TO sanic_user;"