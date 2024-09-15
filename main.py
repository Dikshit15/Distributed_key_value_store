
class KeyValueStore:
    def __init__(self, store):
        self.store = store

    def put(self, key, value):
        self.store.update({key: value})

    def get(self, key):
        return self.store.get(key, None)


if __name__ == '__main__':
    # Creating an empty dictionary as the store
    store = KeyValueStore({})

    store.put('name', 'Alice')
    store.put('age', 30)

    print(store.get('name'))
    print(store.get('age'))
    print(store.get('gender'))
