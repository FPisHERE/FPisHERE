hrs = input("Enter Hours:")
rph = input("Enter rate:")
try:
    h = float(hrs)
    r = float(rph)
except:
    print("Error, please enter numeric input.")
    quit()
print(h,r)
if h <= 40:
    pay = h * r
else:
    pay = 40 * r + (h - 40) * r * 1.5
print(pay)
