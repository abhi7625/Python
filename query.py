import pymysql.cursors


# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='supernova',
                             db='unitedcargo',
			     unix_socket='/run/mysqld/mysqld.sock',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
		


try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "create table entry_fields(id INT AUTO_INCREMENT PRIMARY KEY,creation DATE, grno INT NOT NULL, pkgs INT, awt INT, cwt INT, invoiceno INT, sender varchar(40), receiver varchar(40), origin varchar(40), destination varchar(40), mode varchar(40), freight varchar(40));" 
        
        cursor.execute(sql)

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()
finally:
    connection.close()
    exit()

