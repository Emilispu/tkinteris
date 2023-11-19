# importing modules from packages
from sqlalchemy import *
from sqlalchemy.orm import relationship, declarative_base, sessionmaker
from datetime import *



# connect or create to db
engine = create_engine('sqlite:///users_and_messages.db', echo=True)
Base = declarative_base()
metadata = MetaData()

Session = sessionmaker(bind=engine)
session = Session()


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    user = Column('User_name', String, unique=True, nullable=False)
    passw = Column('Password', String, nullable=False)
    last_con = Column('Last time connect', String, default='None', nullable=True)
    status1 = Column(Integer, ForeignKey('status.id'))
    language = Column("Language", String, nullable=True)
    message = relationship('Messages')

    def __init__(self, user, passw, last_con):
        self.user = user
        self.passw = passw
        self.last_con = last_con

    def __repr__(self):
        return f"{self.id}, {self.user}, {self.passw}, {self.last_con}"


class User_status(Base):
    __tablename__ = 'status'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    user_stat =Column('Status', String, nullable=False)
    users = relationship('Users')

    def __init__(self, user_stat):
        self.user_stat = user_stat

    def __repr__(self):
        return f"{self.id}, {self.user_stat}"


class Messages (Base):
    __tablename__ = 'message'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String, ForeignKey('users.id'), nullable=False)
    message_text = Column('Message', String(500), nullable=False)
    atach = Column('Atached file', BLOB, nullable=True)
    mess_date = Column('Data of message', DateTime(), default=datetime.utcnow, nullable=True)
    mess_title_choise = Column('Theme of message', String, nullable=True)
    message_title = Column('Title of message', String, nullable=False)
    message_status = Column('Status of message', String, default='Sended', nullable=False)
    message_comment = Column('Message comments', String, nullable=True)

    def __init__(self, message_text, mes_title_choise, message_title, user_id):
        self.message_text = message_text
        self.date = date
        self.mess_title_choise = mes_title_choise
        self.message_title = message_title
        self.user_id = user_id

    def __repr__(self):
        return f"{self.id}, {self.user_id}, {self.message_text}, {self.message_title}, {self.mess_title_choise}, {self.mess_date}, {self.atach}"

Base.metadata.create_all(engine)

class Check_user_connection():
    """
​Ieškokite išsamios informacijos
384 / 5 000
Vertimo rezultatai
Vertimo rezultatas
The class is for checking if the user's login is correct.
Variables used in the class:
user_name
user_password
Everything must be of type String.

Functions:
def check_connection:
Verifying login. Value: True or False.
If False, it automatically redirects to the wich_Error function:
('no username' or 'invalid password' or 'invalid logins')
    """
    engine = create_engine('sqlite:///users_and_messages.db', echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    def __init__(self, user_name, user_password):
        self.user_name = user_name
        self.user_password = user_password

    def check_connection(self):
        try:
            for x in session.query(Users).filter_by(user=f"{self.user_name}").all():
                print(x.user, self.user_name, x.passw, self.user_password)
                if x.user == self.user_name and x.passw == self.user_password:
                    return True
                elif x.passw != self.user_password:
                    print('Password nor correct')
                else:
                    print('check user name and password. ')
        except: print('bad')

    def name(self):
        if self.check_connection(self):
            print(self.user_name)

    # ouruser = session.query(Users).filter_by(user='Emilis').first()
    # statusas = session.query(User_status).filter_by(user_stat='Not actyvated').all()
    # for x in statusas:
    #     ouruser.status1 = x.id
    def user_status(self):
        for x in session.query(Users).filter_by(user=f"{self.user_name}").all():
            x.last_con = datetime.utcnow()
            if x.status1 == 1:
                # x.status1 = 1
                return True

    def user_status2(self):
        for x in session.query(Users).filter_by(user=f"{self.user_name}").all():
            x.last_con = datetime.utcnow()
            if x.status1 == 1:
                x.status1 = 2
                session.commit()
                session.close()



    def __repr__(self):
        return self.check_connection()

# a = Check_user_connection('Emilis', 'Puidokas')
# print('****************', a.user_status(), '**************')

# ITRAUKTI TIESIOGIAI
# status1 = User_status(user_stat ='Not actyvated')
# status2 = User_status(user_stat ='Actyvated')
# status3 = User_status(user_stat ='Deactyvated')
# status4 = User_status(user_stat ='Blocked')
# session.add(status1)
# session.add(status2)
# session.add(status3)
# session.add(status4)

# ITRAUKTI PER SASAJA
# user1 = session.query(Users).filter_by(user='Emilis').all()
# for x in user1:
#     user_ids = x.id
#
# message1 = Messages(message_text='Laba vakara, vis dar vyksta testavimas', mes_title_choise='AS', message_title='Vakarėja', user_id=2)
#
# session.add(message1)
# user1 = session.query(Users).filter_by(user='Emilis').all()
# for x in user1:
#     user_ids = x.id
#
# message1 = Messages(message_text='Laba vakara, vis dar vyksta testavimas', mes_title_choise='AS', message_title='Vakarėja', user_id=2)
#
# session.add(message1)
#
# message1.user_id = int(user_ids)
#
# b = Users(user='Emilis', passw='Puidokas', last_con=f"{datetime.utcnow()}")
# session.add(b)
# session.query()
# User_statusas = session.get(Users, 1)
# User_statusas.status1 =

# ouruser = session.query(Users).filter_by(user='Emilis').first()
# statusas = session.query(User_status).filter_by(user_stat='Not actyvated').all()
# for x in statusas:
#     ouruser.status1 = x.id






session.commit()
session.close()