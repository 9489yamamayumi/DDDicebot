from discord.ext import commands
import os
import traceback
import random

bot = commands.Bot(command_prefix='.')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.command()
async def r(ctx,arg):
    #prepare
    vals=arg.split('d')
    times=int(vals[0])
    sides=int(vals[1])
    results=[]
    rsltsum=0
    #diceroll
    for i in range(times):
        roll=random.randint(1,sides)
        results.append(roll)
        rsltsum+=roll
    #result
    await ctx.send(f"{arg} >> {rsltsum} : {results}")
    
bot.run(token)
