# Class that executes the main script
from .account import Account
from .user import User

class Main:

    @staticmethod
    def main():

        # Define ganache endpoint
        ganacheUrl = "http://127.0.0.1:7545"
        #Mainet infura endpoinnt
        infura_url = "https://mainnet.infura.io/v3/e84a16c980ca45c8a3e33da73f2a1bf3"


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
            accounts.append(Account(address, ganacheUrl))

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
        user = User(favourites, infura_url)
        prices = user.getPrices()
        print(prices)

if __name__ == "__main__":
    Main.main()


        