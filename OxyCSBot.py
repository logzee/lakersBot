from LakersChatBot import ChatBot


class LakersStan(ChatBot):

  STATES = [
    'waiting',
    'welcome',
    'confused',
    'Lakers_fan',
    'Lakers_Hater',
    'Basketball_fan',
    'question_section',
    'not_basketball_fan',
    'saw_the_last_game',
    'didnt_catch_the_last_game'
    'exiting_angry'
  ]
  
  TAGS = {
    # descriptors
    'like': 'like',
    'fan': 'like',
    'love' : 'like',
    'dont like': 'dislike',
    'dont' : 'dislike',
    'hate' : 'dislike',
    
    
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
    'nah': 'no',
    
    #basketball
    'basketball' : 'basketball'
    
    #memory
    'already' : 'again',
    'before' : 'again',
    'just' : 'again'
    #teams
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
    'Chicago': 'Bulls',
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
    'Rockets': 'Rockets',
    'Indiana Pacers': 'Pacers',
    'Indiana': 'Pacers',
    'Pacers': 'Pacers',
    'LA Clippers': 'Clippers',
    'LA': 'Clippers',
    'Clippers': 'Clippers',
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
    'Wizards': 'Wizards', 
    'Los Angeles Lakers' : 'Lakers',
    'Lakers' : 'Lakers'
  }
    
    
  TEAMS = {
    'Hawks',
    'Celtics',
    'Nets',
    'Hornets',
    'Bulls',
    'Cavaliers',
    'Mavericks',
    'Nuggets',
    'Pistons',
    'Warriors',
    'Rockets',
    'Pacers',
    'Clippers',
    'Grizzlier',
    'Heat',
    'Bucks',
    'Timberwolves',
    'Pelicans',
    'Knicks',
    'Thunder',
    'Magic',
    '76ers',
    'Suns',
    'Blazers',
    'Kings',
    'Spurs',
    'Raptors',
    'Jazz',
    'Wizards'
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
  
  # enter the welcome state state functions
  
  def on_enter_welcome(self):
    return "Hey! I haven't seen you around before, are you a laker-head too?"
  
  # enter the conversation: redirects to states based on the users feelings towards the Lakers
  def respond_welcome(self, message, tags):
    self.team = None
    if 'yes' in tags:
      return self.go_to_state('Lakers fan')
    elif 'no' in tags:
      for team in self.TEAMS:
        if team in tags:
          self.team = team
          return self.go_to_state('Lakers hater')
    return self.go_to_state('question section')
  
  # follow - up state if the user does not specify an alternate team they follow
  def on_enter_question_section(self):
    return " ".join(["Thats a shame :/ ...", 
                     "If ur not a lakers fan, what team do u follow?" ])
  
  # Identifies if they don't like the lakers or if they don't like basketball
  def respond_from_question_section(self, message, tags):
    self.team = None
    for team in self.TEAMS:
      if team in tags:
        self.team = team
        return self.go_to_state('Lakers hater')
    if 'dislike' in tags:
      if 'basketball' in tags:
        return self.go_to_state('not_basketball_fan')
    return self.go_to_state('confused')
  
  #response if they officially don't like the lakers but like another team
  def on_enter_Lakers_hater(self):
    respond " ".join([ "You're a", self.team.capitalize(), "fan?!",
                      "Im really trying to be nicer on the ol' web, after those punk ass mods banned me from r/NBA, but c'mon your a",
                      self.team, "fan!", "I honestly thought they got relegated to the B league after their last season"])
    
  # the bot exits in an angry fashion
  def respond_from_Lakers_hater(self):
    respond self.go_to_state('exiting_angry')
    
  # responds with angry exit message, moves back to waiting state
  def on_enter_exiting_angry(self):
    respond "Honestly can't even process what your saying right now. Not sure if its the 6 pack of coors im sipping on, or the concusion I got last week while playing at the rec center but im furious. I need to go cool off, I hope when Im back youve come to ur senses and support the lakers", self.go_to_state('waiting')
  
