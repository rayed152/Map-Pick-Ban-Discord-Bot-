import discord
import os
from dotenv import main
import os
main.load_dotenv()



class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        # if message.content == '$hello':
        #     await message.channel.send('Hi')

        maps = ["Bind", "Accent", "Haven", "Pearl", "Ice-Box", "Fracture", "Breeze"]
        new_maps = "\n"''.join(maps)
        if message.content == '$Start':
            await message.channel.send(f"Maps Remaining, \n{new_maps}")
            await message.channel.send("Lets Start!")

        
        if message.content == "Bind":
            for item in maps: 
                if item == message.content:
                    maps.remove(item)
            new_maps = "\n"''.join(maps)
            await message.channel.send(f"{message.content} Have been removed.")
            new_maps = "\n"''.join(maps)
            await message.channel.send(f"Remaining Maps Are: \n{new_maps}")
        
        

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(os.environ['pass'])