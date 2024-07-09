
from flask import (
    Blueprint, render_template
)

from app.db import get_db

bp = Blueprint('cars', __name__, url_prefix='/cars')

@bp.route('/', methods=('GET', 'POST'))
def index():
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * from cars;")
    data = cur.fetchall()
    return render_template('cars/index.html', cars=data)