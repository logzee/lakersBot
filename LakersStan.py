from LakersChatBot import ChatBot


class LakersStan(ChatBot):

  STATES = [
    'waiting',
    'welcome',
    'Lakers fan',
    'Lakers Hater',
    'Basketball fan',
    'not basketball fan',
    'saw the last game',
    'didnt catch the last game',
  ]
  
  TAGS = {
    # descriptors
    'like': 'positive',
    'fan': 'positive',
    'dont like': 'negative',
    
    #Greatings
    'Hello': 'Hello',
    'Hi': 'Hello',
    'Greetings': 'Hello',
    'Howdy': 'Hello',
    'Hey': 'Hello',
    
    #yes / no
    'yes': 'yes',
    'Yeah': 'yes',
    'no': 'no',
    'nah': 'no'
  }
    
    
  TEAMS = {
    'Atlanta Hawks': 'Hawks',
    'Atlanta': 'Hawks',
    'Hawks': 'Hawks',
    'Boston Celtics': 'Celtics',
    'Boston': 'Celtics',
    'Celtics': 'Celtics',
    'Brooklyn Nets': 'Nets',
    'Brooklyn Nets': 'Nets',
    'Nets': 'Nets',
    'Charlotte Hornets': 'Hornets',
    'Charlotte': 'Hornets',
    'Hornets': 'Hornets',
    'Chicago Bulls': 'Bulls',
    'Chicago': 'Bulls,
    'Bulls': 'Bulls',
    'Cleveland Cavaliers': 'Cavaliers',
    'Cleveland': 'Cavaliers',
    'Cavaliers': 'Cavaliers',
    'Dallas Mavericks': 'Mavericks',
    'Dallas': 'Mavericks',
    'Mavericks': 'Mavericks',
    'Denver Nuggets': 'Nuggets',
    'Denver': 'Nuggets',
    'Nuggets': 'Nuggets',
    'Detroit Pistons': 'Pistons',
    'Detroit': 'Pistons',
    'Pistons': 'Pistons',
    'Golden State Warriors': 'Warriors',
    'Golden State': 'Warriors',
    'Warriors': 'Warriors',
    'Houston Rockets': 'Rockets',
    'Houston': 'Rockets',
    'Rockets': 'Rockets
    'Indiana Pacers': 'Pacers',
    'Indiana': 'Pacers',
    'Pacers': 'Pacers',
    'LA Clippers': 'Clippers',
    'LA': 'Clippers',
    'Clippers': 'Clippers',
    'Los Angeles Lakers': 'Lakers',
    'Los Angeles': 'Lakers',
    'Lakers', 'Lakers',
    'Memphis Grizzlies': 'Grizzlies',
    'Memphis': 'Grizzlies',
    'Grizzlies': 'Grizzlies',
    'Miami Heat': 'Heat',
    'Miami': 'Heat',
    'Heat': 'Heat',
    'Milwaukee Bucks': 'Bucks',
    'Milwuakee': 'Bucks',
    'Bucks': 'Bucks',
    'Minnesota Timberwolves': 'Timberwolves',
    'Minnesota': 'Timberwolves',
    'Timberwolves': 'Timberwolves',
    'New Orleans Pelicans': 'Pelicans',
    'New Orleans': 'Pelicans',
    'Pelicans': 'Pelicans',
    'New York Knicks': 'Knicks',
    'New York': 'Knicks',
    'Knicks': 'Knicks',
    'Oklahoma City Thunder': 'Thunder',
    'Oklahoma City': 'Thunder',
    'Thunder': 'Thunder',
    'Orlando Magic': 'Magic',
    'Orlando': 'Magics',
    'Magic': 'Magic',
    'Philadelphia 76ers': '76ers',
    'Philadelphia': '76ers',
    '76ers': '76ers',
    'Pheonix Suns': 'Suns',
    'Pheonix': 'Suns',
    'Suns': 'Suns,
    'Portland Trail Blazers': 'Trail Blazers',
    'Portland': 'Trail Blazers',
    'Trail Blazers': 'Trail Blazers',
    'Sacramento Kings': 'Kings',
    'Sacramento': 'Kings',
    'Kings': 'Kings',
    'San Antonio Spurs': 'Spurs',
    'San Antonio': 'Spurs',
    'Spurs': 'Spurs',
    'Toronto Raptors': 'Raptors',
    'Toronto': 'Raptors',
    'Raptors': 'Raptors',
    'Utah Jazz': 'Jazz',
    'Utah': 'Jazz',
    'Jazz', 'Jazz',
    'Washington Wizards': 'Wizards',
    'Washington': 'Wizards',
    'Wizards': 'Wizards' 
  }
  # initialize the bot
  def __init__(self):
    #Initialize lakers bot
    super().__init__(default_state='waiting')
    
  # responses from the waiting state function
  def respond_from_waiting(self, message, tags):
    if 'Hello' in tags:
      return self.go_to_state('welcome')
    else:
      return self.finish('confused')
  
  # "specify_faculty" state functions
  
  def on_enter_welcome(self):
    return "Hey! I haven't seen you around before, are you a laker-head too?"
  
  # enter the conversation
  def respond_welcome(self, message, tags):
    if 'yes' in tags:
      return self.go_to_state('Lakers fan')
    elif 'no' in tags:
      return self.go_to_state('Lakers hater')
