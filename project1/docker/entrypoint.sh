#!/bin/bash

PGDATA=/var/lib/postgresql/data
/usr/local/bin/initdb

cat << PGHBA > $PGDATA/pg_hba.conf
host    all             all             0.0.0.0/0            trust
PGHBA

/usr/local/bin/postgres
