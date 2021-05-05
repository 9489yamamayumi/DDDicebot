from discord.ext import commands
import os
import traceback
import random

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)
    
TRPGmode = "None"
TRPGtype = ["CoC","Paranoia","Others"]

#change TRPG mode
@bot.command()
async def mc(ctx,arg):
    if(arg in TRPGtype):
        TRPGmode = arg
        await ctx.send(f"now changed TRPGmode to {arg}\r\nモードを {arg} に変更しました")
    else:
        await ctx.send(f"this mode isn't supported\r\nそのモードは存在しません")

#AdB to roll B-sides dices A times
@bot.command()
async def r(ctx,arg):
    #prepare
    vals=arg.split('d')
    results=[]
    rsltsum=0
    exstts=""
    #diceroll
    for i in range(int(vals[0])):
        roll=random.randint(1,int(vals[1]))
        results.append(roll)
        rsltsum+=roll
    #result
    if(arg=="1d100" and TRPGmode=="CoC"):
        if(rsltsum<6):exstts = "<critical!>"
        if(rsltsum>95):exstts = "<fumble!>"
    await ctx.send(f"roll {arg} -> {rsltsum} : {results} {exstts}")
    
    
bot.run(token)
