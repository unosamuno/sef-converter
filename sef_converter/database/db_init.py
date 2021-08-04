import sqlite3 as sl

con = sl.connect('format-db.db')

with con:
    con.execute("""
            CREATE TABLE MACHINE_FORMAT (
                machine_id INTEGER PRIMARY KEY AUTOINCREMENT,
                machine_name STRING,
                i_axis_limit_min_val FLOAT,
                i_axis_limit_max_val FLOAT,
                min_velocity FLOAT,
                max_velocity FLOAT
            );
    """)
with con:
    con.execute("""
            CREATE TABLE TEXTILE_FORMAT (
                textile_id INTEGER PRIMARY KEY AUTOINCREMENT,
                textile_name STRING,
                type STRING,
                width_x FLOAT,
                height_y FLOAT,
                thickness FLOAT
            );
    """)
with con:
    con.execute("""
            CREATE TABLE TOOL_FORMAT (
                tool_id INTEGER PRIMARY KEY AUTOINCREMENT,
                tool_name STRING,
                target_offset_translation FLOAT,
                target_offset_rotation FLOAT,
                material STRING
            );
    """)

