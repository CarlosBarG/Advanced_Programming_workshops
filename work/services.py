import uvicorn
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from fastapi import FastAPI
from typing import List
app = FastAPI()
##Creation of the postgres connection class
class PostgresConnection:
  def __init__(
        self, user: str, password: str, host: str, port: int, database_name: str
    ):  



    self.engine = create_engine('postgresql://postgres:postgres@localhost:5432/public')
    self.session = sessionmaker(bind=engine)
    self.session = Session()

metadata = MetaData()
products = Table('products', metadata,
                 Column('id', Integer, primary_key=True),
                 Column('name', String),
                 Column('description', String))

#Delete another fastapi app

@app.get("/hello_ud")
def hello_ud():
    return "Welcome to UD!"

@app.get("/products")
def get_products():
    query = products.select()
    result = session.execute(query)
    products = result.fetchall()
    return products


@app.post("/products")
def create_product(name: str, description: str):
    query = products.insert().values(name=name, description=description)
    session.execute(query)
    session.commit()
    return {"message": "Product created successfully"}
##Change the argument host by local host
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)