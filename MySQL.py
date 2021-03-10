import mysql.connector
import pandas as pd


def get_connection():
    """ connecting to DataBase """

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="shirel123",
        database="hospitalmanagementsystem"
    )

    return connection


def close_connection(connection):
    """ closing connection DataBase """

    if connection:
        connection.close()


def read_database_version():
    """  returns just information """

    connection = get_connection()
    dataBase = connection.get_server_info()
    return dataBase


def get_hospital_detail(hospital_id=2):
    """ returns detail of hospital selected """

    connection = get_connection()
    cursor = connection.cursor()
    sql_select_query = "SELECT * FROM Hospital WHERE Hospital_Id = %s"
    cursor.execute(sql_select_query, (hospital_id,))
    res = cursor.fetchall()
    close_connection(connection)
    return res


def get_doctor_detail(doctor_id=105):
    """ returns detail of doctor selected """

    connection = get_connection()
    cursor = connection.cursor()
    sql_select_query = "SELECT * FROM Doctor WHERE Doctor_Id = %s"
    cursor.execute(sql_select_query, (doctor_id,))
    res = cursor.fetchall()
    close_connection(connection)
    return res


def get_specialist_doctors_list(speciality='Garnacologist', salary=30000):
    """ returns detail in Data Frame of doctor Area of
        specialization, salary and above that selected """

    connection = get_connection()
    dataBase = pd.read_sql("SELECT * FROM Doctor WHERE speciality = %s ", connection, params=[speciality])
    close_connection(connection)
    return dataBase[dataBase['Salary'] >= salary]


def get_hospital_name(hospital_id=2):
    """ returns name of hospital selected """

    connection = get_connection()
    cursor = connection.cursor()
    sql_select_query = "SELECT Hospital_Name FROM Hospital WHERE Hospital_id = %s"
    cursor.execute(sql_select_query, (hospital_id,))
    res = cursor.fetchone()
    close_connection(connection)
    return res


def get_doctors(hospital_id=2):
    """ returns Data of doctor who belong to a particular hospital
        according to the ID of the hospital"""

    connection = get_connection()
    cursor = connection.cursor()
    sql_select_query = "SELECT * FROM Doctor WHERE Hospital_id = %s"
    cursor.execute(sql_select_query, (hospital_id,))
    res = cursor.fetchall()
    close_connection(connection)
    return res


def update_doctor_experience(doctor_id=105):
    """ Updates the years of seniority of each Doctor """

    connection = get_connection()
    cursor = connection.cursor()
    sql_select_query = "UPDATE Doctor SET Experience = 15 WHERE Experience IS null AND Doctor_Id = %s"
    cursor.execute(sql_select_query, (doctor_id,))
    connection.commit()
    cursor.execute("SELECT * FROM Doctor")
    res = cursor.fetchall()
    close_connection(connection)
    return res


def create_new_table(Hospital_Name='Mayo Clinic'):
    """ Create a new table
        With all the doctors who work
        in this hospital it is from the DOCTOR table. """

    connection = get_connection()
    cursor = connection.cursor()
    sql_select_query = "CREATE TABLE Doctors_Hospital AS " \
                       "SELECT D.Doctor_Id, D.Doctor_Name, H.Hospital_Name " \
                       "FROM Doctor D JOIN Hospital H ON D.Hospital_Id = H.Hospital_Id WHERE Hospital_Name ='" + Hospital_Name + "'"
    connection.commit()
    cursor.execute(sql_select_query)
    cursor.execute("SELECT * FROM Doctors_Hospital")
    res = cursor.fetchall()
    close_connection(connection)
    return res


switcher = {
    1: get_connection,
    2: close_connection,
    3: read_database_version,
    4: get_hospital_detail,
    5: get_doctor_detail,
    6: get_specialist_doctors_list,
    7: get_hospital_name,
    8: get_doctors,
    9: update_doctor_experience,
    10: create_new_table
}


def switch_demo(argument=int(input("Enter number: "))):
    func = switcher.get(argument)
    return func()


print(switch_demo())
