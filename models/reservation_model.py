from services.db_config import get_connection

def delete_reservation_by_id(reservation_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            # Verificar si la reserva existe
            cursor.execute("SELECT * FROM Reservation WHERE ReservationID = %s", (reservation_id,))
            reservation = cursor.fetchone()

            if not reservation:
                return {"error": "Reservation not found"}

            # Eliminar la reserva
            cursor.execute("DELETE FROM Reservation WHERE ReservationID = %s", (reservation_id,))
            connection.commit()

            return {"message": "Reservation deleted successfully!"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        connection.close()