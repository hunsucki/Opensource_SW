#예제1

class MyCollection :
    def __getitem__(self, key):
        return f"Value for {key}"
    
collection = MyCollection()
print(collection.__getitem__(3))
print(collection[3])

