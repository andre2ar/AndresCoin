genesis_block = {
    'previous_hash': '',
    'index': 0,
    'transactions': []
}
blockchain = [genesis_block]

open_transactions = []
owner = 'Andre'


def hash_block(block):
    return '-'.join([str(block[key]) for key in block])


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
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)

    block = {
        'previous_hash': hashed_block,
        'index': len(blockchain),
        'transactions': open_transactions
    }

    blockchain.append(block)


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
    for index, block in enumerate(blockchain):
        if index == 0:
            continue

        if block['previous_hash'] != hash_block(blockchain[index - 1]):
            return False
    return True


waiting_for_input = True
while waiting_for_input:
    print("Please choose")
    print('1: Add a new transaction value')
    print('2: Mine a new block')
    print('3: Output the blockchain blocks')
    print('h: Manipulate blockchain blocks')
    print('q: Quit')

    user_choice = get_user_choice().lower()

    if user_choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        add_transaction(recipient, amount)
    elif user_choice == '2':
        mine_block()
    elif user_choice == '3':
        print_blockchain_elements()
        input('Press any key to continue')
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = {
                'previous_hash': '0xlkji2323LLlkjMDOIU2N,M.N,.',
                'index': 1,
                'transactions': []
            }
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('Invalid input')

    if not verify_chain():
        print('Invalid blockchain!')
        waiting_for_input = False
else:
    print("User left")

