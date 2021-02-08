# Class that executes the main script
from account.account import Account
from user.user  import User
from web3 import Web3
import sys
from time import sleep

class Main:

    @staticmethod
    def main():

        # Define ganache endpoint
        ganacheUrl = "http://127.0.0.1:7545"
        # Mainet infura endpoinnt
        mainnet_infura_url = "https://mainnet.infura.io/v3/548d364006b94801b8cb992b70abbf13"
        # Kovan infura endpoinnt
        kovan_infura_url = "https://kovan.infura.io/v3/548d364006b94801b8cb992b70abbf13"

        # One web3Instance per user
        web3Instance = Web3(Web3.HTTPProvider(kovan_infura_url))
        mainnetInstance = Web3(Web3.HTTPProvider(mainnet_infura_url))
        
        # Create a User account
        print("")
        userName = input("Enter a username: ")
        password = input("Enter a password: ")

        user = User(userName, password, web3Instance, mainnetInstance)

        print(f"\nWelcome {userName}!\n")

        # Get User Public Key
        try:
            numberOfAccounts = int(input("How many accounts would you like to track?\n"))
        except ValueError:
            print("Please enter a number")

        if numberOfAccounts <= 0:
            raise Exception("Number has to be greater than zero")

        print("")
        # Instatiate an Account object
        accounts = []
        for i in range(numberOfAccounts):
            address = input("Please enter public key address:\n")
            accountName = input("Please enter a name for this account:\n")
            user.addNewAccount(address, accountName)

        print("")

        list(map(
                lambda x: print(f"{x.name}'s balance is: {x.getBalance()} ether"),
                user.accounts
                        ))

        sleep(4)

        print("")

        # Get User favourites
        print("Please enter your favourite pairs and type 'done' when finished:")
        favourites = []
        i = 1
        while True:
            data = input(f"Favourite {i}: ")
            i += 1
            if 'done' == data:
                break
            favourites.append(data)

        # Instantaite User Objects
        user.favourites = favourites
        prices = user.getPrices()
        print("")
        list(map(
            lambda x: print(f"{x[0]}: {x[1]}"),
            prices.items()
                ))

        print("")

        depositingAccount = input("Which account would you like to deposit from: \n")
        token = input("Which token would you like to deposit: \n")
        amount = int(input("How much would you like to deposit: \n"))

        print("")

        txHash = user.deposit(depositingAccount, token, amount)

        txHash = Web3.toHex(txHash)

        print("Successful Deposit!")
        print(f"Transaction Hash: {txHash}")



if __name__ == "__main__":
    Main.main()


        
# 0x51B7d41aD7Ef02805a0aAa6d62c571799c3D27b2
# 0x19F38E15D24a43CC8546feA64E04128551185A7B