from motor.motor_asyncio import AsyncIOMotorClient
uri = "mongodb://jesus_coronado:1234asdf@cluster0-shard-00-00.gujhw.mongodb.net:27017,cluster0-shard-00-01.gujhw.mongodb.net:27017,cluster0-shard-00-02.gujhw.mongodb.net:27017/?replicaSet=atlas-php85k-shard-0&ssl=true&authSource=admin&retryWrites=true&w=majority&appName=Cluster0"

MONGO_URI = "mongodb+srv://usuario:contraseña@cluster.mongodb.net/?retryWrites=true&w=majority"

client = AsyncIOMotorClient(MONGO_URI)
db = client["Prueba1"]
collection = db["archivos"]