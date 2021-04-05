hrs = float(raw_input("Enter Hours:"))
rate = float(raw_input("Enter Rate:"))

if ( hrs <= 40 ):
	pay = hrs * rate

if ( hrs > 40 ):
	pay = 40 * rate
	pay = pay + ( 1.5 * rate * ( hrs - 40 ) )

print pay
