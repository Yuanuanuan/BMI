height = input('請輸入身高: ')
weight = input('請輸入體重: ')
height = float(height)
weight = float(weight)
BMI = weight/((height/100)**2)
if BMI >=18.5 and BMI < 24:
	print('你的BMI為: ', BMI, '體重正常')
elif BMI >= 24 and BMI < 27:
	print('你的BMI為: ', BMI, '體重過重')
elif BMI < 18.5:
	print('你的BMI為: ', BMI, '體重過輕')
elif BMI >=27 and BMI < 30:
	print('你的BMI為: ', BMI, '輕度肥胖')
elif BMI >= 30 and BMI < 35:
	print('你的BMI為: ', BMI, '中度肥胖')
elif BMI >= 35:
	print('你的BMI為: ', BMI, '重度肥胖')