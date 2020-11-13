from cash_machine import accounts_list

class AuthBankAccount:
    back_account_authenticad = None

    @staticmethod
    def authenticate(account_number, password):
        for bank_account in accounts_list:
            if AuthBankAccount.has_bank_account_valid(bank_account, account_number, password):
                AuthBankAccount.back_account_authenticad = True
                return bank_account
        return False
    
    @staticmethod
    def has_bank_account_valid(bank_account, acccount_number, passaword):
        return bank_account.check_account_number(acccount_number) and \
            bank_account.check_password(passaword)