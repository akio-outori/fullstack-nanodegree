all: build run

PGHOST="localhost"
PGUSER="postgres"
PGDB="news"

build:
	cd docker && docker build --no-cache -t postgres-9.5 .

run:
	docker run --rm --name postgres-9.5 -e POSTGRES_PASSWORD=postgres -d -p 5432:5432 postgres-9.5
	echo "Giving postgres a chance to start up.." && sleep 10
	psql -h $(PGHOST) -U $(PGUSER) -f database/bootstrap.sql
	psql -h $(PGHOST) -U $(PGUSER) -d $(PGDB) -f database/newsdata.sql

clean:
	docker kill $$(docker ps | grep postgres | awk '{ print $$1 }')
