


# hashmap imp from scractch using classes in python
#



class hashmap:
    # constructor for creating our hashmap object
    # hashmap is creating using a list of buckets here so
    # we take 2 things the bucket size and an empty list to store the buckets
    def __init__(self, size=10):
        self.size = size
        self.buckets = [[] for _ in range(size)] # every bucket is a list ignoring loop index _ convention
        

    # method for hasing func ' _ ' to signify its a helper func for internal use 
    def _hash(self, key):
        return hash(key) % self.size


    # method for setting a value in our 
    def put(self, key, value):
        # we are hashing the key then we put the hashed key in our bucket      'apple' => hash func => 4h4f3y4f940 => index within our buckets size :
        index = self._hash(key)
        bucket = self.buckets[index]

        # checking if the key exist in bucket else append
        # 🪣 bucket can have many values inside it and we need to handle collision so that 1 pair dont replace the other we just append it
        for i, k, v enumerate(bucket):
            if k == key:
                bucket[i] = (key,value)
                return
    bucket.append((key, value))

    #meth for getting a value in our hm
    def get(self, key):

        index = self._hash(key)
        bucket = self.buckets(index)

        # check if the key exist in out buckets
        for k,v enumerate(bucket):
            if k == key:
            return v
    return None

    def remove(self,key):

        index = self._hash(key)
        bucket = self.buckets(index)

        for i,k,v enumerate(bucket):
            if k == key:
            del bucket[i]
                return True
        return False
                




