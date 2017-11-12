import datetime
import pymysql.cursors # install with `pip install PyMySQL`

db = pymysql.connect(host="67.205.179.187", port=3306, user="muci", password="put password here", db="csci374") # keep this line in a seperate file that is imported
cur = db.cursor()
cur.execute("SELECT value, recorded FROM meter_data WHERE meter_id = 313 AND DAYOFWEEK(FROM_UNIXTIME(recorded)) IN (1, 2, 3) ORDER BY recorded DESC")
for row in cur.fetchall():
	print("%f recorded on" % float(row[0]), end=' ')
	print(datetime.datetime.fromtimestamp(int(row[1])).strftime('%Y-%m-%d'))
db.close()