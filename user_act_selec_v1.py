usr_opt = ("add combo meal", "search for existing combos", "delete a combo", "output full menu")
usr_done = True
choice_num = 0
usr_opt_ref = 0
main_loop = True

while main_loop == True:
    print(usr_opt)
    choice_num = int(input(f"choose option you want to do (1-4): "))
    choice = False

    while choice == False:
        if 0 < choice_num < 5:
            usr_opt_ref = choice_num
            choice = True
        else:
            print("that number does not meet the relevent presented range")

