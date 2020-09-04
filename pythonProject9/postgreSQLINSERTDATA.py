import psycopg2
import random
import string
import timeit

def random_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
    return result_str

def random_number(lenght):
    if  lenght == 4:
        randomNumbers = random.randint(1000, 9999)
        return randomNumbers
    if  lenght == 5:
        randomNumbers = random.randint(10000, 99999)
        return randomNumbers
    if  lenght == 6:
        randomNumbers = random.randint(100000, 999999)
        return randomNumbers
    if  lenght == 7:
        randomNumbers = random.randint(1000000, 9999999)
        return randomNumbers

start = timeit.default_timer()
#Establishing the connection
conn = psycopg2.connect(
   database="dataofmillions", user='postgres', password='selimpinarbasi', host='127.0.0.1', port= '5432'
)
#Setting auto commit false
conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

i = 1
while i <= 10000000:
    postgres_insert = """INSERT INTO RANDOMNUMBERS(FOUR_DIGITS, FIVE_DIGITS, SIX_DIGITS, SEVEN_DIGITS) VALUES (%s, %s, %s, %s)"""
    record_insert = (random_number(4), random_number(5), random_number(6), random_number(7))
    postgres_insert2 = '''INSERT INTO RANDOMSTRINGS(FOUR_DIGITS, FIVE_DIGITS, SIX_DIGITS, SEVEN_DIGITS) VALUES (%s, %s, %s, %s)'''
    record_insert2 = (random_string(4), random_string(5), random_string(6), random_string(7))
    # Preparing SQL queries to INSERT a record into the database.
    cursor.execute(postgres_insert, record_insert)
    cursor.execute(postgres_insert2, record_insert2)
    i += 1


# Commit your changes in the database
conn.commit()
print("Records inserted........")

# Closing the connection
conn.close()
stop = timeit.default_timer()
print("time is : ", stop - start)