def check_highest_bids(bids):
    highest_bids = 0
    highest_bids_name = ""
    for key in bids:
        if bids[key] > highest_bids:
            highest_bids = bid[key]
            highest_bids_name = key
    return highest_bids, highest_bids_name


bids = {}
while True:
    name = input("What is your name ? : ")
    price = input("What is your bid ? : $")
    bids[name] = int(price)
    loop = input("ARE THERE ANY MORE BIDS ? (YES/NO) : ").lower()
    if loop == "no":
        break
    elif loop == "yes":
        continue
    else:
        break
winner_price, winner_name = check_highest_bids(bids)
print(f"THE WINNER IS '{winner_name.upper()}' WITH BID OF ${winner_price} .")

