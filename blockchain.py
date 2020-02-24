blockchain = []


def get_last_blockchain_value():
    if len(blockchain) > 0:
        return blockchain[-1]
    return None


def add_transaction(transaction_amount, last_transaction=None):
    if last_transaction is None:
        last_transaction = get_last_blockchain_value()
        if last_transaction is None:
            last_transaction = [1]

    blockchain.append([last_transaction, transaction_amount])


def get_transaction_value():
    user_input = float(input('Your transaction amount please: '))
    return user_input


def get_user_choice():
    user_input = input('Your choice: ')
    return user_input


def print_blockchain_elements():
    for block in blockchain:
        print(block)


while True:
    print("Please choose")
    print('1: Add a new transaction value')
    print('2: Output the blockchain blocks')
    print('q: Quit')

    user_choice = get_user_choice()

    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_transaction(tx_amount)
    elif user_choice == '2':
        print_blockchain_elements()
        input()
    elif user_choice.lower() == 'q':
        break
    else:
        print('Invalid input')


print('Done!')
