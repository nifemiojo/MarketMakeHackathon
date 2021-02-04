# Class Account template for each account the user registers
from web3 import Web3

class Account:

    # Set up web3 connection
    def __init__(self, address, provider):
        self.address = address
        self.web3 = Web3(Web3.HTTPProvider(provider))


    def getBalance(self):
        # Using web3.py
        checksumAddress = self.web3.toChecksumAddress(self.address)
        accountBalance = self.web3.eth.get_balance(checksumAddress)
        convertedAccountBalance = Web3.fromWei(accountBalance, 'ether')
        return convertedAccountBalance