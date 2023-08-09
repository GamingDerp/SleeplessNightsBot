import discord
from discord.ext import commands
from datetime import datetime, timedelta
import time
import asyncio
import aiosqlite
        
# Misc Commands Class
class MiscCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    # Creating table on startup   
    @commands.Cog.listener()
    async def on_ready(self):
        await self.create_table()
    
    # Creates database table on startup
    async def create_table(self):
        async with aiosqlite.connect("dbs/todo.db") as db:
            await db.execute('''
                CREATE TABLE IF NOT EXISTS todos (
                    user_id INTEGER, 
                    todo TEXT
                )
            ''')
            await db.commit()
    
    # WhoIs Command
    @commands.command(aliases=["siohw", "Whois", "siohW", "WHOIS", "SIOHW"])
    async def whois(self, ctx, user:discord.Member):
        e = discord.Embed(color=0xc700ff)
        e.set_author(name=f"Gathering Information..."),
        if user.avatar:
            e.set_thumbnail(url=user.avatar.url)
        e.add_field(name="📍 Mention", value=user.mention)
        e.add_field(name="🔖 ID", value=user.id)
        e.add_field(name="📑 Nickname", value=user.display_name)
        e.add_field(name="📅 Created On", value=user.created_at.strftime("`%B %d, %Y %H:%M %p`"))
        e.add_field(name="📅 Joined On", value=user.joined_at.strftime("`%B %d, %Y %H:%M %p`"))
        if user.premium_since:
            e.add_field(name=f"<a:DiscordBoost:1121298549657829436> Boosting", value=user.premium_since.strftime("`%B %d, %Y %H:%M %p`"))
        e.add_field(name="👑 Top Role", value=user.top_role.mention)
        e.add_field(name="🎲 Activity", value=f"{user.activity.name}" if user.activity is not None else None)
        e.add_field(name="🚦 Status", value=user.status)
        emotes = {
            "hypesquad_brilliance": "<:HypeSquadBrilliance:1123772502024405053>",
            "hypesquad_bravery": "<:HypeSquadBravery:1123772444994437240>",
            "hypesquad_balance": "<:HypeSquadBalance:1123772443069259897>",
            "bug_hunter": "<:BugHunter:1123772432679981057>",
            "bug_hunter_level_2": "<:BugHunterLevel2:1123772435150422086>",
            "early_verified_bot_developer": "<:EarlyVerifiedBotDeveloper:1123772440338776064>",
            "verified_bot_developer": "<:EarlyVerifiedBotDeveloper:1123772440338776064>",
            "active_developer": "<:ActiveDeveloper:1123772429307744287>",
            "hypesquad": "<:HypeSquadEvents:1123772447125155963>",
            "early_supporter": "<:EarlySupporter:1123772438380019762>",
            "discord_certified_moderator": "<:ModeratorProgramsAlumni:1123772518365409370>",
            "staff": "<:Staff:1123772450430267393>",
            "partner": "<:Partner:1123774032932769812>",
        }
        badges = [
            emoji
            for f in user.public_flags.all()
            if (emoji := emotes.get(f.name))
        ]
        if badges:
            e.add_field(name="🧬 Flags", value=" ".join(badges))
        else:
            e.add_field(name="🧬 Flags", value="None")
        e.add_field(name="🤖 Bot?", value=user.bot)
        if user.status != user.mobile_status:
            e.add_field(name="📺 Device", value="Desktop")
        elif user.status != user.desktop_status:
            e.add_field(name="📺 Device", value="Mobile")
        req = await self.bot.http.request(discord.http.Route("GET", "/users/{uid}", uid=user.id))
        banner_id = req["banner"]
        if banner_id:
            banner_url = f"https://cdn.discordapp.com/banners/{user.id}/{banner_id}?size=1024"
            e.add_field(name="📰 Banner", value="**Linked Below**")
            e.set_image(url=banner_url)
        else:
            e.add_field(name="📰 Banner", value="None")
        e.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url),
        e.timestamp = datetime.utcnow()
        await ctx.send(embed=e)

    # Snipe Events
    sniped_message = None
    
    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.author.bot:
            return
        global sniped_message
        sniped_message = message
        
    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if before.author.bot: 
            return
        global sniped_message
        sniped_message = before
        
    # Snipe Command
    @commands.command(aliases=["epins", "Snipe", "epinS", "SNIPE", "EPINS"])
    async def snipe(self, ctx):
        global sniped_message
        if sniped_message is None:
            await ctx.send("There are no recently deleted messages to snipe.")
            return
        if sniped_message.content:
            e = discord.Embed(color=0xc700ff)
            e.set_author(name=sniped_message.author.name, icon_url=sniped_message.author.avatar.url)
            e.description = f"> {sniped_message.content}"
            await ctx.send(embed=e)
        elif sniped_message.attachments:
            attachment_url = sniped_message.attachments[0].url
            e = discord.Embed(color=0xc700ff)
            e.set_author(name=sniped_message.author.name, icon_url=sniped_message.author.avatar.url)
            e.set_image(url=attachment_url)
            await ctx.send(embed=e)
        sniped_message = None  # Reset sniped message after displaying
        
    # Deathnote Help Command
    @commands.command(aliases=["plehhtaed", "Deathhelp", "plehhtaeD", "DEATHNOTEHELP", "PLEHHTAED"])
    async def deathhelp(self, ctx):
        e = discord.Embed(color=0xc700ff)
        e.set_author(name="☠️ Available Death Methods ☠️")
        e.add_field(
            name="__Death Options__",
            value=f"\n> 🗻 Cliff"
                  f"\n> 🚝 Train"
                  f"\n> 🏊🏼 Drown"
                  f"\n> 🗿 Crush"
                  f"\n> 🌭 Choke"
                  f"\n> 🚗 Car Crash"
                  f"\n> 🔪 Murder"
                  f"\n> ⚡️ Shock"
                  f"\n> 🔥 Fire"
                  f"\n> 💥 Explosion"
                  f"\n> 🌩 Lightning"
                  f"\n> 🌋 Volcano"
                  f"\n> 🌪 Tornado"
                  f"\n> 🧱 Earthquake"
                  f"\n> 🌊 Hurricane",
        )
        e.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url),
        e.timestamp = datetime.utcnow()
        await ctx.send(embed=e)

    # Pickle Rick Command
    @commands.hybrid_command(name="pickle", description="Sends pickle rick")
    async def pickle(self, ctx):
            await ctx.send("I'M PICCKLLE RIIIIIICCCKKKK 🥒")
        
    # Remind Command
    @commands.command(aliases=["dnimer", "Remind", "dnimeR", "REMIND", "DNIMER"])
    async def remind(self, ctx, time, *, task):
        def convert(time):
            pos = ['s', 'm', 'h', 'd']
            time_dict = {"s": 1, "m": 60, "h": 3600, "d": 3600*24}
            unit = time[-1]
            if unit not in pos:
                return -1
            try:
                val = int(time[:-1])
            except:
                return -2
            return val * time_dict[unit]
        converted_time = convert(time)
        if converted_time == -1:
            await ctx.send("You didn't input the time correctly!")
            return
        if converted_time == -2:
            await ctx.send("The time must be an integer!")
            return
        
        # Timer Embed
        e = discord.Embed(color=0xc700ff)
        e.description = "⏰ Started Reminder ⏰"
        e.add_field(name="Time", value=time)
        e.add_field(name="Task", value=task)
        e.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        e.timestamp = datetime.utcnow()
        await ctx.send(embed=e)
        
        # End Timer Embed
        await asyncio.sleep(converted_time)
        await ctx.send(ctx.author.mention)
        e = discord.Embed(color=0xc700ff)
        e.description = "⏰ Time's Up ⏰"
        e.add_field(name="Task", value=task)
        await ctx.send(embed=e)
        
    # Todo Add Command
    @commands.command(aliases=["ddadt", "Tdadd", "ddadT", "TDADD", "DDADT"])
    async def tdadd(self, ctx, *, text):
        author_id = ctx.author.id
        async with aiosqlite.connect("dbs/todo.db") as db:
            await db.execute("INSERT INTO todos (user_id, todo) VALUES (?, ?)", (author_id, text))
            await db.commit()
        await ctx.send(f"Added **{text}** to your todo list!")
    
    # ToDo Del Command
    @commands.command(aliases=["leddt", "Tddel", "leddT", "TDDEL", "LEDDT"])
    async def tddel(self, ctx, todo_num: int):
        author_id = ctx.author.id
        async with aiosqlite.connect("dbs/todo.db") as db:
            cursor = await db.execute("SELECT rowid, todo FROM todos WHERE user_id = ?", (author_id,))
            rows = await cursor.fetchall()
            if todo_num <= 0 or todo_num > len(rows):
                await ctx.send("Invalid todo number!")
                return
            todo_id, todo_text = rows[todo_num - 1]
            await db.execute("DELETE FROM todos WHERE rowid = ?", (todo_id,))
            await db.commit()
        await ctx.send(f"Removed **{todo_text}** from your todo list!")
    
    # ToDo List Command
    @commands.command(aliases=["tsildt", "Tdlist", "tsildT", "TDLIST", "TSILDT"])
    async def tdlist(self, ctx, user: discord.User = None):
        if user is None:
            user = ctx.author
        async with aiosqlite.connect("dbs/todo.db") as db:
            cursor = await db.execute("SELECT todo FROM todos WHERE user_id = ?", (user.id,))
            todos = await cursor.fetchall()
        if not todos:
            await ctx.send(f"**{user.name}** has no items in their todo list!")
        else:
            todo_list = "\n".join([f"**{idx + 1})** {todo[0]}" for idx, todo in enumerate(todos)])
            e = discord.Embed(color=0xc700ff)
            e.set_author(name=f"{user.name}'s Todo List", icon_url=user.avatar.url)
            e.description=todo_list
        await ctx.send(embed=e)

    
async def setup(bot):
    await bot.add_cog(MiscCog(bot))
