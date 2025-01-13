import os
import sys
import asyncio
import logging

logging.basicConfig(level=logging.INFO)

if not os.path.exists('./data'):
    os.mkdir('./data')

from free_one_api.impls import app

def main():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    
    application = loop.run_until_complete(app.make_application("./data/config.yaml"))

    logging.getLogger().setLevel(application.logging_level)
    loop.run_until_complete(application.run())

if __name__ == "__main__":
    main()
