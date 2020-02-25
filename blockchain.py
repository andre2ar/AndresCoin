blockchain = []
open_transactions = []
owner = 'Andre'


def get_last_blockchain_value():
    if len(blockchain) > 0:
        return blockchain[-1]
    return None


def add_transaction(recipient, amount):
    transaction = {
        'sender': owner,
        'recipient': recipient,
        'amount': amount
    }

    open_transactions.append(transaction)


def mine_block():
    pass


def get_transaction_value():
    recipient = input('Enter the recipient of the transaction: ')
    amount = float(input('Your transaction amount please: '))

    return recipient, amount


def get_user_choice():
    user_input = input('Your choice: ')
    return user_input


def print_blockchain_elements():
    for block in blockchain:
        print(block)
    else:
        print('-'*20)

    print("Complete blockchain, "+str(len(blockchain))+" elements")
    print(blockchain)
    print('-'*20)


def verify_chain():
    is_valid = True

    for block_index in range(len(blockchain)):
        if block_index == 0:
            continue
        elif blockchain[block_index][0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
            break
    return is_valid


waiting_for_input = True
while waiting_for_input:
    print("Please choose")
    print('1: Add a new transaction value')
    print('2: Output the blockchain blocks')
    print('h: Manipulate blockchain blocks')
    print('q: Quit')

    user_choice = get_user_choice().lower()

    if user_choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        add_transaction(recipient, amount)
        print(open_transactions)
    elif user_choice == '2':
        print_blockchain_elements()
        input()
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('Invalid input')

    if not verify_chain():
        print('Invalid blockchain!')
        waiting_for_input = False
else:
    print("User left")

