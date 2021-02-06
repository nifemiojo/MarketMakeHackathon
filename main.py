# Class that executes the main script
from account.account import Account
from user.user  import User
from web3 import Web3
import sys

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

        
        myKovanAddress = ""
        myKovanAccount = Account(myKovanAddress, web3Instance)
        myKovanAccount.name = "Femi's Kovan Account 1"

        """         print("Balances")
            print("-----------")
            print(f"{myKovanAccount.name}: {myKovanAccount.getBalance()} ether")
            print("") """

        myKovanAccount.depositFundsToAave("AAVE", 0.05)

        sys.exit()
        

        # Get User Public Key
        try:
            numberOfAccounts = int(input("How many accounts would you like to track?\n"))
        except ValueError:
            print("Please enter a number")

        if numberOfAccounts <= 0:
            raise Exception("Number has to be greater than zero")

        # Instatiate an Account object
        accounts = []
        for i in range(numberOfAccounts):
            address = input("Please enter public key address:\n")
            accounts.append(Account(address, web3Instance))

        list(map(
                lambda x: print(f"Your account balance is: {x.getBalance()} ether"),
                accounts
                        ))

        # Get User favourites
        print("Please enter your favourite pairs and type 'done' when finished:\n")
        favourites = []
        i = 1
        while True:
            data = input(f"Favourite {i}: ")
            i += 1
            if 'done' == data:
                break
            favourites.append(data)

        # Instantaite User Objects
        user = User(favourites, mainnet_infura_url)
        prices = user.getPrices()
        print(prices)

if __name__ == "__main__":
    Main.main()


        