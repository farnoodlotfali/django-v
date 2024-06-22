from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
from .classes.FeyzianMsg import FeyzianMsg
from dotenv import dotenv_values
from telethon.sync import TelegramClient, events
from telethon.tl.types import Message, PeerChannel
from .models import Post

config = dotenv_values(".env")

api_id = config["api_id"]
api_hash = config["api_hash"]

username = config["username"]

def home(request):
    symbols = User.objects.all()
    posts = Post.objects.all()
    print(symbols)
    return render(request, "home.html", {"symbols": symbols, "posts": posts})



async def get_user_posts_view(request):
    async with TelegramClient(username, api_id, api_hash) as client:

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
                    PeerChannel(int(config["CHANNEL_FEYZ"])),
                    PeerChannel(int(config["CHANNEL_TEST_FEYZIAN"])),

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
    int(config["CHANNEL_FEYZ"]): channelTestFeyzian,
    int(config["CHANNEL_TEST_FEYZIAN"]): channelTestFeyzian,

    # int(config["CHANNEL_ALI_BEY"]): channelTestAliBeyro,
    # int(config["CHANNEL_TEST_ALI_BEYRANVAND"]): channelTestAliBeyro,

    # int(config["CHANNEL_BINANCE_PRO"]): channelTestBinancePro,
    # int(config["CHANNEL_TEST_BINANCE_PRO"]): channelTestBinancePro,

    # int(config["CHANNEL_RASTAD"]): channelTestRastad,
    # int(config["CHANNEL_TEST_RASTAD"]): channelTestRastad,

}
