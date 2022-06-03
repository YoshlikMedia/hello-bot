from dataclasses import dataclass

from environs import Env


@dataclass
class DbConfig:
    host: str
    password: str
    user: str
    database: str


@dataclass
class TgBot:
    token: str
    admin_ids: list[int]
    use_mongo: bool
    webhook: bool
    webhook_url: str


@dataclass
class Miscellaneous:
    other_params: str = None


@dataclass
class Config:
    tg_bot: TgBot
    db: DbConfig
    misc: Miscellaneous


def load_config(path: str = None):
    env = Env()
    env.read_env(path)

    return Config(
        tg_bot=TgBot(
            token=env.str("BOT_TOKEN"),
            admin_ids=list(map(int, env.list("ADMINS"))),
            use_mongo=env.bool("USE_MONGO", default=False),
            webhook=env.bool("USE_WEBHOOK", default=False),
            webhook_url=env.str("WEBHOOK_URL", default=""),
        ),
        db=DbConfig(
            host=env.str('DB_HOST', default='localhost'),
            password=env.str('DB_PASS', default=''),
            user=env.str('DB_USER', default='root'),
            database=env.str('DB_NAME', default='tgbot'),
        ),
        misc=Miscellaneous()
    )
