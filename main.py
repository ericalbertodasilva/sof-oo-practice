from utils import clear, header
from console import AuthBankAccountConsole, CashMachineConsole

def main():
    clear();
    header();

    if AuthBankAccountConsole.is_auth():
        clear()
        header()
        CashMachineConsole.call_operation()
    else:
        print('Conta invalida')

if __name__ == '__main__':
    while True:
        main()

        input('Pressione <ENTER> para continuar..')