import pyrebase

class validation:

    def __init__(self):

        self.config_os = {
            "databaseURL": "https://teste-98a84-default-rtdb.firebaseio.com/wmotos",
            "apiKey": "AIzaSyChC-2pPOHpGbB6QyddsfOwDN5Z-q3M3Pw",
            "authDomain": "teste-98a84.firebaseapp.com",
            "databaseURL": "https://teste-98a84-default-rtdb.firebaseio.com",
            "projectId": "teste-98a84",
            "storageBucket": "teste-98a84.appspot.com",
            "messagingSenderId": "682907299643",
            "appId": "1:682907299643:web:3a0023d2636fd84678911e",
            "measurementId": "G-1ZBQV3V06H"
        }

        firebase = pyrebase.initialize_app(self.config_os)
        self.db = firebase.database()

    def getStatus(self):
        #RETORNA O STATUS
        return self.db.get().each()[0].val()