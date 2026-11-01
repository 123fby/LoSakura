from losakura.src.logic.chat_flow import ChatFlow
import loframework 

if __name__ == '__main__':
    driver = loframework.load_driver("asyncio")
    driver.lifespan_register(ChatFlow)
    loframework.run(driver)
    