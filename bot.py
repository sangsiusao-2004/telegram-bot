from telethon import TelegramClient, events

# ====== THÔNG TIN CỦA BẠN ======
api_id = 38104728
api_hash = '8b8de757cfa3856bbc9434f174fdabaf'

# ====== NGUỒN & ĐÍCH ======
source_chat = -1001562574961
target_chat = -1003981659447

# ====== KHỞI TẠO ======
client = TelegramClient('session', api_id, api_hash)

# ====== AUTO COPY ======
@client.on(events.NewMessage(chats=source_chat))
async def handler(event):
    try:
        # Nếu là text
        if event.message.media:
            await client.send_file(
                target_chat,
                event.message.media,
                caption=event.message.text or ""
            )
        else:
            await client.send_message(
                target_chat,
                event.message.text or ""
            )
    except Exception as e:
        print("Lỗi:", e)

# ====== CHẠY BOT ======
client.start()
print("Bot đang chạy...")
client.run_until_disconnected()