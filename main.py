import discord
import os
import requests
from content import *
from keep_alive import keep_alive


client = discord.Client()
TOKEN = os.environ['TOKEN']


@client.event
async def on_ready():
    print(f"{client.user} has connected")
    print(f"{len(client.guilds)}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "!guilds" and str(message.author) == "anonymous_#0984":
        await message.reply(f"I am in {len(client.guilds)} {'server' if len(client.guilds) == 1 else 'servers'}")

    async def api2(ctx, w):
        response = requests.get(f"https://api.waifu.pics/{w}/{ctx}")
        url = response.json()["url"]
        await message.reply(url)

    async def api1(ctx, w):
        url = f"https://api.waifu.im/random/?selected_tags={ctx}"
        result = requests.get(url).json()["images"][0]["url"]
        print(result)
        await message.reply(result)

    async def nsfw():
        embed_ = discord.Embed(
            title="Set your channel to nsfw first ಥ_ಥ",
            description="Check your settings (^///^)",
        )
        embed_.set_image(url="https://i.imgur.com/oe4iK5i.gif")
        await message.reply(embed=embed_)

    msg = message.content.lower().split(" ")

    if msg[0] == "waifu":
        if msg[1] == "help":
            embed = discord.Embed(
                title="Waifu Commands",
            )
            embed.add_field(name="SFW Commands(Prefix= waifu)", value="""
            awoo
            bite
            blush
            bonk
            bully
            cringe
            cry
            cuddle
            dance
            glomp
            handhold 
            happy
            highfive
            hug
            kick
            kill
            kiss
            lick
            maid
            megumin
            neko
            nom
            pat
            poke
            shinobu
            slap
            smile
            smug
            waifu
            wave
            wink
            yeet""", inline=False)
            embed.add_field(name="NSFW Commands (Prefix= waifu nsfw)", value="""
            ass
            blowjob
            ecchi
            ero
            hentai
            maid
            milf
            neko 
            oppai
            oral
            paizuri
            selfies
            trap
            uniform""", inline=False)

            await message.reply(embed=embed)

        elif msg[1] == "nsfw":
            if message.channel.is_nsfw():
                if msg[2] in nsfwCommands_api1:
                    await api1(msg[2], "nsfw")

                elif msg[2] in nsfwCommands_api2:
                    await api2(msg[2], "nsfw")
            else:
                await nsfw()

        elif msg[1] != ("sfw" or "nsfw"):
            if msg[1] in sfwCommands_api2:
                await api2(msg[1], "sfw")

            elif msg[1] in sfwCommands_api1:
                await api1(msg[1], "sfw")


keep_alive()
client.run(TOKEN)
