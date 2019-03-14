#!/usr/bin/env python

# Reporting script to return the required values from the postgres database.
# Boilerplate code borrowed from this project - https://github.com/akio-outori/terraform-renderer

import sys
from lib.switch import switch
from lib.database import database

# Show possible command line options
def showOpts():
  print("Option not understood:")
  print("  top_authors")
  print("  top_articles")
  print("\nusage: tf-generator <option> <file>.yml")
  sys.exit(1)

def run_query(query):
    db = database.connection('news', 'postgres', 'localhost')
    return database.query(db, query)

# Get Options
try:
    option = sys.argv[1]
except:
    showOpts()

for case in switch(option):

    if case("top_authors"):
        print(run_query('select * from top_authors limit 3;'))
        break

    if case("top_articles"):
        print(run_query('select * from top_articles;'))
        break
