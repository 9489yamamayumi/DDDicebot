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
async def ping(ctx):
    await ctx.send('pong')


@bot.command()
async def echo(ctx,arg):
    await ctx.send(arg)

@bot.command()
async def r(ctx,arg):
#    random.seed()
#    vals=arg.split('d')
#    times=int(vals[0])
#    sides=int(vals[1])
#    results=[]
#    rsltsum=0
#    for i in range(times):{
#        results.append(random.randint(1,sides))
#        rsltsum+=results[i]
#    }
#    await ctx.send(f"{arg} >> {rsltsum} : {results}")
     await ctx.send(f"ok")


bot.run(token)
