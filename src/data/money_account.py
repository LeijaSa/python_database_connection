import psycopg2
from config import config_money


class MoneyAccount(object):  

    def __init__(self):
        pass

    def create_table_for_money_database(self):
        command = (
        """
        CREATE TABLE IF NOT EXISTS money_account (
            id SERIAL PRIMARY KEY,
            owner VARCHAR(255) NOT NULL,
            checking_account INTEGER NOT NULL,
            saving_account INTEGER NOT NULL
        )
        """)
        try:
            with psycopg2.connect(**config_money()) as conn:
                with conn.cursor() as cur:
                    cur.execute(command)
                conn.commit()
        except (psycopg2.DatabaseError, Exception) as error:
            print(error)

    def account_exists(self, owner):
            command = "SELECT 1 FROM money_account WHERE owner = %s"
            try:
                with psycopg2.connect(**config_money()) as conn:
                    with conn.cursor() as cur:
                        cur.execute(command, (owner,))
                        return cur.fetchone() is not None # Returns True if the account exists.
            except (psycopg2.DatabaseError, Exception) as error:
                print(error)
                return False # Handle errors gracefully

    def create_new_account(self, owner, checking_account, saving_account):
        command = (
            "INSERT INTO money_account (owner, checking_account, saving_account) VALUES (%s, %s, %s)")
        try:
            with psycopg2.connect(**config_money()) as conn:
                with conn.cursor() as cur:
                    values=(owner, checking_account, saving_account)
                    cur.execute(command, values)
                    print(f'Account {owner} created successfully.')
                conn.commit()
        except (psycopg2.DatabaseError, Exception) as error:
            print(error)

    def get_money_account_table(self):
        command = 'SELECT * FROM money_account;'
        try:
            with psycopg2.connect(**config_money()) as conn:
                with conn.cursor() as cur:
                    cur.execute(command)
                    accounts = cur.fetchall()
                    print(accounts)
                conn.commit()
        except (psycopg2.DatabaseError, Exception) as error:
            print(error)

    def get_money_account_info(self,owner:str):
        command=('SELECT owner, checking_account,saving_account FROM money_account WHERE owner = %s')
        try:
            with psycopg2.connect(**config_money()) as conn:
                with conn.cursor() as cur:
                    cur.execute(command, (owner,))
                    account = cur.fetchone()
                    if account:
                        print(account)
                    else:
                        print(f'Account {owner} not found.')
                conn.commit()    
        except (psycopg2.DatabaseError, Exception) as error:
            print(error)

    def update_money(self, name:str, checking_account:int, saving_account:int):
        command = (
            "UPDATE money_account SET checking_account=%s, saving_account=%s WHERE owner=%s")
        try:
            with psycopg2.connect(**config_money()) as conn:
                with conn.cursor() as cur:
                    values=(checking_account, saving_account, name)
                    cur.execute(command, values)
                conn.commit()
        except (psycopg2.DatabaseError, Exception) as error:
            print(error)

    def transfer_money(self, from_name:str, to_name:str, amount:int):
        from_command = (
            "UPDATE money_account SET checking_account=checking_account-%s WHERE owner=%s")
        to_command = (
            "UPDATE money_account SET checking_account=checking_account+%s WHERE owner=%s")
        if self.account_exists(from_name) and self.account_exists(to_name):
            try:
                with psycopg2.connect(**config_money()) as conn:
                    with conn.cursor() as cur:
                        # Start a transaction
                        cur.execute("BEGIN")  # or conn.autocommit = False before the with cur block
                        try:
                            from_values = (amount, from_name)
                            to_values = (amount, to_name)
                            cur.execute(from_command, from_values)
                            cur.execute(to_command, to_values)
                            # Commit the transaction (both updates happen or none)
                            conn.commit() #or cur.execute("COMMIT")
                        except Exception as transfer_error:  # Catch any error during the transfer
                            conn.rollback()  # Revert the changes if there's an error
                            print(f"Transfer failed: {transfer_error}")

            except (psycopg2.DatabaseError, Exception) as error:
                print(f"Database error: {error}")
        else:
            print(f"One or both accounts do not exist: {from_name}, {to_name}")


def main():
    pass

if __name__ == '__main__':
    main()


    