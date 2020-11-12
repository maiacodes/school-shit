def loginPlayer(playerID):
    print(f"Player {playerID}, please login.")
    name = input("Name: ")
    pswd = input("Password: ")

    return authenticator(playerID, name, pswd)

def authenticator(pid, name, pswd):
    player = Player(pid, name)
    return True, player

class Player:
  def __init__(self, pid, name):
    self.id = pid
    self.name = name
    self.score = 0
  def addScore(self, score):
    self.score = self.score + score
    if (self.score % 2) == 0:
      self.score = self.score + 10
    else:
      if (self.score - 5) < 0:
        return
      self.score = self.score - 5