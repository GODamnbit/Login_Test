from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'

    phone = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(11), nullable=False)
    email = db.Column(db.String(50))
    password = db.Column(db.String(32), nullable=False)
    delete_type = db.Column(db.SmallInteger, nullable=False, default=0)
    sex = db.Column(db.Integer, nullable=False, default=0)
    head_img = db.Column(db.String(200))
    address = db.Column(db.String(100))
    born_date = db.Column(db.DateTime)
    longitude = db.Column(db.DECIMAL)
    latitude = db.Column(db.DECIMAL)
    production = db.Column(db.String(500))


class Admin(db.Model):
    __tablename__ = 'admin'

    phone = db.Column(db.Integer, db.ForeignKey('user.phone'))
    delete_type = db.Column(db.SmallInteger, nullable=False)


class Alembic_version(db.Model):
    __tablename__ = 'alembic_version'

    version_num = db.Column(db.String(32), primary_key=True)


class Bus(db.Model):
    __tablename__ = 'bus'

    bus_id = db.Column(db.Integer, primary_key=True)
    route_id = db.Column(db.Integer, db.ForeignKey('route.route_id'))
    phone = db.Column(db.Integer, db.ForeignKey('user.phone'))
    type_id = db.Column(db.Integer, nullable=False)
    delete_type = db.Column(db.SmallInteger, nullable=False, default=0)
    permit_passengers = db.Column(db.Integer, nullable=False)
    start_date = db.Column(db.DateTime)
    belong_company = db.Column(db.String(30))


class Bus_passenger(db.Model):
    __tablename__ = 'bus_passenger'

    bus_id = db.Column(db.Integer, db.ForeignKey('bus.bus_id'))
    passenger_id = db.Column(db.Integer, db.ForeignKey('passenger.passenger_id'))
    timestamp = db.Column(db.TIMESTAMP, nullable=False)


class Passenger(db.Model):
    __tablename__ = 'passenger'

    passenger_id = db.Column(db.Integer, primary_key=True)
    delete_type = db.Column(db.SmallInteger, nullable=False, default=0)
    sex = db.Column(db.Integer)
    age_level = db.Column(db.SmallInteger)
    is_glasses = db.Column(db.SmallInteger)
    is_hat = db.Column(db.SmallInteger)
    is_mask = db.Column(db.SmallInteger)
    is_lipstick =db.Column(db.SmallInteger)
    face_expression = db.Column(db.SmallInteger)
    future_matrix = db.Column(db.Text)


class Route(db.Model):
    __tablename__ = 'route'

    route_id = db.Column(db.Integer, primary_key=True)
    route_name = db.Column(db.String(20))


class Station(db.Model):
    __tablename__ = 'station'

    station_id = db.Column(db.Integer, primary_key=True)
    station_name = db.Column(db.String(20), nullable=False)
    delete_type = db.Column(db.SmallInteger, nullable=False, default=0)
    station_type = db.Column(db.SmallInteger, nullable=False)
    longitude = db.Column(db.DECIMAL)
    latitude = db.Column(db.DECIMAL)


class Station_passenger(db.Model):
    __tablename__ = 'station_passenger'

    station_id = db.Column(db.Integer, db.ForeignKey('station.station_id'))
    passenger_id = db.Column(db.Integer, db.ForeignKey('passenger.passenger_id'))
    timestamp = db.Column(db.TIMESTAMP, nullable=False)


class User_bus(db.Model):
    __tablename__ = 'user_bus'

    phone = db.Column(db.Integer, db.ForeignKey('user.phone'))
    bus_id = db.Column(db.Integer, db.ForeignKey('bus.bus_id'))
    timestamp = db.Column(db.TIMESTAMP, nullable=False)


class User_passenger(db.Model):
    __tablename__ = 'user_passenger'

    phone = db.Column(db.Integer, db.ForeignKey('user.phone'))
    passenger_id = db.Column(db.Integer, db.ForeignKey('passenger.passenger_id'))
    timestamp = db.Column(db.TIMESTAMP, nullable=False)


class User_station(db.Model):
    __tablename__ = 'user_station'

    phone = db.Column(db.Integer, db.ForeignKey('user.phone'))
    station_id = db.Column(db.Integer, db.ForeignKey('station.station_id'))
    timestamp = db.Column(db.TIMESTAMP, nullable=False)
