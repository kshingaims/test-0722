from flask import Flask
from azure.storage.blob import BlobServiceClient  # 検証対象

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Azure App Service + Blob SDK!"

if __name__ == "__main__":
    app.run()