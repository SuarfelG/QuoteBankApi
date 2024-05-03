from flask import Flask,  request
from flask_restful import Resource, Api ,abort
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema,fields

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quote.db'
db = SQLAlchemy(app)

api = Api(app)  

class QuoteBank(db.Model):
  __tablename__='quote_data'
  
  id=db.Column(db.Integer,primary_key=True)
  quote=db.Column(db.String(), nullable=False)
  author=db.Column(db.String(), nullable=False)

with app.app_context():
  db.create_all()

class QouteSchema(Schema):
    quote=fields.String()
    author=fields.String()
    

quote_schema=QouteSchema()



class QouteResource(Resource):
  def get(self,id):
    qouteData=QuoteBank.query.get(id)
    if qouteData:
      return quote_schema.dump(qouteData)
    else:
      abort(404 , message="Item Not Found")

  def put(self , id):
    data = request.form
    print(data)
    qouteData=quote_schema.load(data)
    if not qouteData:
      abort(500 , message='can not process request')
    else:
        newquote=QuoteBank(quote=qouteData['quote'],author=qouteData['author'])
        db.session.add(newquote)
        db.session.commit()
        return quote_schema.dump(newquote)
  

    
    

api.add_resource(QouteResource, '/quotes/<int:id>')  

if __name__=="__main__":
  app.run(debug=True)
