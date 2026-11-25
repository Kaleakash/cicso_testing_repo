class Database:
    def __new__(cls):    
                print("Creating database object")
                return super().__new__(cls)
    def connect(self):
        print("Database connected")


# Creating objects
db1 = Database()    # different objects
db2 = Database()    # different objects
db3 = Database()    # different objects
db4 = db3           # same object with two reference. 
db1.connect()
db2.connect()
db3.connect()

# Check object identity
print(db1 is db2)
print(db2 is db3)
print(db3 is db4)