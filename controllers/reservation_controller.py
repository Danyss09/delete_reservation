from flask import Blueprint, jsonify
from models.reservation_model import delete_reservation_by_id

reservation_bp = Blueprint('reservation', __name__)

# Ruta para eliminar una reserva
@reservation_bp.route('/delete_reservation/<int:reservation_id>', methods=['DELETE'])
def delete_reservation_route(reservation_id):
    response = delete_reservation_by_id(reservation_id)
    
    # Si la reserva no se encuentra o hay un error, devolvemos el error
    if "error" in response:
        return jsonify(response), 404
    
    # Si la eliminación es exitosa, devolvemos el mensaje de éxito
    return jsonify(response), 200
