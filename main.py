# import lib
import datetime

print("Attendance Register: Please ensure you sign in and out while entering and leaving the office.")
print()
while True:
    time_stamp = input("Enter 1 to clock in, 2 to clock out, 3 to view hours spent at work and 4 to exit: ")
# specify time as now or system time
    now = datetime.datetime.now()
# lock time to start and finish by rendering sections redundant
    start_time = now.replace(hour=8, minute=0, second=0, microsecond=0)
    close_time = now.replace(hour=18, minute=0, second=0,microsecond=0)
# Note that you can nest if statements
    if time_stamp == "1":
        if now <= start_time:
            print("Welcome to work! Have a productive day.")
        else:
            print("You are late to work. Expect a query.")
    elif time_stamp == "2":
        if now >= close_time:
            print("Goodbye! I hope you had a productive day.")
        elif now <= close_time >= start_time:
            print("You have successfully clocked out.")
        else:
            print("Sorry, you can't clock out. It's not closing time yet.")
    elif time_stamp == "3":
        if now >= start_time <= close_time:
            print(f"You have spent {now - start_time} hours at work today.")
        else:
            print("Sorry, you can't view hours. It's not within work hours yet.")
    elif time_stamp == "4":
        break
    else:
        print("Invalid input.")



