from config.database import Base, DBConnection

with DBConnection() as conn:
    Base.metadata.create_all(conn.create_engine())