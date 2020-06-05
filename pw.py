x = 3
while True:
	password = input('請輸入密碼')
	if password != ('a123456'):
		x = x - 1
		print('"密碼錯誤! 還有', x, '次機會"')
		if x == 0:
			print("錯誤")
			break
	else:
		print("登入成功")
		break