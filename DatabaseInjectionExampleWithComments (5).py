import psycopg2
import logging
import getpass
from psycopg2 import sql


###????
logging.basicConfig (filename=("C:/Users/ajap1/Desktop/Python Projects & Exersices/DatabaseInjectionExampleWithComments (5).txt"),
                     format ='%(asctime)s %(message)s',
                     filemode='w')

# log handler
logger = logging.getLogger()

# # log threshold
logger.setLevel(logging.INFO)

# # Set up connection object and bool for loop
connected: bool = False
connection = None

# Run the prompt for username and password
while connected is False:

    # User validation loop

    keepGoing = True
    username = input('Username: ')
    while keepGoing:

        if username != "":
            keepGoing = False
        else:
            print("Username cannot be blank. Please enter username")
            username = input('Username: ')

# New Password validation loop

    password: str = ''

    keepGoing = True
    password = getpass.getpass()
    while keepGoing:

     if password != '':
         keepGoing = False
     else:
         print("Input valid password")
         password = getpass.getpass()


    # Exception Handling
    try:
        connection = psycopg2.connect(  # This is the connection string for your Postgres Database server
            host="localhost",  # The connecting Database host, which means the location of you DB
            database="postgres",  # The database name in your host
            user=username,  # The user name of your database
            password=password, # !!!!!! change to your password, this is the password you use when set up the database
        )
        logger.info('Connected to database as \'' + username + '\'')
        print('Connected to database as \'' + username + '\'')
        connected = True
    except psycopg2.OperationalError:
        logger.error('Cannot connect to database as \'' + username + '\'')
        print('Cannot connect to database as \'' + username + '\'')

connection.set_session(autocommit=True)  # Use the connection string to connect the database

with connection.cursor() as cursor:  # Define a cursor that be used to execute database command
    cursor.execute('SELECT COUNT(*) FROM users') # Use the cursor to execute command: "count rows of user table"
    result = cursor.fetchone() # return execution result to the variable "result"
    print(result) # print out the result


def count_rows(table_name: str, limit: int) -> int:
    try:
        with connection.cursor() as cursor:
            stmt = sql.SQL("""
            SELECT
            count(*)
            FROM (
            SELECT 1 FROM {table_name}
            LIMIT {limit}
            ) as limit_query
            """).format(
                table_name = sql.Identifier(table_name),
                limit = sql.Literal(limit)
            )
            cursor.execute(stmt)
            result = cursor.fetchone()
            rowcount, = result
            return rowcount
    except psycopg2.DatabaseError:
        logger.error('Table \'' + table_name + '\' could not be found.')
        print('Table \'' + table_name + '\' could not be found.')


def is_admin(username: str) -> bool:  # Define a function. This is not actual execution, just definition!!!
    with connection.cursor() as cursor:  # Define a cursor that be used to execute database command
        cursor.execute("""
            SELECT
                admin
            FROM
                users
            WHERE
                username = %(username)s
        """, {
            'username':username
        })  # Use the cursor to execute command: "check if user with given "username" is admin user"
        result = cursor.fetchone()  # return execution result to the variable "result"

    if result is None:
        #User does not exist
        return False
    else:
        admin, = result  # let the variable "admin" same as "result"
        return admin    # return the "admin" to where this function been called


# Admin validation loop

adminValidation: str = ''
while adminValidation != 'O':
    adminValidation = input("Enter validated username or press 'O' to quit: ")
    if "" == adminValidation:
        print("Enter validated username")
    elif adminValidation == 'O':
        break
    else:
        logger.info('Validating admin status for user \'' + adminValidation + '\'')
        print('Result: ' + str(is_admin(adminValidation)))



