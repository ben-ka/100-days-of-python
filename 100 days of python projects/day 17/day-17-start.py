class User:
    def __init__(self,username,user_id) :
        self.username = username
        self.id = user_id
        self.followers = 0
        self.following = 0
    def add_follower(self, user_followed):
        self.following+=1
        user_followed.followers +=1
        


user1 = User("bennn","001")
user2 = User("tom","002")
user1.add_follower(user2)
print(user2.followers)