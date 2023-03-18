from datetime import datetime

print("WELCOME TO YOUR CLOCK-IN DEVICE")

clockIn = input("Enter 'arrive' or 'leave': ").lower()  # lowercase input to avoid errors

if clockIn == "arrive":
    # set arrival time to 8:00 AM
    arrive = datetime.now().replace(hour=8, minute=0, second=0, microsecond=0)

    # get current time
    current_time = datetime.now().strftime("%H:%M:%S")

    # check if user arrived on time or not
    if datetime.now() <= arrive:
        print(f"Welcome to work! You arrived at {current_time} today, keep it up!")
    else:
        print("You are late and a penalty of GHC5.00 will apply.")

else:
    # set closing time to 10:00 AM
    leave = datetime.now().replace(hour=10, minute=0, second=0, microsecond=0)

    # get user's clock-out time
    closureTime = datetime.now().strftime("%H:%M:%S")

    # check if user is leaving on time or not
    if datetime.now() >= leave:
        print("I hope you had a good day at work today! See you tomorrow.")
    else:
        print(f"Sorry, it's too early to close! Our closing time is {leave}.")











