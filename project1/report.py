#!/usr/bin/env python

# Reporting script to return the required values from the postgres database.
# Boilerplate code borrowed from this project -
# https://github.com/akio-outori/terraform-renderer

import sys
from lib.switch import switch
from lib.database import database
from lib.output import output

# Show possible command line options


def showOpts():
    print("Option not understood:")
    print("  top_authors")
    print("  top_articles")
    print("  highest_error")
    print("\nusage: report.py <option>")
    sys.exit(1)


def run_query(query):
    db = database.connection('news', 'postgres', 'localhost')
    return database.query(db, query)

# Get Options
try:
    option = sys.argv[1]
except BaseException:
    showOpts()

for case in switch(option):

    if case("top_authors"):
        print(output.text(run_query('SELECT * FROM top_authors;')))
        break

    if case("top_articles"):
        print(output.text(run_query('SELECT title, clicks FROM top_articles LIMIT 3;')))
        break

    if case("highest_error"):
        print(output.text(run_query('SELECT * FROM error_stats WHERE error > 1.0;')))
        break
