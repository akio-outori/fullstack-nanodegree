FROM postgres:9.5-alpine
USER postgres

COPY entrypoint.sh /
EXPOSE 5432

ENTRYPOINT ["/entrypoint.sh"]
