userid = "venu"
mobile = "32332323"
mylist2 = [3, "usa", 4, "india",]
for item in mylist2:
    try:
        if type(item) == int:
            if item % 2 == 0:
                print(f"my list item: {item}")
        else:
            print(f"User {userid} {mobile} input is bad")
            raise ValueError(f"{item} is not a integer")
    except Exception as err:
        print(f"An error occurred: {err}")