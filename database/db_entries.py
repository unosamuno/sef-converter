import sqlite3 as sl
con = sl.connect("format-db.db")

sql_insert = 'INSERT INTO MACHINE_FORMAT(machine_id, machine_name, i_axis_limit_min_val, i_axis_limit_max_val, min_velocity, max_velocity) VALUES(?,?,?,?,?,?)'
machine_format_data = [
    (1234, 'klickibunti', 3.14, 2.78, 6.0, 9.9)
]
"""
To make entries in database
"""
#with con:
#    con.executemany(sql_insert, machine_format_data)

"""
To read entries in database
"""
with con:
    data = con.execute("SELECT * FROM MACHINE_FORMAT")
    for row in data:
        print(row)



