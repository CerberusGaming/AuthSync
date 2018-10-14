from AuthSync.AuthSync import coro, EventLoop

from AuthSync.Joomla.Main import Joomla

Joomla = Joomla()


async def joomla_sync():
    while EventLoop.is_running():
        await coro(Joomla.sync, 60)


EventLoop.create_task(joomla_sync())
