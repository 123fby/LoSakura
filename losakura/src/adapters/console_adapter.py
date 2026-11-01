from loframework.internal.matcher import Matcher
from loframework.internal.adapter import Event


from loguru import logger

bot_name = Matcher.register_matcher("Lolo")
@Matcher.handle(bot_name)
async def handle_msg(matcher: Matcher, event:Event): 
    try:
        ai_chat=get_chat_flow()
        msg_info=event.to_dict()
        logger.info(msg_info)
        logger.info("洛洛要处理消息啦")
        ai_msg=await ai_chat.process_msg(msg_info)
        logger.info(f"AI response: {ai_msg}")
        if ai_msg:
            await matcher.send(ai_msg)
            logger.info(f"Sent response: {ai_msg}")
        else:
            await matcher.send("hello")
            logger.info("Sent hello message")
    except Exception as e:
        logger.error(f"Error in handle_msg: {str(e)}")
        await matcher.send(f"处理消息时出错: {str(e)}")
