from app import db

class Category(db.EmbeddedDocument):
    verb = db.StringField()                    # e.g present
    verbOutcomePreposition = db.StringField()  # e.g as
    outcome = db.StringField()                 # e.g more masculine
    actionToolPreposition = db.StringField()   # e.g with
    tool = db.StringField()                    # e.g clothing

class User(db.Document):
    name = db.StringField()
    credentials = db.StringField()

class Star(db.EmbeddedDocument):
    user = db.ReferenceField(User)
    stars = db.IntField()

class Tip(db.Document):
    category = db.ReferenceField(Category)
    user = db.ReferenceField(User)
    ctime = db.DateTimeField()
    title = db.StringField()
    text_raw = db.StringField()
    text_rendered = db.StringField()
    stars = db.ListField(db.EmbeddedDocumentField(Star))

Category.register_delete_rule(Tip, 'category', db.CASCADE)
