class Twitter:

    def __init__(self):
        self.timer = 0
        self.tweets = {}
        self.follows = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = [(-self.timer, tweetId)]
        else:
            self.tweets[userId].append((-self.timer, tweetId))
        self.timer += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        buf = []
        if userId in self.tweets:
            heap += self.tweets[userId][-10:]
        if userId in self.follows:
            for ffid in self.follows[userId]:
                if ffid in self.tweets:
                    heap += self.tweets[ffid][-10:]
        heapq.heapify(heap)

        while heap and len(buf)<10:
            buf.append(heapq.heappop(heap)[1])
        return buf

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            if followerId not in self.follows:
                self.follows[followerId] = set()
            self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows and followerId != followeeId:
            if followeeId in self.follows[followerId]:
                self.follows[followerId].remove(followeeId)
