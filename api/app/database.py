import mysql.connector


def get_database():
    return mysql.connector.connect(
        host="database",
        port=3306,
        user="giovanni",
        password="catrame",
        database="giovanni"
    )


__database = get_database()


def insert_reading(sensor_id: int, temperature: float):
    cursor = __database.cursor()

    cursor.execute(
        '''INSERT INTO `readings` (`reading_id`, `sensor_id`, `temperature`, `created_at`) '''
        '''VALUES(NULL, %s, %s, current_timestamp())''', (sensor_id, temperature)
    )
