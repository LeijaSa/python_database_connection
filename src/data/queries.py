import psycopg2
from config import config


con = None


def get_person_table():
    try:
        # **is there to get the return value of config()
        con = psycopg2.connect(**config())
        cursor = con.cursor()
        SQL = 'SELECT *FROM person;'
        cursor.execute(SQL)
        row = cursor.fetchall()
        print(row)
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()

def get_column_names():

    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor()
        SQL ="SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'person';"
        cursor.execute(SQL)
        row = cursor.fetchall()
        for r in row:
            print(r)
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()

def get_certificate_table_column_names():

    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor()
        SQL ="SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'certificates';"
        cursor.execute(SQL)
        row = cursor.fetchall()
        print(row)
        SQL2 = 'SELECT *FROM certificates ORDER BY id;'
        cursor.execute(SQL2 )
        rows = cursor.fetchall()
        print(rows)
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()

def get_average_age():
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor()
        SQL = "SELECT AVG(age) FROM person;"
        cursor.execute(SQL)
        row = cursor.fetchone()
        print(f'Average age: {row[0]:.2f}')
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()

def get_person_certificates():
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor()
        SQL = "SELECT person.name, certificates.name FROM person JOIN certificates ON person.id = certificates.person_id;"
        cursor.execute(SQL)
        row = cursor.fetchall()
        for r in row:
            print(f"Person: {r[0]}, certificate: {r[1]}")
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()

def insert_row_to_person_certificates(person_id:int, certificate_name:str):
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor()
        SQL = "INSERT INTO certificates (person_id, name) VALUES (%s, %s);"
        # If only one value, it need comma
        values = (person_id, certificate_name)
        cursor.execute(SQL, values)
        con.commit()
        print("Row inserted successfully into certificates table")
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()

        
def insert_row_to_person_table(name:str, age:int, student:bool):
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor()
        SQL = "INSERT INTO person (name, age, student) VALUES (%s, %s, %s);"
        values = (name, age, student)
        cursor.execute(SQL, values)
        con.commit()
        print("Row inserted successfully into person table")
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()


def update_row_to_person_table(id:int, name:str=None, age:int=None, student:bool=None):
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor()
        # Start building the SQL statement
        SQL = "UPDATE person SET"

        # Use a list to hold the SET clauses
        set_clauses = []
        params = []

        if name is not None:
            set_clauses.append(" name=%s")
            params.append(name)
        if age is not None:
            set_clauses.append(" age=%s")
            params.append(age)
        if student is not None:
            set_clauses.append(" student=%s")
            params.append(student)

         # Join the SET clauses with commas
        SQL += ", ".join(set_clauses)

        SQL += " WHERE id=%s;"
        params.append(id)

        cursor.execute(SQL, params)  # Pass parameters safely
        con.commit()
        print("Row updated successfully in person table")
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()

def update_row_to_certificate_table(name:str, person_id:int):
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor()
        SQL = "UPDATE certificates SET name=%s WHERE person_id = %s;"
        values = (name, person_id)
        cursor.execute(SQL, values)
        con.commit()
        print("Row updated successfully in certificate table")
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()

def alter_certificates_table():
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor()
        SQL = "ALTER TABLE certificates DROP CONSTRAINT fk_person, ADD CONSTRAINT fk_person FOREIGN KEY (person_id) REFERENCES person(id) ON DELETE CASCADE;"
        cursor.execute(SQL)
        con.commit()
        print("Column 'person_id' altered successfully")
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()

def delete_row_from_person_table(id:int):
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor()
        SQL = "DELETE FROM person WHERE id=%s;"
        values = (id,)
        cursor.execute(SQL, values)
        con.commit()
        print("Row deleted successfully from person table")
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()

def main():
    # Choose what methods to execute
    #get_person_table()
    #get_column_names()
    #get_certificate_table_column_names()
    #get_average_age()
    #get_person_certificates()
    #insert_row_to_person_certificates(1,'Microsoft')
    #insert_row_to_person_table('John Doe', 75, True)
    #update_row_to_person_table(id=5,name= 'Johnny Doe',student=False)
    #update_row_to_certificate_table(name='JavaScript', person_id=1)
    #alter_certificates_table()
    #delete_row_from_person_table(id=4)
    pass


if __name__ == '__main__':
    main()