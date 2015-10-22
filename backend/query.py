import pymysql.cursors
from datetime import datetime
import time

time.strftime('%Y-%m-%d %H:%M:%S')

connection = pymysql.connect(host="localhost", user="aquaponics", passwd="somepassword1", db="sensors",
                             unix_socket="/opt/lampp/var/mysql/mysql.sock")

try:
    with connection.cursor() as cursor:
        sensor_id_subquery = "(SELECT id FROM sensors.sensor ORDER BY id DESC LIMIT 1)"
        sensor_sql = "INSERT INTO sensor(measurement_time) VALUES (%s);"
        cursor.execute(sensor_sql, datetime.now())
        ph_sql = "INSERT INTO ph(ph, measurement_id) VALUES (%s," + sensor_id_subquery + ")"
        cursor.execute(ph_sql, 2)

        connection.commit()
finally:
    connection.close()