while True:

	month = {	
	'1':'January',
	'2':'February',
	'3':'March',
	'4':'April',
	'5':'May',
	'6':'June',
	'7':'July',
	'8':'August',
	'9':'September',
	'10':'October',
	'11':'November',
	'12':'December'		}
		
	print('Enter a number from 1 to 12 to get a month with its related number.')
	
	key = input('Type a number:')
	
	if key in month:
		print('The month is', month[key])
	else:
		print('You entered a wrong value')
	
