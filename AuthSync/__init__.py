import asyncio
from AuthSync.App.Config import Config

AppConfig = Config()
EventLoop = asyncio.get_event_loop()
