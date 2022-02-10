# -*- coding: utf-8 -*-

# Module author @Azuremods

from .. import loader,utils
from time import sleep

@loader.tds
class HeartMod(loader.Module):
    """Heart module"""
    strings = {'name':'Heart:3'}
    
    async def luvcmd(self, message):
        """.luv Love you """
        lov_txt = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        if not lov_txt:
            if not reply:
                await utils.answer(message, "<b>.luv {your text}</b>")
                return
            else:
                lov_txt = reply.raw_text
        
        heart1 = "🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️🤍❤️❤️❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍"
        heart2 = "🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🧡🧡🤍🧡🧡🤍🤍\n🤍🧡🧡🧡🤍🧡🧡🧡🤍\n🤍🧡🧡🧡🧡🧡🧡🧡🤍\n🤍🧡🧡🧡🧡🧡🧡🧡🤍\n🤍🤍🧡🧡🧡🧡🧡🤍🤍\n🤍🤍🤍🧡🧡🧡🤍🤍🤍\n🤍🤍🤍🤍🧡🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍"
        heart3 = "🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💛💛🤍💛💛🤍🤍\n🤍💛💛💛🤍💛💛💛🤍\n🤍💛💛💛💛💛💛💛🤍\n🤍💛💛💛💛💛💛💛🤍\n🤍🤍💛💛💛💛💛🤍🤍\n🤍🤍🤍💛💛💛🤍🤍🤍\n🤍🤍🤍🤍💛🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍"
        heart4 = "🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💚💚🤍💚💚🤍🤍\n🤍💚💚💚🤍💚💚💚🤍\n🤍💚💚💚💚💚💚💚🤍\n🤍💚💚💚💚💚💚💚🤍\n🤍🤍💚💚💚💚💚🤍🤍\n🤍🤍🤍💚💚💚🤍🤍🤍\n🤍🤍🤍🤍💚🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍"
        heart5 = "🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💙💙🤍💙💙🤍🤍\n🤍💙💙💙🤍💙💙💙🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍🤍💙💙💙💙💙🤍🤍\n🤍🤍🤍💙💙💙🤍🤍🤍\n🤍🤍🤍🤍💙🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍"
        heart6 = "🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💜💜🤍💜💜🤍🤍\n🤍💜💜💜🤍💜💜💜🤍\n🤍💜💜💜💜💜💜💜🤍\n🤍💜💜💜💜💜💜💜🤍\n🤍🤍💜💜💜💜💜🤍🤍\n🤍🤍🤍💜💜💜🤍🤍🤍\n🤍🤍🤍🤍💜🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍"
        heart7 = "🤍🤍💜💜🤍💜💜🤍\n🤍💜💜💜🤍💜💜💜\n🤍💜💜💜💜💜💜💜\n🤍💜💜💜💜💜💜💜\n🤍🤍💜💜💜💜💜🤍\n🤍🤍🤍💜💜💜🤍🤍\n🤍🤍🤍🤍💜🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍"
        heart8 = "🤍💜💜💜🤍💜💜\n🤍💜💜💜💜💜💜\n🤍💜💜💜💜💜💜\n🤍🤍💜💜💜💜💜\n🤍🤍🤍💜💜💜🤍\n🤍🤍🤍🤍💜🤍🤍\n🤍🤍🤍🤍🤍🤍🤍"
        heart9 = "🤍💜💜💜💜💜\n🤍💜💜💜💜💜\n🤍🤍💜💜💜💜\n🤍🤍🤍💜💜💜\n🤍🤍🤍🤍💜🤍\n🤍🤍🤍🤍🤍🤍"
        heart10 = "🤍💜💜💜💜\n🤍🤍💜💜💜\n🤍🤍🤍💜💜\n🤍🤍🤍🤍💜\n🤍🤍🤍🤍🤍"
        heart11 = "🤍🤍💜💜\n🤍🤍🤍💜\n🤍🤍🤍🤍\n🤍🤍🤍🤍"
        heart12 = "🤍🤍🤍\n🤍🤍🤍\n🤍🤍🤍"
        heart13 = "🤍🤍\n🤍🤍"
        heart14 = "🤍"
        
        await utils.answer(message, heart1)
        sleep(0.3)
        await utils.answer(message, heart2)
        sleep(0.3)
        await utils.answer(message, heart3)
        sleep(0.3)
        await utils.answer(message, heart4)
        sleep(0.3)
        await utils.answer(message, heart5)
        sleep(0.3)
        await utils.answer(message, heart6)
        sleep(0.3)
        await utils.answer(message, heart7)
        sleep(0.3)
        await utils.answer(message, heart8)
        sleep(0.3)
        await utils.answer(message, heart9)
        sleep(0.3)
        await utils.answer(message, heart10)
        sleep(0.3)
        await utils.answer(message, heart11)
        sleep(0.3)
        await utils.answer(message, heart12)
        sleep(0.3)
        await utils.answer(message, heart13)
        sleep(0.3)
        await utils.answer(message, heart14)
