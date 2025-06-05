from flask import Blueprint
bp = Blueprint('loan', __name__)

@bp.route('/apply')
def apply():
    return "Apply for a loan"