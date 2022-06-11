from flask import (Blueprint, request)
from . import models

bp = Blueprint('reptile', __name__, url_prefix="/reptiles")

@bp.route('/', methods=['POST', 'GET'])
def index():
    # Return Reptiles Index
    if request.method == 'GET':
        reptiles_dict = {
            'reptiles': []
        }
        # find all reptiles
        reptiles = models.Reptile.query.all()
        for row in reptiles:
            # JSON friendly dict format
            row_dict = {
                'id': row.id,
                'common_name': row.common_name,
                'scientific_name': row.scientific_name,
                'consevation_status': row.conservation_status,
                'native_habitat': row.native_habitat,
                'fun_fact': row.fun_fact
            }
            reptiles_dict['reptiles'].append(row_dict)
        return reptiles_dict

    # Add New Reptile
    elif request.method == 'POST':
        new_reptile = models.Reptile(
            common_name = request.form['common_name'],
            scientific_name = request.form['scientific_name'],
            conservation_status = request.form['conservation_status'],
            native_habitat = request.form['native_habitat'],
            fun_fact = request.form['fun_fact']
        )
        # JSON friendly dict format
        new_reptile_dict = {
            'common_name': request.form['common_name'],
            'scientific_name': request.form['scientific_name'],
            'conservation_status': request.form['conservation_status'],
            'native_habitat': request.form['native_habitat'],
            'fun_fact': request.form['fun_fact']
        }
        # Add New Reptile to Database
        models.db.session.add(new_reptile)
        models.db.session.commit()

        # Print dictionary object on console and return on postman
        print(new_reptile_dict)
        return(new_reptile_dict)


@bp.route('/<int:id>')
def show(id):
    reptile = models.Reptile.query.filter_by(id=id).first()
    reptile_dict = {
        'common_name': reptile.common_name,
        'scientific_name': reptile.scientific_name,
        'conservation_status': reptile.conservation_status,
        'native_habitat': reptile.native_habitat,
        'fun_fact': reptile.fun_fact
    }
    return reptile_dict