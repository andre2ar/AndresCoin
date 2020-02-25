MINING_REWARD = 10

genesis_block = {
    'previous_hash': '',
    'index': 0,
    'transactions': []
}
blockchain = [genesis_block]

open_transactions = []
owner = 'Andre'

participants = {
    owner
}


def hash_block(block):
    return '-'.join([str(block[key]) for key in block])


def get_balance(participant):
    tx_sender = [[tx for tx in block['transactions'] if tx['sender'] == participant] for block in blockchain]
    amount_sent = 0
    for tx in tx_sender:
        if len(tx) > 0:
            amount_sent += tx[0]

    tx_recipient = [[tx for tx in block['transactions'] if tx['recipient'] == participant] for block in blockchain]
    amount_received = 0
    for tx in tx_recipient:
        if len(tx) > 0:
            amount_received += tx[0]

    return amount_received - amount_sent


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
    participants.add(owner)
    participants.add(recipient)


def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    reward_transaction = {
        'sender': 'MINING',
        'recipient': owner,
        'amount':  MINING_REWARD
    }
    open_transactions.append(reward_transaction)

    block = {
        'previous_hash': hashed_block,
        'index': len(blockchain),
        'transactions': open_transactions
    }

    blockchain.append(block)
    return True


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
    print('4: Output participants')
    print('h: Manipulate blockchain blocks')
    print('q: Quit')

    user_choice = get_user_choice().lower()

    if user_choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        add_transaction(recipient, amount)
    elif user_choice == '2':
        if mine_block():
            open_transactions = []
    elif user_choice == '3':
        print_blockchain_elements()
        input('Press any key to continue')
    elif user_choice == '4':
        print(participants)
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

