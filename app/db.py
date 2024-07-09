# Module Imports
import sys
import mariadb

from flask import current_app, g




def get_db():
    if 'db' not in g:
        # g.db = sqlite3.connect(
        #     current_app.config['DATABASE'],
        #     detect_types=sqlite3.PARSE_DECLTYPES
        # )
        # g.db.row_factory = sqlite3.Row
        # Connect to MariaDB Platform
        try:
            conn = mariadb.connect(
                user="mariadb",
                password="mariadb",
                host="db",
                port=3306,
                database=current_app.config['DATABASE']
            )
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            sys.exit(1)

        # Get Cursor
        g.db = conn

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_app(app):
    app.teardown_appcontext(close_db)