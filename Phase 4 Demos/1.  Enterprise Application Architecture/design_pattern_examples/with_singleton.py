class Database:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            print("Creating database object")
            cls._instance = super().__new__(cls)
        return cls._instance

    def connect(self):
        print("Database connected")


# Creating objects
db1 = Database()
db2 = Database()
db3 = Database()

db1.connect()
db2.connect()
db3.connect()

# Check object identity
print(db1 is db2)
print(db2 is db3)
print(db1 is db3)