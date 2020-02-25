import aiosqlite
from discord.ext import commands
bot = commands.Bot(command_prefix='?')


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')


@bot.command()
async def t(ctx, prefix):
    await bot.db.execute(
        f"UPDATE Guild SET Prefix=? WHERE GuildID=?", (prefix, ctx.message.guild.id))
    await bot.db.commit()
    await ctx.send("done")


class Fetch:
    def __init__(self, bot):
        self.bot = bot

    async def all(self, *arg):
        get = await self.bot.db.execute(*arg)
        results = await get.fetchall()
        return results

    async def one(self, *arg):
        get = await self.bot.db.execute(*arg)
        results = await get.fetchone()
        return results


async def create_dbconnect():
    bot.db = await aiosqlite.connect("test.db", check_same_thread=False)


bot.fetch = Fetch(bot)
bot.loop.create_task(create_dbconnect())

