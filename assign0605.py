text = "X-DSPAM-Confidence:    0.8475"
start = text.find(":")
number = text[start+1:]
flo_number = float(number.strip())
print(flo_number)
