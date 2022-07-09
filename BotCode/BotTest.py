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

			if dict_value == []:
				for card_suit_check in cards_deck:
					if cards_deck[card_suit_check] == []:
						pass

					else:
						dict_value = cards_deck[card_suit_check]
						#print(f'[!]changed dict_value to {card_suit_check} - {dict_value}\n')
						break

			if dict_value == []:
				return(hand_inp)

			#print(f'dict_val - {dict_value}')
			card_num = dict_value[randint(0, len(dict_value) - 1)]

			card = f'{card_suit}__{card_num}'

			#print(dict_value[ : dict_value.index(card_num)], dict_value[ dict_value.index(card_num) + 1 : ], dict_value[ : dict_value.index(card_num)] + dict_value[ dict_value.index(card_num) + 1 : ])


			cards_deck.update({card_suit : dict_value[ : dict_value.index(card_num)] + dict_value[ dict_value.index(card_num) + 1 : ]})
			hand_inp.append(card)

	
	#print(hand_inp, '\n',  cards_deck)



	return(hand_inp)

def check_table(table_inner, card_check):

	if len(table_inner) >= 1:
		cards_data = []
		card_check = card_check.split('__')

		suit_check = card_check[0]
		num_check = card_check[1]
		is_trump = True if suit_check == trump else False

		card_check = [suit_check, cards_all[suit_check].index(num_check), is_trump]


		for card in table_inner:
			card = card.split('__')
			suit = card[0]
			num = card[1]
			is_trump = True if suit == trump else False

			cards_data.append([suit, cards_all[suit].index(num), is_trump])

		#print(f'[!] cards_data - {cards_data}')


		ret_bool = False

		for card in cards_data:
			#print(f'[!] card_data = {card}, check_card = {card_check}')
			if card_check[2]:
				if card[2]:
					if card_check[1] > card[1] and card_check[0] == card[0]:
						ret_bool = True
				else:
					ret_bool = True


			else:
				if not card[2]:
					if card_check[1] > card[1] and card_check[0] == card[0]:
						ret_bool = True

		return(ret_bool)

	else:
		return(False)






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



SPADES = '♠️'
HEARTS = '♥️'
DIAMS = '♦️'
CLUBS = '♣️'

cards_deck = {'♣️' : cards_base, 
'♠️' : cards_base, 
'♥️' : cards_base, 
'♦️' : cards_base}


cards_all = {'♣️' : cards_base, 
'♠️' : cards_base, 
'♥️' : cards_base, 
'♦️' : cards_base}



'''
cards_deck = {'clubs' : cards_base, 
'pikes' : cards_base, 
'hearts' : cards_base, 
'tiles' : cards_base}


cards_all = {'clubs' : cards_base, 
'pikes' : cards_base, 
'hearts' : cards_base, 
'tiles' : cards_base}




'''






#hand_gen([])
#print()


expression_true = 1
cycle_counter = 0


hands = []

for hand_num in range(players):
	hands.append(hand_gen([]))

	#print(f'hand_{hand_num+1} - {hands[-1]}')


trump = list(cards_deck.keys())[randint(0, 3)]
print(f'\n[!]Trump - {trump}\n')




trash_cards = []

while expression_true:
	# APPENDING HANDS

	# ГОТОВО Объеденить руки-списки в один словарь или двумерный список чтобы не прописывать работу с каждым игроком отдельно
	# ГОТОВО Сделать проход по получившемуся контейнеру игроков, заполнить руки

	# ГОТОВО В заполнитель рук добавить проверку на заполнение руки и наличие карт впринципе.


	for hand_counter, hand in enumerate(hands):
		hands.pop(hand_counter)
		hands.insert(hand_counter, hand_gen(hand))

	table = []



	main_user_hand = hands[0]

	main_user_hand.sort()




	

	

	for hand_id in range(1, players):
		hand = hands[hand_id]
		card_throw = hand[randint(0, len(hand) - 1)]

		hand.remove(card_throw)
		hands[hand_id] = hand

		print(f'''\nhand_{hand_id} throwed "{card_throw}", it\'s hand - {hand}''')

		table.append(card_throw)

	print(f'\n\n[!] Table cards now - {table}\n\n')



	print(f'Our hand is {main_user_hand}')

	#table.append(card_throw)

	flag_check = False

	can_trash = []

	for user_card in main_user_hand:
		can_trash.append(check_table(table, user_card))

	if True not in can_trash:
		print('[!] User have not cards to trash table\n')
		continue


	while not flag_check:
		card_throw = main_user_hand[int(input(('Choose card: '))) - 1]

		

		print(f'''User throwed "{card_throw}"''')

		if check_table(table, card_throw):
			print(f'\n\n[!] Table trashed')
			
			trash_cards.append(table[0])
			trash_cards.append(card_throw)

			main_user_hand.remove(card_throw)
			hands[0] = main_user_hand

			flag_check = True

			table.append(card_throw)
		else:
			print(f'\n\n[!] Check table is False')


	'''print(f'\nCards remained in deck: \n')
				for i in cards_deck:
					print(f'suit - {i}, cards - {cards_deck[i]}')
				print('\n\n')
			'''




	if cycle_counter == test_amount:
		print(f'\n\n[!] TRASH CARDS IS {trash_cards}')
		break

	else:

		cycle_counter += 1












