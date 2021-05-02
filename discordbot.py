from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
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
    random.seed()
    vals=arg.split('d')
    '''
    result=[]
    dsum=0
    for i in range(vals[0]):{
        result.append(random.randint(1,vals[1]))
        dsum+=result[i]
    }
    '''
    await ctx.send(random.randint(1,vals[1]))
    
    
bot.run(token)
