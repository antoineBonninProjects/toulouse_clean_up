# Toulouse Clean Up

## Synopsis

The objective of this project is to display in real time the latest value sent by an Arduino MKRFox1200 on the user's web browser.
This project features:

* **MKRFox1200 embedded code**
This is the embedded code on the Arduino MKRFox1200. It makes the Arduino send frames to the SigFox backend.
You will be given:
    - The code
    - A documentation of the Arduino code
    - A step by step explanation of how to register your device and create HTTP POST callbacks

* **Server code**
As I personnaly find python powerful and easy to use, I made the choice to use that language code my server.
Python code features:
    - SQLAlchemy ORM to easily interract with the SQLite database in which I store the SigFox device incoming data
    - Flask for implementing my HTTP REST services such as HTTP POST service to handle the SigFox backend callback reception and HTTP GET services to handle get requests from the client web application. Flask is also what I use to run the server.
    - Flask_socketio to implement websocket functionnalities for real time data update on the client side
    - A Sphinx generated documentation explaining the code, the requirements and how to run the server.

* **Client code**
The web aplication is codded using the Angular4 framework because I found a lot of tutorials and because it is easy to run with npm.
You can find on this repo:
    - The angular app code
    - A documentation explaining how to set everything up and serve the code


## Code Examples

### Arduino MKRFox1200

The SigFox library examples are really useful to get started with this Arduino board. Here are some links that explain some of the library examples:

https://www.arduino.cc/en/Tutorial/SigFoxFirstConfiguration
https://www.arduino.cc/en/Tutorial/SigFoxEventTrigger

### Server code

#### SQLAlchemy
Here are the main SQLAlchemy functionalities I use in my project so that you understand it when you read the code.

* **Create your database tables**

```Python
    from sqlalchemy import create_engine, Column, Integer, String
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy.ext.declarative import declarative_base
    import os

    # This is the base class for all your database tables
    Base = declarative_base()

    # This is the path to your database, replace with your location
    db_path = "sqlite:///"+os.path.join(os.path.dirname(__file__), 'memory.sqlite')

    # Starting point for your SQLAlchemy application
    engine = create_engine(db_path)

    # A class to interract with your database
    Session = sessionmaker(bind=engine)


    class SigFoxMessages(Base):
      """ Just a exemple of database table
      """

        __tablename__= "sigfox_messages"

        id = Column("id", Integer, primary_key=True)
        device_id = Column("device_id", String)
        seq_num = Column("seq#", Integer)
        weight = Column("weight", Integer)

        @property
        def serialize(self):
            """
            Do not forget this property if you want your table entries (lines)
            to be serializable (JSON format).
            """
            return {
                'id': self.id,
                'device_id': self.device_id,
                'seq_num': self.seq_num,
                'weight': self.weight
            }

    # This creates your newly defined database tables in your database
    Base.metadata.create_all(bind=engine)
```

* **Add data to your database**

```Python
  # Create a Session object to interract with your database
  db_session = Session()

  # Create the entry to append to your database table
  db_msg = SigFoxMessages()
  db_msg.device_id = json_msg["device_id"]
  db_msg.seq_num = json_msg["seq_num"]
  db_msg.weight = json_msg["weight"]

  # Add it to your database table
  db_session.add(db_msg)

  # Commit and Close the Session when you're done
  db_session.commit()
  db_session.close()
```

* **Read data from your database**

```Python
  # Create a Session object to interract with your database
  db_session = Session()

  # Make a query for all entries in the 'sigfox_messages' table
  # (represented by the SigFoxMessages class for SQLAlchemy ORM)
  qryresult = db_session.query(SigFoxMessages).all()

  # Make a query with a filter on a given condition: the device_id field of the entries must be '12' here.
  entries = db_session.query(SigFoxMessages).
                               filter(SigFoxMessages.device_id == 12).
                               all()
  # Make a query for one element in database. Fails if more
  # than one element is returned by the query.
  single_entry = db_session.query(SigFoxMessages).
                               filter(SigFoxMessages.device_id == 12).
                                one()

  # Make a query to know the number of entries that matches the condition device_id == 12
  entry_count = db_session.query(SigFoxMessages).
                               filter(SigFoxMessages.device_id == 12).
                               count()

  # Close the Session when you're done                              
  db_session.close()
```

More information can be found


#### Flask

#### Flask-socketio

## Motivation

A short description of the motivation behind the creation and maintenance of the project. This should explain **why** the project exists.

## Installation

Provide code examples and explanations of how to get the project.

## API Reference

Depending on the size of the project, if it is small and simple enough the reference docs can be added to the README. For medium size to larger projects it is important to at least provide a link to where the API reference docs live.


## License

A short snippet describing the license (MIT, Apache, etc.)
