from random import randint

deck_size = 36
prem_cards = 16
players = 2
test_amount = 4 
check_list = []
expression_true = True
cycle_counter = 0
hands = []
trash_cards = []

is_poker = False
#проверка игры
if is_poker:
	cards_base.append('Joker')
	hand_size = 2
else:
	hand_size = 6


#заполнение руки с проверкой карт в колоде 
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
						break

			if dict_value == []:
				return(hand_inp)

			card_num = dict_value[randint(0, len(dict_value) - 1)]

			card = f'{card_suit}__{card_num}'


			cards_deck.update({card_suit : dict_value[ : dict_value.index(card_num)] + dict_value[ dict_value.index(card_num) + 1 : ]})
			hand_inp.append(card)


	return(hand_inp)

#проверка на отбивание карты 
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


		ret_bool = False

		for card in cards_data:
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


#проверка на количество игроков
if 4 < players < 2:
	print('Incorrect players quantity')
	exit(0)


#кол-во карт с числами
card_min = int(11 - (deck_size - prem_cards) / 4)


#все возможные карты 
cards_numeric = ['2', '3', '4', '5', '6', '7', '8', '9', '10']
cards_peoples = ["Jack", "Queen", "King", "Ace"]
cards_base = cards_numeric[ card_min -2  : ] + cards_peoples

#колода для игры (меняется)
cards_deck = {'\u2663' : cards_base,  '\u2660' : cards_base,  '\u2665' : cards_base,  '\u2666' : cards_base}
#список карт для игры(не меняется) 
cards_all = {'\u2663' : cards_base, '\u2660' : cards_base, '\u2665' : cards_base, '\u2666' : cards_base}

#hands-2мерный список с руками всех игроков 
for hand_num in range(players):
	hands.append(hand_gen([]))

#определение козыря
trump = list(cards_deck.keys())[randint(0, 3)]
print(f'\n[!]Trump - {trump}\n')


#логика игры
while expression_true:

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

		print(f'''\nhand_{hand_id} throwed "{card_throw}"''')

		table.append(card_throw)

	print(f'\n\n[!] Table cards now - {table}\n\n')

	print(f'Our hand is {main_user_hand}')

	flag_check = False

	can_trash = []

	for user_card in main_user_hand:
		can_trash.append(check_table(table, user_card))

	if True not in can_trash:	
		print('[!] User have not cards to trash table and grabed cards\n')	

		main_user_hand.append(table[0])
		main_user_hand.sort()

		continue


	while not flag_check:
		inp_num = int(input(('Choose card: '))) - 1

		if inp_num == -1:
			main_user_hand.append(table[0])
			main_user_hand.sort()

			print(f'[!]User grabed table cards')

			break

		#elif len(main_user_hand) -1 > inp_num > -1:

		elif inp_num > (len(main_user_hand) -1) or inp_num < -1:  # 12
			print(f'[!]Check selected card number')

		else:

			card_throw = main_user_hand[inp_num]

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
				print(f'\n\n[!] Cant trash via this card')

	print('\n\n','=='*10)




	if cycle_counter == test_amount:
		print(f'\n\n[!] TRASH CARDS IS {trash_cards}')
		break

	else:

		cycle_counter += 1