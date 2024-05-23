import subprocess

# traverse the software list
Data = subprocess.check_output(['wmic', 'product', 'get', 'name'])
a = str(Data)

# try block
try:

	# arrange the string
	for i in range(len(a)):
		print(a.split("\\r\\r\\n")[6:][i])

except IndexError as e:
	print("All Done")

