# import pymysql.cursors
# connection = pymysql.connect(host='localhost',
#                              port=3306,
#                              user='root',
#                              password='123',
#                              database='Blog',
#                              charset='utf8mb4',
#                              cursorclass=pymysql.cursors.DictCursor)

# def Create_Table():
#     with connection.cursor() as cursor:
#         sql = """
#         CREATE TABLE IF NOT EXISTS blogs(
#         id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
#         title VARCHAR(255) NOT NULL,
#         description TEXT;
#        """
#         cursor.execute(sql)
#     connection.commit()
