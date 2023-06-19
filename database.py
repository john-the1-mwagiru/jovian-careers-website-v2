import sqlalchemy
from sqlalchemy import create_engine

engine = create_engine(
  "mysql+pymysql://yw4t6xhvqg7ai9rzj6a2:pscale_pw_sOYjiy3d7HUGgREXJzTtS7YeniLjx7U1yEWa9GGguAK@aws.connect.psdb.cloud/joviancareers?charset=utf8mb4",
  connect_args={"ssl": {
    "ssl_ca": "/etc/ssl/cert.pem",
  }})
