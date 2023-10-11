from peewee import *

db = SqliteDatabase('hub.db')

class Device(Model):
    name = CharField()
    mac = CharField()
    state = BooleanField()
    lastOnline = DateTimeField()

    def toJson(self):
        return { "name" : self.name,
                 "mac": self.mac,
                 "state" : self.state,
                 "lastOnline" : str(self.lastOnline)}

    class Meta:
        database = db # This model uses the "people.db" database.

def connect():
    global db

    db.connect()
    db.create_tables( [Device] )

    # make sure state starts offline
    for device in Device.select():
        device.state = False
        device.save()

def close():
    global db

    db.close()