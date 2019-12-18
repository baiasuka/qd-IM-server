import asyncio
from core import ServerCore

app = ServerCore()

if __name__ == '__main__':
    asyncio.run(app.main())
