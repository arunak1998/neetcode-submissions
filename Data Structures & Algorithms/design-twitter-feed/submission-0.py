class Twitter:

    def __init__(self):
        self.count=0

        self.followmap=defaultdict(set)
        self.tweetmap=defaultdict(list)
        

    def postTweet(self, userId: int, tweetId: int) -> None:

        self.tweetmap[userId].append([self.count,tweetId])
        self.count-=1




        

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        result = []

        users = self.followmap[userId] | {userId}

        for followeeId in users:

            if self.tweetmap[followeeId]:

                index = len(self.tweetmap[followeeId]) - 1

                time, tweetId = self.tweetmap[followeeId][index]

                heapq.heappush(
                    heap,
                    [time, tweetId, followeeId, index]
                )
        while heap and len(result) < 10:

            count, tweetId, followeeId, index = heapq.heappop(heap)


            result.append(tweetId)


            index -= 1


            if index >= 0:
                count, tweetId = self.tweetmap[followeeId][index]

                heapq.heappush(
                    heap,
                    [count, tweetId, followeeId, index]
                )
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
       self.followmap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followmap[followerId]:
            self.followmap[followerId].remove(followeeId)



