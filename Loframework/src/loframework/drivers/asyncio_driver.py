import asyncio
from typing import override
from loguru import logger
from loframework.drivers import Driver, Adapter


class AsyncioDriver(Driver):
    def __init__(self,ADAPTERS:dict[str,Adapter]):
        self._shutdown_event = asyncio.Event()
        self.ADAPTERS = ADAPTERS
        self.adapter_lists:list[str] = list(self.ADAPTERS.keys())
        self.adapters:dict[str,Adapter] = {}
    def __str__(self):
        return f"AsyncioDriver"
    @override
    def run(self):
        """ 启动驱动 (接口)"""
        asyncio.run(self._run())

    async def _run(self):
        print(self.adapter_lists[0])
        await self.start()
        await self.lifespan_start()
        await self.adapters[self.adapter_lists[0]].run()
        try:
            logger.info("准备关闭driver")
        except asyncio.CancelledError:
           print("Shutting down...")
        except KeyboardInterrupt:
            print("KeyboardInterrupt")
        finally:
            await self.lifespan_stop()
            await self.stop()
    @override
    def get_driver(self):
        return self

    async def start(self):
        """启动并初始化适配器"""
        print("Starting...")
        self.load_adapter(self.adapter_lists[0])

    async def stop(self):
        print("Stopping...")
    #等待后续完善
    # async def _wait_shutdown(self):
    #     await self._shutdown_event.wait()
        

    # def shutdown(self):
    #     self._shutdown_event.set()

    @override
    def load_adapter(self, adapter_name:str):
        if adapter_name not in self.adapter_lists:
            raise ValueError(f"Adapter {adapter_name} not found")
        adapter = self.ADAPTERS[adapter_name]()
        print(f"Loading adapter {adapter_name}...")
        self.adapters[adapter_name] = adapter
    def register_adapter(self, *adapter:str):
        for adapter_name in adapter:
            if adapter_name not in self.adapter_lists:
                self.adapter_lists.append(adapter_name)
            else:
                print(f"Adapter {adapter_name} already registered")