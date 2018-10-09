import os
import glob
import importlib
import asyncio
from concurrent.futures import ThreadPoolExecutor
from AuthSync import EventLoop

pool = ThreadPoolExecutor(max_workers=5)


async def coro(task, timer):
    while EventLoop.is_running():
        await asyncio.wait(fs={EventLoop.run_in_executor(pool, task)}, return_when=asyncio.ALL_COMPLETED)
        await asyncio.sleep(timer)


def run():
    path = os.path.normpath(os.getcwd() + "/AuthSync/Tasks/*")
    import_files = glob.glob(path)
    for file in import_files:
        if not os.path.basename(file).startswith('__'):
            file = file.strip('.py').replace(os.path.normpath(os.getcwd()), '')
            file = file.replace("\\", "/").lstrip('/').split('/')

            pkg = ".".join(file)
            module = file[-1]
            imported = importlib.import_module(pkg)
            task = getattr(imported, module)
            if hasattr(imported, 'async_timer'):
                timer = getattr(imported, 'async_timer')
                if timer < 10:
                    timer = 10
            else:
                timer = 60
            EventLoop.create_task(coro(task, timer))

    EventLoop.run_forever()
