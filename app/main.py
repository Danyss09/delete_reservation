from fastapi import FastAPI, HTTPException
from app.database import get_db_connection

app = FastAPI()

@app.delete("/delete/{reservation_id}")
async def delete_reservation(reservation_id: int):
    connection = await get_db_connection()
    try:
        # Verificar si la reserva existe
        exists_query = "SELECT COUNT(*) FROM Reservations WHERE ReservationID = $1;"
        exists = await connection.fetchval(exists_query, reservation_id)
        if exists == 0:
            raise HTTPException(status_code=404, detail="Reservation not found")

        # Eliminar la reserva
        delete_query = "DELETE FROM Reservations WHERE ReservationID = $1;"
        await connection.execute(delete_query, reservation_id)
        await connection.close()
        return {"message": "Reservation deleted successfully", "reservation_id": reservation_id}
    except Exception as e:
        await connection.close()
        raise HTTPException(status_code=500, detail=f"Error: {e}")
