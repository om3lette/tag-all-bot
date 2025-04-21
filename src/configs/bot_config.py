from betterconf import betterconf, DotenvProvider, field

@betterconf(provider=DotenvProvider(auto_load=True))
class BotConfig:
    bot_token: str
    bot_username: str = field(default="tag_all")
