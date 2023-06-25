import discord
from discord.ext import commands
import random

owner_id = 532706491438727169
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)
###################################[ ACTION CLASS ]###################################
# Action Commands Class
class Action(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Bonk Command
    @commands.command(aliases=["knob", "Bonk", "knoB"])
    async def bonk(self, ctx, user:discord.Member):
        e = discord.Embed(color=0xc700ff)
        e.description = f"{ctx.author.mention} bonks {user.mention}!"
        e.set_image(url="https://media.discordapp.net/attachments/807071768258805764/1109240042238513233/BonkGif.gif"),
        await ctx.send(embed=e)

    # Slap Command
    @commands.command(aliases=["pals", "Slap", "palS"])
    async def slap(self, ctx, user:discord.Member):
        e = discord.Embed(color=0xc700ff)
        e.description = f"{ctx.author.mention} slaps {user.mention}!"
        e.set_image(url="https://media.discordapp.net/attachments/807071768258805764/1106847432907685928/AnimeSlappingGif.gif"),
        await ctx.send(embed=e)

    # Throw Command
    @commands.command(aliases=["worht", "Throw", "worhT"])
    async def throw(self,ctx,user:discord.Member):
        e = discord.Embed(color=0xc700ff)
        e.description = f"{ctx.author.mention} throws {user.mention} off a cliff!"
        e.set_image(url="https://media.discordapp.net/attachments/807071768258805764/1116579751897878558/ThrowGif.gif"),
        await ctx.send(embed=e)

    # Kidnap Command
    @commands.command(aliases=["pandik", "Kidnap", "pandiK"])
    async def kidnap(self, ctx, user:discord.Member):
        e = discord.Embed(color=0xc700ff)
        e.description = f"{ctx.author.mention} kidnaps {user.mention}!"
        e.set_image(url="https://media.discordapp.net/attachments/807071768258805764/1107074673361047673/AnimeKidnapGif.gif"),
        await ctx.send(embed=e)

    # Strangle Command
    @commands.command(aliases=["elgnarts", "Strangle", "elgnartS"])
    async def strangle(self, ctx, user:discord.Member):
        strangle_response = ["they crush their windpipes, killing them! RIP ☠️", f"causes them to faint!", f"they're hands slip, {user.mention} gets away!", f"they grab at {ctx.author.mention}, strangling them back!"]
        strangle_owner_response = ["it kills them! RIP ☠️", f"causes {user.mention} to faint!"]
    
        if ctx.message.author.id == owner_id:
            e = discord.Embed(color=0xc700ff)
            e.description = f"{ctx.author.mention} strangles {user.mention} and {random.choice(strangle_owner_response)}"
            e.set_image(url="https://cdn.discordapp.com/attachments/807071768258805764/1108639607370813440/AnimeStranglingGif.gif"),
            await ctx.send(embed=e)
        else:
            e = discord.Embed(color=0xc700ff)
            e.description = f"{ctx.author.mention} strangles {user.mention} and {random.choice(strangle_response)}"
            e.set_image(url="https://cdn.discordapp.com/attachments/807071768258805764/1108639607370813440/AnimeStranglingGif.gif"),
            await ctx.send(embed=e)
        
    # Stab Command
    @commands.command(aliases=["bats", "Stab", "batS"])
    async def stab(self, ctx, user:discord.Member):
        stab_response = ["it kills them! RIP ☠️", "they bleed out! RIP ☠️","they missed!", f"due to their momentum, the knife comes back and stabs {ctx.author.mention}!"]
        stab_owner_response = ["it kills them! RIP ☠️", f"{user.mention} bleeds out! RIP ☠️"]
    
        if ctx.message.author.id == owner_id:
            e = discord.Embed(color=0xc700ff)
            e.description = f"{ctx.author.mention} stabs {user.mention} and {random.choice(stab_owner_response)}"
            e.set_image(url="https://media.discordapp.net/attachments/807071768258805764/1106846955612684308/AnimeStabbingGif.gif"),
            await ctx.send(embed=e)
        else:
            e = discord.Embed(color=0xc700ff)
            e.description = f"{ctx.author.mention} stabs {user.mention} and {random.choice(stab_response)}"
            e.set_image(url="https://media.discordapp.net/attachments/807071768258805764/1106846955612684308/AnimeStabbingGif.gif"),
            await ctx.send(embed=e)
    
    # Shoot Command
    @commands.command(aliases=["toohs", "Shoot", "toohS"], pass_context=True)
    async def shoot(self, ctx, user:discord.Member):
        shoot_response = ["it kills them! RIP ☠️", "it goes straight through their skull! RIP ☠️","it does nothing! They have a body of steel!", f"it ricochets off the wall and kills {ctx.author.mention}! RIP ☠️", "the gun jams!"]
        shoot_owner_response = ["it kills them! RIP ☠️", "it goes straight through their skull! RIP ☠️"]
    
        if ctx.message.author.id == owner_id:
            e = discord.Embed(color=0xc700ff)
            e.description = f"{ctx.author.mention} shoots at {user.mention} and {random.choice(shoot_owner_response)}"
            e.set_image(url="https://cdn.discordapp.com/attachments/807071768258805764/1106843019321282591/AnimeShootingGif.gif"),
            await ctx.send(embed=e)
        else:
            e = discord.Embed(color=0xc700ff)
            e.description = f"{ctx.author.mention} shoots at {user.mention} and {random.choice(shoot_response)}"
            e.set_image(url="https://cdn.discordapp.com/attachments/807071768258805764/1106843019321282591/AnimeShootingGif.gif"),
            await ctx.send(embed=e)

    # Deathnote Command
    @commands.command(aliases=["etonhtaed", "Deathnote", "etonhtaeD"])
    async def deathnote(self, ctx, user:discord.Member, *, arg):
        
        # Embeds
        ha = discord.Embed(color=0xc700ff)
        ha.description = f"{user.mention} had a heart attack and died! RIP ☠️"
        ha.set_image(url="https://media.discordapp.net/attachments/807071768258805764/1116945127810805820/HeartAttackGif.gif")
    
        e1 = discord.Embed(color=0xc700ff)
        e1.description = f"{user.mention} fell off a cliff and died! RIP ☠️"
        e1.set_image(url="https://media.discordapp.net/attachments/807071768258805764/1116815474852896890/FallOffCliffGif.gif")
   
        e2 = discord.Embed(color=0xc700ff)
        e2.description = f"{user.mention} got ran over by a train and died! RIP ☠️"
        e2.set_image(url="https://media.discordapp.net/attachments/807071768258805764/1116814851403165726/HitByTrainGif.gif")

        e3 = discord.Embed(color=0xc700ff)
        e3.description = f"{user.mention} drowned in a 2 inch pool! RIP ☠️"
        e3.set_image(url="https://media.discordapp.net/attachments/807071768258805764/1116822537272316004/DrowningGif.gif")
    
        e4 = discord.Embed(color=0xc700ff)
        e4.description = f"{user.mention} was crushed by a boulder and died! RIP ☠️"
        e4.set_image(url="https://media.discordapp.net/attachments/807071768258805764/1116944054052204584/CrushedByBoulderGif.gif")
    
        e5 = discord.Embed(color=0xc700ff)
        e5.description = f"{user.mention} choked on a hot dog and died! RIP ☠️"
        e5.set_image(url="https://media.discordapp.net/attachments/807071768258805764/1116944567107854336/ChokingGif.gif")
    
        e6 = discord.Embed(color=0xc700ff)
        e6.description = f"{user.mention} got into a car crash and died! RIP ☠️"
        e6.set_image(url="https://media.discordapp.net/attachments/807071768258805764/1116944863032787105/CarCrashGif.gif")

        e7 = discord.Embed(color=0xc700ff)
        e7.description = f"{user.mention} was murdered! RIP ☠️"
        e7.set_image(url="https://media.discordapp.net/attachments/807071768258805764/1116945578954334228/MurderGif.gif")

        e8 = discord.Embed(color=0xc700ff)
        e8.description = f"{user.mention} was shocked by 10,000 volts of electricity and died! RIP ☠️"
        e8.set_image(url="https://media.discordapp.net/attachments/807071768258805764/1117941430439120936/ElectricShockGif.gif")

        e9 = discord.Embed(color=0xc700ff)
        e9.description = f"{user.mention} got caught in a fire and died! RIP ☠️"
        e9.set_image(url="https://media.discordapp.net/attachments/807071768258805764/1116946041422495844/FireGif.gif")

        e10 = discord.Embed(color=0xc700ff)
        e10.description = f"{user.mention} swallowed tnt and exploded! RIP ☠️"
        e10.set_image(url="https://media.discordapp.net/attachments/807071768258805764/1116946286361456750/ExplodingGif.gif")

        e11 = discord.Embed(color=0xc700ff)
        e11.description = f"{user.mention} got struck by lightning and died! RIP ☠️"
        e11.set_image(url="https://media.discordapp.net/attachments/807071768258805764/1116946562329882725/LightningGif.gif")

        e12 = discord.Embed(color=0xc700ff)
        e12.description = f"{user.mention} fell into a volcano and died! RIP ☠️"
        e12.set_image(url="https://media.discordapp.net/attachments/807071768258805764/1116946885542936576/VolcanoGif.gif")

        e13 = discord.Embed(color=0xc700ff)
        e13.description = f"{user.mention} got sucked into a tornado and died! RIP ☠️"
        e13.set_image(url="https://media.discordapp.net/attachments/807071768258805764/1116947245598781576/TornadoGif.gif")

        e14 = discord.Embed(color=0xc700ff)
        e14.description = f"{user.mention} fell into a crack made by an earthquake and died! RIP ☠️"
        e14.set_image(url="https://media.discordapp.net/attachments/807071768258805764/1116947453229404301/EarthquakeGif.gif")

        e15 = discord.Embed(color=0xc700ff)
        e15.description = f"{user.mention} got washed away in a hurricane and died! RIP ☠️"
        e15.set_image(url="https://media.discordapp.net/attachments/807071768258805764/1116947898169557002/HurricaneGif.gif")

        # Comparing the user arg to the statements
        if arg.lower() == "cliff":
            await ctx.send(embed=e1)
        if arg.lower() == "train":
            await ctx.send(embed=e2)
        if arg.lower() == "drown":
            await ctx.send(embed=e3)
        if arg.lower() == "crush":
            await ctx.send(embed=e4)
        if arg.lower() == "choke":
            await ctx.send(embed=e5)
        if arg.lower() == "car crash":
            await ctx.send(embed=e6)
        if arg.lower() == "murder":
            await ctx.send(embed=e7)
        if arg.lower() == "shock":
            await ctx.send(embed=e8)
        if arg.lower() == "fire":
            await ctx.send(embed=e9)
        if arg.lower() == "explosion":
            await ctx.send(embed=e10)
        if arg.lower() == "lightning":
            await ctx.send(embed=e11)
        if arg.lower() == "volcano":
            await ctx.send(embed=e12)
        if arg.lower() == "tornado":
            await ctx.send(embed=e13)
        if arg.lower() == "earthquake":
            await ctx.send(embed=e14)
        if arg.lower() == "hurricane":
            await ctx.send(embed=e15)

    # Highfive Command
    @commands.command(aliases=["evifhgih", "Highfive", "evifhgiH"])
    async def highfive(self, ctx, user:discord.Member): 
        e = discord.Embed(color=0xc700ff)
        e.description = f"{ctx.author.mention} highfives {user.mention}!"
        e.set_image(url="https://media.discordapp.net/attachments/807071768258805764/1106851182279934072/AnimeHighfiveGif.gif"),
        await ctx.send(embed=e)

    # Poke Command
    @commands.command(aliases=["ekop", "Poke", "ekoP"])
    async def poke(self, ctx, user:discord.Member):
        e = discord.Embed(color=0xc700ff)
        e.description = f"{ctx.author.mention} pokes {user.mention}!"
        e.set_image(url="https://media.discordapp.net/attachments/807071768258805764/1117137231950401617/PokeGif.gif"),
        await ctx.send(embed=e)

    # Pat Command
    @commands.command(aliases=["tap", "Pat", "taP"])
    async def pat(self, ctx, user:discord.Member):
        e = discord.Embed(color=0xc700ff)
        e.description = f"{ctx.author.mention} pats {user.mention}!"
        e.set_image(url="https://cdn.discordapp.com/attachments/807071768258805764/1106851615320846386/AnimePatGif.gif"),
        await ctx.send(embed=e)
    
    # Hug Command
    @commands.command(aliases=["guh", "Hug", "guH"])
    async def hug(self, ctx, user:discord.Member):  
        e = discord.Embed(color=0xc700ff)
        e.description = f"{ctx.author.mention} hugs {user.mention}!"
        e.set_image(url="https://media.discordapp.net/attachments/807071768258805764/1106847914019536926/AnimeHuggingGif.gif"),
        await ctx.send(embed=e)

    # Kiss Command
    @commands.command(aliases=["ssik", "Kiss", "ssiK"])
    async def kiss(self, ctx, user:discord.Member):
        e = discord.Embed(color=0xc700ff)
        e.description = f"{ctx.author.mention} kisses {user.mention}!"
        e.set_image(url="https://media.discordapp.net/attachments/807071768258805764/1106848342966800404/AnimeKissingGif.gif"),
        await ctx.send(embed=e)

    # Cuddle Command
    @commands.command(aliases=["eldduc", "Cuddle", "eldduC"])
    async def cuddle(self, ctx, user:discord.Member): 
        e = discord.Embed(color=0xc700ff)
        e.description = f"{ctx.author.mention} cuddles with {user.mention}!"
        e.set_image(url="https://media.discordapp.net/attachments/807071768258805764/1106848675025666128/AnimeCuddlingGif.gif"),
        await ctx.send(embed=e)
###################################[ ADDING COG ]###################################
# Adding cog to bot
async def setup(bot):
    await bot.add_cog(Action(bot))