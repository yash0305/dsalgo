# class hashing():
#     def __init__(self):
#         self.MAX = 100
#         self.arr  = [None for i in range(self.MAX)]

#     def get_hash(self,key):
#         hash = 0
#         for char in key:
#             hash = hash + ord(char)
#         return hash % self.MAX

#     def __setitem__(self,index,value):
#         h = self.get_hash(index)
#         self.arr[h] = value


#     def __getitem__(self,index):
#         h = self.get_hash(index)
#         return self.arr[h]


class hashing():
    def __init__(self):
        self.MAX = 10
        self.arr  = [[] for i in range(self.MAX)]

    def get_hash(self,key):
        hash = 0
        for char in key:
            hash = hash + ord(char)
        return hash % self.MAX

    def __setitem__(self,key,value):
        h = self.get_hash(key)
        found = False

        for idx, element in enumerate(self.arr[h]):
            print(f"idx -> {idx}    element -> {element}")
            if len(element) == 2 and element[0] == key:
                print(f"e   {element[0]}")
                self.arr[h][idx] = (key,value)
                found = True
                break
        if not found:
                self.arr[h].append((key,value))


    def __getitem__(self,key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def __delitem__(self,key):
        h = self.get_hash(key)
        for index ,element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]






h = hashing()
h.MAX = 10
# key = h.get_hash("yash")
h["march 6"] = 78
h["march 7"] = 79
h["march 8"] = 80
h["march 9"] = 234
h["march 10"] = 24
h["march 11"] = 8
h["march 12"] = 7
h["march 13"] = 74
h["march 14"] = 979
h["march 15"] = 889
h["march 16"] = 97
h["march 17"] = 9999
h["march 18"] = 889
h["march 19"] = 39
h["march 20"] = 38
h["march 21"] = 388
h["march 22"] = 90
h["march 23"] = 977
h["march 28"] = 77


h["march 17"] = 459

# print(h["march 6"])

# for a in h.arr:
#     print(a)

# print(key)
del h["march 10"]