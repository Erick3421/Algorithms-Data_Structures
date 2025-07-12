class HashMap:
    def __init__(self, size=100) -> None:
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size
    
    def put(self, key,value):
        index = self._hash(key)
        bucket = self.buckets[index]

        for i, (k,v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key,value)
                return
            
        bucket.append([key, value])
    
    def get(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]

        for (k, v) in bucket:
            if k == key:
                return v
        return None

if __name__ == "__main__":
    mapa = HashMap()

    mapa.put("nome", "Erick")
    mapa.put("idade", 22)
    mapa.put("profissao", "Estagiário")

    print(mapa.get("nome"))       
    print(mapa.get("idade"))      
    print(mapa.get("profissao"))  
    print(mapa.get("cidade"))     