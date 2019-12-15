from sqlalchemy import create_engine
from sqlalchemy import *
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
import DatbaseInitialization, Insert
from datetime import datetime

engine = create_engine("sqlite:///db1.sqlite")
session = Session(bind=engine)



result = session.query(DatbaseInitialization.Customer).all()
for row in result:
   print ("Name: ",row.first_name," ",row.last_name, " Address:",row.address, " Email:",row.email)




result = session.query(DatbaseInitialization.Item).all()
for row in result:
   print ("Name: ",row.name," Cost Price:",row.cost_price, " Selling Price:",row.selling_price, " Quantity:",row.quantity)


result = session.query(DatbaseInitialization.Order).all()
for row in result:
   print ("ID: ",row.id," Date Placed:",row.date_placed, " Customer Id:",row.customer_id)



print(session.query(DatbaseInitialization.Customer))