from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import random, uuid, sys

app_f = Flask(__name__)
app_f.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///war.db'
db = SQLAlchemy(app_f)

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    wins = db.Column(db.Integer, default=0)
    
    def __init__(self, id_t, name_t, wins_t):
        self.id = id_t
        self.name = name_t
        self.wins = wins_t

    def __repr__(self):
        return '<Player %r>' % self.name

app_f.app_context().push()
db.create_all()

def simulate_game(player1_s = 'Player 1', player2_s = 'Player 2'):
    
    deck_unique = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']
    deck = [2,3,4,5,6,7,8,9,10,'J','Q','K','A',2,3,4,5,6,7,8,9,10,'J','Q','K','A',2,3,4,5,6,7,8,9,10,'J','Q','K','A',
            2,3,4,5,6,7,8,9,10,'J','Q','K','A']
    
    random.shuffle(deck)
    deck_temp = deck.copy()
    
    count = len(deck)
    i = 0
    player1_deck = []
    player2_deck = []
    trace = []
    turn = 1
    
    while i < count:
        
        index = random.randint(0, len(deck_temp)-1)
        
        if turn == 1:
            player1_deck.append(deck_temp[index])
            deck_temp.pop(index)
            turn = 2
            
        elif turn == 2:
            player2_deck.append(deck_temp[index])
            deck_temp.pop(index)
            turn = 1
        
        i += 1

    player1_wins = 0
    player2_wins = 0

    while len(player1_deck) > 0 and len(player2_deck) > 0:
        player1_card = deck.index(player1_deck.pop())
        player2_card = deck.index(player2_deck.pop())

        if player1_card == player2_card:
            trace.append(('Tie', {'Player1card':player1_card}, {'Player2card':player2_card}))
            continue
        elif player1_card > player2_card:
            trace.append(('Player 1 wins', {'Player1card':player1_card}, {'Player2card':player2_card}))
            player1_wins += 1
        else:
            trace.append(('Player 2 wins', {'Player1card':player1_card}, {'Player2card':player2_card}))
            player2_wins += 1
    
    if player1_wins > player2_wins:
        winner = player1_s
    elif player2_wins > player1_wins:
        winner = player2_s
    else:
        winner = "Tie"
    
    return winner, trace

@app_f.route('/start_game', methods=['GET', 'POST'])
def start_game():
    winner, trace = simulate_game()
    player1_s = 'Player 1'
    player2_s = 'Player 2'
    player1 = db.session.query(Player).filter_by(name=player1_s).first()
    player2 = db.session.query(Player).filter_by(name=player2_s).first()
    
    if player1 == None:
        player1_row = Player(random.randint(0, sys.maxsize), player1_s, 0)
        db.session.add(player1_row)
        db.session.commit()
    
    if player2 == None:
        player2_row = Player(random.randint(0, sys.maxsize), player2_s, 0)
        db.session.add(player2_row)
        db.session.commit()
    
    player1 = db.session.query(Player).filter_by(name=player1_s).first()
    player2 = db.session.query(Player).filter_by(name=player2_s).first()
    
                
    if winner == player1_s:
        if player1 is not None:
            player1.wins += 1
    elif winner == player2_s:
        if player2 is not None:
            player2.wins += 1
    
    db.session.commit()
    
    return jsonify({'Status': 'New game started', 'winner': winner, 'trace': trace})

@app_f.route('/lifetime_wins', methods=['GET'])
def lifetime_wins():
    player1 = db.session.query(Player).filter_by(name='Player 1').first()
    player2 = db.session.query(Player).filter_by(name='Player 2').first()
    if player1 is not None and player2 is not None:
        return jsonify({"Player 1 lifetime wins": player1.wins, "Player 2 lifetime wins": player2.wins})
    elif player1 is not None:
        return jsonify({"Player 1 lifetime wins": player1.wins})
    elif player2 is not None:
        return jsonify({"Player 2 lifetime wins": player2.wins})
    else:
        return jsonify({"Player 1": player1, "Player 2": player2})

@app_f.route('/reset_game', methods=['GET', 'POST'])
def reset_game():
    db.drop_all()
    db.create_all()
    return jsonify({'Status': 'Game has been reset'})

if __name__ == '__main__':
    app_f.run(debug=True, host='0.0.0.0')
    