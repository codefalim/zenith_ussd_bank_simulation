#This simple program will simulate the Zenith Bank Nigeria USSD Banking
#The program has the functionality to display USSD code for other Nigerian banks
#As a result it is called NIGERIA UNIFIED USSD BANKING (NUUB) where Zenith Bank is the
#only USSD Banking functionality available at the moment.

#NUUB platform has its own dedicated USSD which will be require to display
#Nigerian banks and their USSD Codes

#At the moment, the program recognize USSD Code for other banks but no functionalities
#yet except for Zenith bank



#Assuming we have some important global variable
all_banks_code = "*3428*#"
account_password = "1111"
account_phone_number = 2348034995327
account_number = 2217887645

def mainmenu():
    while True:
        print("Welcome to Nigeria Unified USSD Banking - NUUB PLATFORM\n-------------------------------------------------------")

        _bank = {"Access Bank":"*901#","Eco bank":"*326#","FCMB bank":"*329#","Fidelity Bank":"*770#","First Bank":"*894#",
                 "GTBank":"*737#","Heritage Bank":"*745#","Ja’iz Bank":" *389*301#","Keystone Bank":" *7111#","Polaris Bank":"*833#",
                 "Stabic IBTC Bank":"*909#","Standard Chartered Nigeria ":"*977#","Sterling Bank":"*822#","TajBank":"*898#", "UBA":"*919#",
                 "Union Bank of Nigeria":"*826#","Unity Bank":"*779#","Wema Bank":"*945#","Zenith Bank":"*966#"}

        display_bank_ussd = input("Kindly enter *3428*# to show available banks and their USSD code: \n->")
        if display_bank_ussd == all_banks_code:
            for bank_name, bank_code in _bank.items():
                print("| {}:{}".format(bank_name, bank_code))

            bank_ussd = input("Enter your bank code as shown above: \n->")
            for bank_name, bank_code in _bank.items():
                if bank_ussd == bank_code:
                    print("Thank you, for choosing " + bank_name + "\n--------------------------------")
                    navigate = int(input("Select an option\n1.Choose different bank\n2.Menu\n3.Continue\n->"))
                    if navigate == 1:
                        continue
                    if navigate == 2:
                        exit(0)
                    if navigate == 3:
                        if bank_name == "Zenith Bank":
                            print("Welcome to Easybanking by Zenith\nBank\n_____________________\nSelect an option:")
                            menu = {"1":"Open Account", "2":"Get a Card", "3":"Register", "4":"Check Balance",
                                    "5":"Airtime", "6":"Transfers", "7":"Self Service", "8":"Next\n->"}

                            for option, activity in menu.items():
                                print("|{}>{}".format(option, activity))

                            option_select = int(input("Enter your option here\n->"))

                            if option_select == 1:
                                print("Register with the Debit Card\n")
                                card_details = input("Enter the last six digit of your card:\n->")

                                print("Thank you for registering for our\n*966# service. Press any no. to start\nbanking")
                                navigate = int(input("Select an option\n1.Choose different bank\n2.End\n->"))
                                if navigate == 1:
                                    continue
                                if navigate == 2:
                                    exit(0)

                            if option_select == 2:
                                card_menu = {"1":"Get a Virtual Card","2":"Retrieve Card PAN/CVV",
                                             "3":"Create Card PIN","4":"Reactivate Card"}

                                for option, activity in card_menu.items():
                                    print("|{}>{}".format(option, activity))

                                    option_select = int(input("Enter your choice\n> "))
                                    if option_select == 1:
                                        print("Getting card")
                                        navigate = int(input("Select an option\n1.Choose different bank\n2. End\n->"))
                                        if navigate == 1:
                                            continue
                                        if navigate == 2:
                                            exit(0)
                                    if option_select == 2:
                                        print("Retrieving card PAN/CVV")
                                        navigate = int(input("Select an option\n1.Choose different bank\n2.End\n->"))
                                        if navigate == 1:
                                            continue
                                        if navigate == 2:
                                            exit(0)

                                    if option_select == 3:
                                        print("Deactivating card")
                                        navigate = int(input("Select an option\n1.Choose different bank\n2.End\n->"))
                                        if navigate == 1:
                                            continue
                                        if navigate == 2:
                                            exit(0)

                                    if option_select == 4:
                                        print("Reactivating Card")
                                        navigate = int(input("Select an option\n1.Choose different bank\n2.End\n->"))
                                        if navigate == 1:
                                            continue
                                        if navigate == 2:
                                            exit(0)

                            if option_select == 3:
                                register = int(input("Enter account number to register:\n->"))

                                if register == account_number:
                                    print("You are already enrolled. Press any\nno. start banking")
                                    navigate = int(input("Select an option\n1.Choose different bank\n2.End\n->"))
                                    if navigate == 1:
                                        continue
                                    if navigate == 2:
                                        exit(0)
                                if register != account_number:
                                    navigate = int(input("You do not have an account\n1.Open account\n2.End\n->"))
                                    if navigate == 1:
                                        continue
                                    if navigate == 2:
                                        exit(0)

                            if option_select == 4:
                                account_prompt = int(input("Enter account number to check\nbalance:\n->"))
                                if account_prompt == account_number:

                                    pin = input("Enter pin to check balance\n->")
                                    if pin == account_password:
                                        print("Retrieving Balance...An SMS\nwill be sent to you shortly. Enjoy\n"
                                              "easybanking with us.\nTransfer: *966*Amount*AccountNo#\nPayment:*966*7*Amount*RefNo#")
                                        navigate = int(input("Select an option\n1.Choose different bank\n2.End\n->"))
                                        if navigate == 1:
                                            continue
                                        if navigate == 2:
                                            exit(0)
                                if account_prompt != account_number:
                                    pin = input("Enter pin to check balance\n->")
                                    if pin == pin:
                                        print("USSD authentification failed!")
                                        navigate = int(input("Select an option\n1.Choose different bank\n2.End\n->"))
                                        if navigate == 1:
                                            continue
                                        if navigate == 2:
                                            exit(0)


                            if option_select == 5:
                                airtime_menu = {"1":"Self","2":"Others"}

                                for option, activity in airtime_menu.items():
                                    print("{}>{}".format(option, activity))

                                option_select = int(input("Enter your option here:\n> "))
                                if option_select == 1:
                                    amount = input("Enter amount:\n>")

                                    print("You are about to buy airtime for\nPhone Number:{} \nAmount: {} \n".format(account_phone_number, amount))
                                    pin = input("Enter pin to purchase airtime\n->")
                                    if pin == account_password:
                                        print("You have sucessfully sent NGN{} airtime to {}".format(amount,account_phone_number))
                                        navigate = int(input("Select an option\n1.Choose different bank\n2.End\n->"))
                                        if navigate == 1:
                                            continue
                                        if navigate == 2:
                                            exit(0)

                                    if pin != account_password:
                                        print("USSD Authentification Failed. Please\nconfirm your credentials is correct\n or your account is active on this platform")
                                        navigate = int(input("Select an option\n1.Choose different bank\n2.End\n->"))
                                        if navigate == 1:
                                            continue
                                        if navigate == 2:
                                            exit(0)
                                if option_select == 2:
                                    amount = input("Enter amount>")
                                    self_phone_number = input("Enter phone number>")

                                    print("You are about to buy airtime for\nPhone Number:", self_phone_number
                                          + "\nAmount:", amount, "\n")
                                    pin = input("Enter pin to purchase airtime\n->")
                                    if pin == account_password:
                                        print(
                                            "You have sucessfully sent NGN", amount, "airtime to ",
                                            self_phone_number)
                                        navigate = int(
                                            input("Select an option\n1.Choose different bank\n2.End\n->"))
                                        if navigate == 1:
                                            continue
                                        if navigate == 2:
                                            exit(0)

                                    else:
                                        print(
                                            "USSD Authentification Failed. Please\nconfirm your credentials is correct\n"
                                            "or your account is active on this platform")
                                        navigate = int(
                                            input("Select an option\n1.Choose different bank\n2.End\n->"))
                                        if navigate == 1:
                                            continue
                                        if navigate == 2:
                                            exit(0)

                                if option_select == 3:
                                    print("Retrieving card PAN/CVV")
                                    navigate = int(input("Select an option\n1.Choose different bank\n2.End\n->"))
                                    if navigate == 1:
                                        continue
                                    if navigate == 2:
                                        exit(0)

                                if option_select == 4:
                                    print("Deactivating card")
                                    navigate = int(input("Select an option\n1.Choose different bank\n2.End\n->"))
                                    if navigate == 1:
                                        continue
                                    if navigate == 2:
                                        exit(0)

                                if option_select == 5:
                                    print("Reactivating Card")
                                    navigate = int(input("Select an option\n1.Choose different bank\n2.End\n->"))
                                    if navigate == 1:
                                        continue
                                    if navigate == 2:
                                        exit(0)

                            if option_select == 6:
                                amount = input("Enter amount:\n>")
                                send_money = input("Enter Account number:\n>")
                                print("Transfer Funds\n1>Bank 1\n2>Bank 2\n3>Bank 3\n4>Bank 4\n5>Bank 5\n6>Other banks")
                                if send_money == send_money:
                                    print("You are about to send\nAmount:{} \nRecipient: FIRST_NAME LAST_NAME \nBank: Bank Name\n".format(amount))
                                pin = input("Enter PIN to confirm:\n->")
                                if pin == account_password:
                                    print("Transaction successful!")
                                    navigate = int(input("Select an option\n1.Choose different bank\n2.End\n->"))
                                    if navigate == 1:
                                        continue
                                    if navigate == 2:
                                        exit(0)

                                if pin != account_password:
                                    print(
                                        "USSD Authentification Failed. Please\nconfirm your credentials is correct\n or your account is active on this platform")
                                    navigate = int(input("Select an option\n1.Choose different bank\n2.End\n->"))
                                    if navigate == 1:
                                        continue
                                    if navigate == 2:
                                        exit(0)
                                navigate = int(input("Select an option\n1.Choose different bank\n2.End\n->"))
                                if navigate == 1:
                                    continue
                                if navigate == 2:
                                    exit(0)

                            if option_select == 7:
                                print("Self service function codes...")
                                navigate = int(input("Select an option\n1.Choose different bank\n2.End\n->"))
                                if navigate == 1:
                                    continue
                                if navigate == 2:
                                    exit(0)

                            if option_select == 8:

                                print("Next function codes...")

                                navigate = int(input("Select an option\n1.Choose different bank\n2.End\n->"))
                                if navigate == 1:
                                    continue
                                if navigate == 2:
                                    exit(0)


                        elif bank_name != "Zenith Bank":
                            print("Sorry, only Zenith bank USSD banking is available at the moment.")
                            navigate = int(input("Select an option\n1.Choose different bank\n2.End\n->"))
                            if navigate == 1:
                                continue
                            if navigate == 2:
                                exit(0)

                        navigate = int(input("Select an option\n1.Choose different bank\n2.End\n->"))
                        if navigate == 1:
                            continue
                        if navigate == 2:
                            exit(0)

        elif display_bank_ussd != all_banks_code:
            print("Wrong NUUB USSD entered!")
            navigate = int(input("Select an option\n1.Choose different bank\n2.End\n->"))
            if navigate == 1:
                continue
            if navigate == 2:
                exit(0)




mainmenu()
