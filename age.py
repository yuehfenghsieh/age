driving = input ('有沒有開過車?')
if driving != '有' and driving != '沒有':
	print('只能輸入有/沒有')
	raise SystemExit
age = input ('你現在幾歲?')
age = int(age)
if driving == '有':
	if age >= 18:
		print('你有合法開車資格')
	else:
		print('奇怪你怎麼開過車')
elif driving == '沒有':
	if age >= 18:
		print('你可以去考駕照了!')
	else:
		print('再過幾年你就可以考駕照了')