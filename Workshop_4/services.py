import uvicorn
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from fastapi import FastAPI
from typing import List

app = FastAPI()

##Creation of the database

DATABASE_URL = 'postgresql://postgres:postgres@localhost:5432/public'
engine = create_engine('postgresql://postgres:postgres@localhost:5432/public')
Session = sessionmaker(bind=engine)
session = Session()

metadata = MetaData()


products = Table('products', metadata,
                 Column('id', Integer, primary_key=True),
                 Column('name', String),
                 Column('description', String))



## Delete another fastapi app




@app.get("/hello_ud")
def hello_ud():
  """"This method return the message Welcome to Ud
  
  """
    return "Welcome to UD!"

@app.get("/products")
def get_products():
  """"This method return a product
  Args : Product
  Return: Product 
  """
    query = products.select()
    result = session.execute(query)
    product = result.fetchall()
##Change the name to product at the return
    return product

##Change name of the post to create_products
@app.post("/create_products")
def create_product(name: str, description: str):
    """This method is used to create a product
    Args: Name(str): Name of the product 
    Description(str): Description of the product

    Return:  Product
    """
    query = products.insert().values(name=name, description=description)
    session.execute(query)
    session.commit()
    return {"message": "Product created successfully"}
##Change the argument host by local host
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
