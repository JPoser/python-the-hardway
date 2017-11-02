lexicon = {
	'north': 'direction',
	'south': 'direction',
	'east': 'direction',
	'west': 'diection',
	'go': 'verb',
	'kill': 'verb',
	'eat': 'verb',
	'the': 'stop',
	'in': 'stop',
	'of': 'stop',
	'bear': 'noun',
	'princess': 'noun',
	3: 'number',
	1234: 'number',
	91234: 'number'

}

def scan(sentence):
	# scans a sentence and returns a tuple containing
	# the type of action and the it's adjunct
	words = sentence.split()
	output = []
	for word in words:
		if word in lexicon:
			lexicon.get(word)
			output_tup = (lexicon.get(word), word)
			output.append(output_tup)
		elif word not in lexicon and isinstance(convert_number(word), (int, long)):
			number = convert_number(word)
			output_tup = (lexicon.get(number), number)
			output.append(output_tup)
		else:
			output_tup = ('error', word)
			output.append(output_tup)
	return output

def convert_number(s):
	try:
		return int(s)
	except ValueError:
		return None