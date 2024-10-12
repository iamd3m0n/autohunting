from telethon.sync import TelegramClient, events
import asyncio

async def send_hunt(client):
    count = 0
    while count < 10000:
        try:
            await client.send_message('@HeXamonbot', '/hunt')  # Replace with the target chat or user
            await asyncio.sleep(5)  # Wait for 5 seconds between messages
            count += 1
        except Exception as e:
            print(f"An error occurred: {e}")
            await asyncio.sleep(60)  # Wait for 60 seconds before retrying

@events.register(events.NewMessage)
async def stop_on_message(event):
    if '✨ Shiny pokemon found!' in event.message.message:
        print('Stopping hunt!')
        await event.client.disconnect()

async def main():
    api_id = 2205928  # Replace with your Telegram API ID
    api_hash = 'f099460ec6cdbe6c1dfdaabf701020b5'  # Replace with your Telegram API hash
    session_name = 'autohunting_session'  # Desired session name
    client = TelegramClient(session_name, api_id, api_hash)

    try:
        await client.start()
        await send_hunt(client)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if client.is_connected():
            await client.disconnect()

if __name__ == '__main__':
    asyncio.run(main())
