# Angelo Andrade
# payRoll_ex_04_06
# 9/8/24

def computepay(hours, rate) :
    # print("In computePay", hours, rate)
    if fh > 40:

        reg = rate * hours
        otp = (hours - 40.0) * (rate * 0.5)
        pay = reg + otp
    else:
        pay = hours * rate
    # print("Returning",pay)
    return pay
sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
fh = float(sh)
fr = float(sr)
# print(fh, fr)
xp = computepay(fh,fr)

print("Pay: ",xp)