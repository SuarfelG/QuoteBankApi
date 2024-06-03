def get(self,id):
    qouteData=QuoteBank.query.get(id)
    if qouteData:
      return quote_schema.dump(qouteData)
    else:
      abort(404 , message="Item Not Found")