import psycopg2  # import the psycopg2 library to your python environment to do Postgres Database operations

connection = psycopg2.connect(  # This is the connection string for your Postgres Database server
    host="localhost",  # The connecting Database host, which means the location of you DB
    database="postgres",  # The database name in your host
    user="postgres",  # The user name of your database
    password="Godawgs", # !!!!!! change to your password, this is the password you use when set up the database
)
connection.set_session(autocommit=True)  # Use the connection string to connect the database

with connection.cursor() as cursor:  # Define a cursor that be used to execute database command
    cursor.execute('SELECT COUNT(*) FROM users')  # Use the cursor to execute command: "count rows of users table"
    result = cursor.fetchone()  # return execution result to the variable "result"
    print(result)  # print out the result


def is_admin(username: str) -> bool:  # Define a function. This is not actual execution, just definition!!!
    with connection.cursor() as cursor:  # Define a cursor that be used to execute database command
        cursor.execute("""   
            SELECT
                admin
            FROM
                users
            WHERE
                username = '%s'
        """ % username)  # Use the cursor to execute command: "check if user with given "username" is admin user"
        result = cursor.fetchone()  # return execution result to the variable "result"
    admin = result  # let the variable "admin" same as "result"
    return admin    # return the "admin" to where this function been called


print(is_admin('alexjohn'))  # !!!!!change to your username # This is where the "is_admin" function executed

# #############followed commented lines are example code lines mentioned in the instruction####################
# print(is_admin("'; update users set admin = 'true' where username = 'yan'; select true; --"))
# print(is_admin("yan"))