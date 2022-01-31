import asyncio
from pyrogram import Client as c

API_ID = input("\n2497276:\n > ")
API_HASH = input("\n78122b16901bda6c500eebe931b31d42:\n > ")

print("\n\n Enter Phone number when asked.\n\n")

i = c(":memory:", api_id=API_ID, api_hash=API_HASH)


async def main():
    await i.start()
    ss = await i.export_session_string()
    print("\nHERE IS YOUR STRING SESSION, COPY IT, DON'T SHARE!!\n")
    print(f"\n{ss}\n")


asyncio.run(main())
