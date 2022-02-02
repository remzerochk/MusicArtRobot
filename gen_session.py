import asyncio
from pyrogram import Client as c

API_ID = input("\n15496152:\n > ")
API_HASH = input("\n6fc8da58e058f700fe4e81b9d15f0617:\n > ")

print("\n\n Enter Phone number when asked.\n\n")

i = c(":memory:", api_id=API_ID, api_hash=API_HASH)


async def main():
    await i.start()
    ss = await i.export_session_string()
    print("\nHERE IS YOUR STRING SESSION, COPY IT, DON'T SHARE!!\n")
    print(f"\n{ss}\n")


asyncio.run(main())
