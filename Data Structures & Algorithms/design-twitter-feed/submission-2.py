class Twitter:

    def __init__(self):
        self.user = []
        self.tweets = []
        self.npost = 0
        self.follows = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user.append(userId)
        self.tweets.append(tweetId)
        if userId not in self.follows:
            self.follows[userId] = {userId}
        self.npost += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        buf = []
        count = 0
        for ii in range(self.npost-1,-1,-1):
            if userId not in self.follows:
                break
            if self.user[ii] in self.follows[userId]:
                buf.append(self.tweets[ii])
                count += 1
            if count == 10:
                break
        return buf

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            self.follows[followerId] = {followerId}
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows and followerId != followeeId:
            if followeeId in self.follows[followerId]:
                self.follows[followerId].remove(followeeId)
