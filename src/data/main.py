

from money_account import MoneyAccount

def main():
    money_account = MoneyAccount()
    money_account.create_table_for_money_database()

    if not money_account.account_exists('John Doe'):
        money_account.create_new_account('John Doe', 1000, 500)
    if not money_account.account_exists('Jane Doe'):
        money_account.create_new_account('Jane Doe', 10, 5)

    money_account.get_money_account_table() 
    money_account.update_money('John Doe', 5, 1000)
    money_account.get_money_account_table()
    # Does not work
    money_account.transfer_money(from_name='Doll',to_name='John Doe',amount=2)
    money_account.get_money_account_table()
    # Works
    money_account.transfer_money(from_name='Jane Doe',to_name='John Doe',amount=5)
    money_account.get_money_account_table()


def validate_user_entries():
    """Prompts the user for account information and validates the input.

    Returns:
        A tuple containing the validated name, checking balance, and saving balance,
        or None if validation fails.
    """
    while True:

        input_parts = input('Enter name, checking account, saving account comma separated:').split(',')
        if len(input_parts) != 3:
            print("Invalid input: Please enter name, checking account, and saving account separated by commas.")
            continue
        else:
            try:
                name_string = ''.join(letter for letter in input_parts[0].strip() if letter.isalpha())
                if not name_string:
                    return None
                elif int(input_parts[1]) < 0:
                        print("Invalid balance: Checking account balance cannot be negative.") 
                elif int(input_parts[2]) < 0:
                        print("Invalid balance: Saving account balance cannot be negative.")
                else:
                    return name_string, int(input_parts[1]), int(input_parts[2])
            except ValueError:
                print("Invalid input: Please enter a valid number for checking and saving account balance.")
                continue

def user_actions():
    money_account = MoneyAccount()
    while True:
        print('0: stop \n1 get info \n2 create new account')
        entry= input('What would you like to do: ')

        if entry == '0':
            break

        elif entry == '1':
            try:
                name=input('Enter name to get info:')
                name_string=str(name)
                money_account.get_money_account_info(name_string)
            except ValueError as e:  # Catch any remaining ValueErrors
                print(f"An error occurred: {e}")

        elif entry == '2':
            try:
                name, checking, saving = validate_user_entries()
                money_account.create_new_account(name, checking, saving)
            except Exception as e:  # Catch any remaining errors from validate_user_entries or create_new_account
                print(f"An error occurred: {e}")
                
        else:
            print('Invalid option')
        

if __name__ == '__main__':
    # For testing, uncomment one of the the following lines
    #main()
    user_actions()