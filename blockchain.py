blockchain = [[1]]


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
    print("Complete blockchain, "+str(len(blockchain))+" elements")
    print(blockchain)


def verify_chain():
    block_index = 0
    is_valid = True
    for block in blockchain:
        if block_index == 0:
            block_index += 1
            continue
        elif block[0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
            break
        block_index += 1
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
        tx_amount = get_transaction_value()
        add_transaction(tx_amount)
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


print('Done!')
