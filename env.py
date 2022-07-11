from pydantic import BaseSettings


class EnvSettings(BaseSettings):
    mongo_db_name: str
    mongo_db_username: str
    mongo_db_password: str
    mongo_db_host: str
    mongo_db_host_port: int

    class Config:
        env_file = ".env"


ENV = EnvSettings()
