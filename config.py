import motor.motor_asyncio

MONGODB_URL = "mongodb://root:rootpassword@localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)

# connect to database python_db
database = client.python_db
