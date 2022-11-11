NamesOFClients = ['Ajay Sinha', 'Benny Dayal', 'Sanjay Mathur', 'Chaturthi Malvankar', 'Ajith Malhotra', 'Raj Singhania', 'Jatin Patel']
ClientPins = ['1111', '1111', '1111', '1111', '1111', '1111', '1111']
ClientBalances = [10000, 20000, 30000, 40000, 50000, 60000, 70000]
ClientDeposition = 0
ClientWithdrawal = 0
ClientBalance = 0
start_index = 1
end_index = 7
new_clients = 0  # Limit till which the number of clients can be added.
while True:
    # os.system("cls")
    print("************************************************************")
    print("========== WELCOME TO ITSOURCECODE BANKING SYSTEM ==========")
    print("************************************************************")
    print("==========     (1). Open New Client Account     ============")
    print("==========     (2). The Client Withdraw a Money ============")
    print("==========     (3). The Client Deposit a Money  ============")
    print("==========     (4). Check Clients & Balance     ============")
    print("==========     (5). Quit                        ============")
    print("************************************************************")

    EnterLetter = input("Select a Letter from the Above Box menu : ")
    if EnterLetter == "1":
        print("*****Create User*****")
        NumberOfClient = eval(input("Number of Clients : "))
        new_clients = new_clients + NumberOfClient

        if new_clients > 7:
            print("\n")
            print("Client registration exceed reached or Client registration too low")
            new_clients = new_clients - NumberOfClient
        else:
            while start_index <= new_clients:
                name = input("Write Your Fullname : ")
                NamesOFClients.append(name)
                pin = str(input("Please Write a Pin to Secure your Account : "))
                ClientPins.append(pin)
                ClientBalance = 0
                ClientDeposition = eval(input("Please Insert a Money to Deposit to Start an Account : "))
                ClientBalance = ClientBalance + ClientDeposition
                ClientBalances.append(ClientBalance)
                print("\nName=", end=" ")
                print(NamesOFClients[end_index])
                print("Pin=", end=" ")
                print(ClientPins[end_index])
                print("Balance=", "P", end=" ")
                print(ClientBalances[end_index], end=" ")
                start_index = start_index + 1
                end_index = end_index + 1
                print("\nYour name is added to Client Table")
                print("Your pin is added to Client Table")
                print("Your balance is added to Client Table")
                print("----New Client account created successfully !----")

        mainMenu = input(" Press Enter Key to go Back to Main Menu to Conduct Another Transaction or Quit_")
    elif EnterLetter == "2":
        v = 0
        print(" letter b is Selected by the Client")
        while v < 1:
            w = -1
            name = input("Please Insert a name : ")
            pin = input("Please Insert a pin : ")
            while w < len(NamesOFClients) - 1:
                w = w + 1
                if name == NamesOFClients[w]:
                    if pin == ClientPins[w]:
                        v = v + 1
                        print("Your Current Balance:", "P", end=" ")
                        print(ClientBalances[w], end=" ")
                        print("\n")
                        ClientBalance = (ClientBalances[w])
                        ClientWithdrawal = eval(input("Insert value to Withdraw : "))
                        if ClientWithdrawal > ClientBalance:
                            deposition = eval(input(
                                "Please withdraw a lower Value because your Balance mentioned above is not enough : "))
                            ClientBalance = ClientBalance + deposition
                            print("Your Current Balance:", "P", end=" ")
                            print(ClientBalance, end=" ")
                            ClientBalance = ClientBalance - ClientWithdrawal
                            print("-\n")
                            print("----Withdraw Successfully!----")
                            ClientBalances[w] = ClientBalance
                            print("Your New Balance: ", "P", ClientBalance, end=" ")
                            print("\n\n")
                        else:
                            ClientBalance = ClientBalance - ClientWithdrawal
                            print("\n")
                            print("----Withdraw Successfully!----")
                            ClientBalances[w] = ClientBalance
                            print("Your New Balance: ", "P", ClientBalance, end=" ")
                            print("\n")
            if v < 1:
                print("Your name and pin does not match!\n")
                break
        mainMenu = input(" Press Enter Key to go Back to Main Menu to Conduct Another Transaction or Quit_")
    elif EnterLetter == "3":
        print("Letter c is selected by the Client")
        x = 0
        while x < 1:
            w = -1
            name = input("Please Insert a name : ")
            pin = input("Please Insert a pin : ")
            while w < len(NamesOFClients) - 1:
                w = w + 1
                if name == NamesOFClients[w]:
                    if pin == ClientPins[w]:
                        x = x + 1
                        print("Your Current Balance: ", "P", end=" ")
                        print(ClientBalances[w], end=" ")
                        ClientBalance = (ClientBalances[w])
                        print("\n")
                        ClientDeposition = eval(input("Enter the value you want to deposit : "))
                        ClientBalance = ClientBalance + ClientDeposition
                        ClientBalances[w] = ClientBalance
                        print("\n")
                        print("----Deposition successful!----")
                        print("Your New Balance: ", "P", ClientBalance, end=" ")
                        print("\n")
            if x < 1:
                print("Your name and pin does not match!\n")
                break
        mainMenu = input(" Press Enter Key to go Back to Main Menu to Conduct Another Transaction or Quit_")
    elif EnterLetter == "4":
        print("Letter d is selected by the Client")
        w = 0
        print("Client name list and balances mentioned below : ")
        print("\n")
        while w <= len(NamesOFClients) - 1:
            print("->.Customer =", NamesOFClients[w])
            print("->.Balance =", "P", ClientBalances[w], end=" ")

            print("\n")
            w = w + 1
        mainMenu = input(" Press Enter Key to go Back to Main Menu to Conduct Another Transaction or Quit_ ")
    elif EnterLetter == "5":
        print("letter e is selected by the client")
        print("Thank you for using our banking system!")
        print("\n")
        print("Thank You and Come again")
        print("God Bless")
        break
    else:
        print("Invalid option selected by the Client")
        print("Please Try again!")

        mainMenu = input("Press Enter Key to go Back to Main Menu to Conduct Another Transaction or Quit_")