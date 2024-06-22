from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
from .classes.FeyzianMsg import FeyzianMsg
from telethon.sync import TelegramClient, events
from telethon.tl.types import Message, PeerChannel
from .models import Post
from dotenv import load_dotenv
import os
import asyncio
from telethon.errors import SessionPasswordNeededError

load_dotenv()

def home(request):
    symbols = User.objects.all()
    posts = Post.objects.all()
    print(symbols)
    return render(request, "home.html", {"symbols": symbols, "posts": posts})



async def get_user_posts_view(request):
    async with TelegramClient( os.getenv("username"), os.getenv("api_id"),  os.getenv("api_hash")) as client:

        async def handle_new_message(event):
            # try:
            await options[event.message.peer_id.channel_id](event.message)

            # except:
            #     print("An exception occurred")

        # async def handle_message_edit(event):
            # try:
            #     msg = event.message
            #     post = await sync_to_async(PostInitial.objects.get)(message_id=msg.id)
            #     post.edit_date = msg.date.strftime("%Y-%m-%d %H:%M:%S")
            #     post.message = msg.message
            #     if msg.reply_to:
            #         post.reply_to_msg_id = msg.reply_to.reply_to_msg_id
            #     else:
            #         post.reply_to_msg_id = None

            #     await sync_to_async(post.save)()
            # except:
            #     print("An exception occurred")

        client.add_event_handler(
            handle_new_message,
            events.NewMessage(
                chats=[
                    PeerChannel(int( os.getenv("CHANNEL_FEYZ"))),
                    PeerChannel(int( os.getenv("CHANNEL_TEST_FEYZIAN"))),

                    # PeerChannel(int(config["CHANNEL_ALI_BEY"])),
                    # PeerChannel(int(config["CHANNEL_TEST_ALI_BEYRANVAND"])),

                    # PeerChannel(int(config["CHANNEL_BINANCE_PRO"])),
                    # PeerChannel(int(config["CHANNEL_TEST_BINANCE_PRO"])),

                    # PeerChannel(int(config["CHANNEL_RASTAD"])),
                    # PeerChannel(int(config["CHANNEL_TEST_RASTAD"])),
                ]
            ),
        )
        # client.add_event_handler(
        #     handle_message_edit,
        #     events.MessageEdited(
        #         chats=[
        #             PeerChannel(int(config["CHANNEL_FEYZ"])),
        #             PeerChannel(int(config["CHANNEL_TEST_FEYZIAN"])),

        #             PeerChannel(int(config["CHANNEL_ALI_BEY"])),
        #             PeerChannel(int(config["CHANNEL_TEST_ALI_BEYRANVAND"])),
        
        #             PeerChannel(int(config["CHANNEL_BINANCE_PRO"])),
        #             PeerChannel(int(config["CHANNEL_TEST_BINANCE_PRO"])),
        #         ]
        #     ),
        # )
        await client.run_until_disconnected()
    # await client.disconnect()
    # return JsonResponse({"posts": []})

async def channelTestFeyzian(msg):
    p1 = FeyzianMsg()
    await p1.extract_data_from_message(msg)
    


options = {
    int( os.getenv("CHANNEL_FEYZ")): channelTestFeyzian,
    int( os.getenv("CHANNEL_TEST_FEYZIAN")): channelTestFeyzian,

    # int(config["CHANNEL_ALI_BEY"]): channelTestAliBeyro,
    # int(config["CHANNEL_TEST_ALI_BEYRANVAND"]): channelTestAliBeyro,

    # int(config["CHANNEL_BINANCE_PRO"]): channelTestBinancePro,
    # int(config["CHANNEL_TEST_BINANCE_PRO"]): channelTestBinancePro,

    # int(config["CHANNEL_RASTAD"]): channelTestRastad,
    # int(config["CHANNEL_TEST_RASTAD"]): channelTestRastad,

}


async def set_phone_number(phone_number,token):

    print(1)
    client = TelegramClient( os.getenv("username"), os.getenv("api_id"),  os.getenv("api_hash"))
    print(2)
    # await client.start()
    await client.connect()
    print( client._phone_code_hash)
    print(3)
    # Ensure you're authorized
    if not await client.is_user_authorized():
        print(4)
        if not token:
            await client.send_code_request(phone_number)
            print(phone_number)
            print(5)
        elif token:
            print(6)
            try:
                print(7)
                await client.send_code_request(phone_number)
                await client.sign_in(phone_number,token)
                print(8)
            except SessionPasswordNeededError:
                await client.sign_in(password=input('Password: '))
                
            print(9)
    print(10)
            
    # me = await client.get_me()

def getPhoneNumberAndCode(request):
    phone_number_param = request.POST.get("phone_number")
    token_param = request.POST.get("token")
    
    if phone_number_param:
        print(11)
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(set_phone_number(phone_number_param,token_param))
    return render(request, "test.html", {"phone_number": phone_number_param})