from betterconf import betterconf, DotenvProvider

@betterconf(provider=DotenvProvider(auto_load=True))
class ApiConfig:
    api_id: int
    api_hash: str
