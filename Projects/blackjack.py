import random

def create_deck():
  ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
  suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
  deck = [{'rank': rank, 'suit': suit} for suit in suits for rank in ranks]
  random.shuffle(deck)
  return deck

def deal_hand(hand, hidden):
  if hidden:
    print('House card:', f"{ hand[0]['rank'] } of { hand[0]['suit'] }")
    print('House card: Flipped Over')
  else:
    for card in hand:
      print('Your cards:', f"{ card['rank'] } of { card['suit'] }")
  return hand

def card_value(card):
  rank = card['rank']
  if rank in [ 'J', 'Q', 'K']:
    return 10
  elif rank == 'A':
    return 11
  else:
    return int(rank)

def count_Score(hand):
  score = 0
  for card in hand:
    score += card_value(card)
  return score

def play_hit(player_hand, house_score, deck):
  new_card = deck.pop()
  player_hand.append(new_card) # grabs new card
  player_score = count_Score(player_hand) # gets new score

  if player_score > 21:
    print(f'\nYou flipped a {new_card['rank']}. Your total is {player_score}')
    print('Bust! You lose')
  elif player_score == 21:
    print(f'\nYou flipped a {new_card['rank']}. Your total is {player_score}')
    print('Blackjack! You win')
  else:
    for card in player_hand:
      print('Your cards:', f"{ card['rank'] } of { card['suit'] }") # prints out new list of player cards
    print("~---~---~---~----~---~---~---~----~")
    print(f"Your total: { player_score } | House total: { house_score }") # prints out total game score

    game_choice = input("Do you want to 'hit' or 'stand'? ").lower()
    if game_choice == 'hit':
      play_hit(player_hand, house_score, deck)
    else:
      play_stand(player_score, house_score)

def play_stand(player_score, house_score, house_hand, deck):
  while house_score < player_score and house_score < 21:
    house_hand.append(deck.pop())
    house_score = count_Score(house_hand)

  if player_score < house_score and house_score < 21:
    print('You lost')
  elif player_score > house_score and player_score < 21:
    print('You win')
  elif player_score == 21:
    print('Blackjack! You win')
  elif house_score == 21:
    print('House got Blackjack! You lose')
  else:
    print("Draw")
  return player_score, house_score

def black_jack():
  deck = create_deck()

  print("~---~---~---~----~---~---~---~----~")
  player_hand = [deck.pop(), deck.pop()]
  house_hand = [deck.pop(), deck.pop()]
  deal_hand(player_hand, hidden = False)
  deal_hand(house_hand, hidden = True)
  player_score = count_Score(player_hand)
  house_score = count_Score(house_hand)

  print("~---~---~---~----~---~---~---~----~")
  print(f"Your total: { player_score } | House total: { house_score }")
  if player_score == 21:
    return print('Blackjack! You win!')
  print("___________________________________")
  game_choice = input("Do you want to 'hit' or 'stand'? ").lower()
  
  if game_choice == 'hit':
    play_hit(player_hand, house_score, deck)
  elif game_choice == 'stand':
    play_stand(player_score, house_score, house_hand, deck)

black_jack()