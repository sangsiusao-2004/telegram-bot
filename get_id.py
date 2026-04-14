from telethon import TelegramClient

api_id = 38104728
api_hash = '8b8de757cfa3856bbc9434f174fdabaf'

client = TelegramClient('session', api_id, api_hash)

async def main():
    print("===== DANH SÁCH CHAT =====")
    async for dialog in client.iter_dialogs():
        print(f"Tên: {dialog.name}")
        print(f"ID: {dialog.id}")
        print("------------------------")

with client:
    client.loop.run_until_complete(main())