from flask import Blueprint, jsonify
from models.reservation_model import delete_reservation_by_id

reservation_bp = Blueprint('reservation', __name__)

@reservation_bp.route('/delete_reservation/<int:reservation_id>', methods=['DELETE'])
def delete_reservation_route(reservation_id):
    response = delete_reservation_by_id(reservation_id)

    if "error" in response:
        return jsonify(response), 404

    return jsonify(response), 200
