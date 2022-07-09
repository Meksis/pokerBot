from random import randint

deck_size = 36
prem_cards = 16
players = 2
test_amount = 4 						# УДАЛИТЬ КАК РЕШИТСЯ ВОПРОС С ПРОВЕРКОЙ НА ЦЕЛЬНОСТЬ КАРТЫ И КОЛОДЫ


def hand_gen(hand_inp):
	inner_hand_size = len(hand_inp)

	if inner_hand_size < hand_size:
		for apend_counter in range(hand_size - inner_hand_size):


			card_suit = list(cards_deck.keys())[randint(0, 3)]
			dict_value = cards_deck[card_suit]
			card_num = dict_value[randint(0, len(dict_value) - 1)]

			card = f'{card_suit}__{card_num}'

			#print(dict_value[ : dict_value.index(card_num)], dict_value[ dict_value.index(card_num) + 1 : ], dict_value[ : dict_value.index(card_num)] + dict_value[ dict_value.index(card_num) + 1 : ])


			cards_deck.update({card_suit : dict_value[ : dict_value.index(card_num)] + dict_value[ dict_value.index(card_num) + 1 : ]})
			hand_inp.append(card)

	
	#print(hand_inp, '\n',  cards_deck)



	return(hand_inp)





check_list = []

if 4 < players < 2:
	print('Incorrect players quantity')
	exit(0)


is_poker = False


cards_numeric_quantity = deck_size - prem_cards
card_min = int(11 - cards_numeric_quantity / 4)

cards_numeric = ['2', '3', '4', '5', '6', '7', '8', '9', '10']
cards_peoples = ["Jack", "Queen", "King", "Ace"]
cards_base = cards_numeric[ card_min -2  : ] + cards_peoples




if is_poker:
	cards_base.append('Joker')
	hand_size = 7
else:
	hand_size = 6

cards_deck = {'clubs' : cards_base, 
'pikes' : cards_base, 
'hearts' : cards_base, 
'tiles' : cards_base}






#hand_gen([])
#print()


expression_true = 1
cycle_counter = 0


hands = []

for hand_num in range(players):
	hands.append(hand_gen([]))

	print(f'hand_{hand_num+1} - {hands[-1]}')


trump = list(cards_deck.keys())[randint(0, 3)]
print(f'\nTrump - {trump}\n')






while expression_true:
	# APPENDING HANDS

	# ГОТОВО Объеденить руки-списки в один словарь или двумерный список чтобы не прописывать работу с каждым игроком отдельно
	# ГОТОВО Сделать проход по получившемуся контейнеру игроков, заполнить руки

	# В заполнитель рук добавить проверку на заполнение руки и наличие карт впринципе.


	for hand_counter, hand in enumerate(hands):
		hands.pop(hand_counter)
		hands.insert(hand_counter, hand_gen(hand))




	print(f'\nCards remained in deck: \n')
	for i in cards_deck:
		print(f'suit - {i}, cards - {cards_deck[i]}')





	if cycle_counter == test_amount:

		break

	else:

		cycle_counter += 1












