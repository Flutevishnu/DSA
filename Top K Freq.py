def topKFrequent(nums, k):
        
        count = {}
        result = [[] for i in range(len(nums))]
        res = []
        for i in nums:
            count[i] = 1+ count.get(i, 0)
        print(count)

        for key, val in count.items():
            result[val].append(key)

        for i in range(len(result)-1, 0, -1):
            for n in result[i]:
                res.append(n)
        print(res)
topKFrequent([1,1,1,2,2,3], 2)