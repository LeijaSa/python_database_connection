# Python database connection exercises

This exercise (money_account) is for managing money accounts. It interacts with a PostgreSQL database to store, retrieve, and update account information, including features like creating accounts, updating balances, and transferring money between accounts.

## Features

- **Create Table**: Initialize the `money_account` table if it does not exist.
- **Check Account Existence**: Verify whether an account exists in the database.
- **Create New Account**: Add a new account with an owner, checking account balance, and saving account balance.
- **Retrieve Accounts**:
  - View all accounts in the `money_account` table.
  - Fetch specific account details by owner.
- **Update Balances**: Modify the checking and saving account balances for a specific account.
- **Transfer Money**: Transfer funds between two existing accounts with proper transaction handling to ensure consistency.
