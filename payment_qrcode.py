import qrcode

upi_id = input("Enter your UPI ID: ")
amount = int(input("Enter amount to pay: "))
#general payment url
#upi://pay?pa=UPI_ID&pn=NAME&am=AMOUNT&cu=CURRENCY&tn=MESSAGE

phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&am={amount}'
googlepay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name={amount}'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name={amount}'

#making qr codes
phonepe_qr = qrcode.make(phonepe_url)
googlepay_qr = qrcode.make(googlepay_url)
paytm_qr = qrcode.make(paytm_url)

# #saving qr codes
# phonepe_qr.save("phonepe_qr.png")
# googlepay_qr.save("googlepay_qr.png")
# paytm_qr.save("paytm_qr.png")

#show qr code

mode = input("Enter payment mode\n1. Phone Pe\n2. Google Pay\n3. Paytm\n")
if (mode == '1'):
    phonepe_qr.show()
elif(mode == '3'):
    paytm_qr.show()
elif(mode == '2'):
    googlepay_qr.show()
else:
    print("Invalid Mode!")
