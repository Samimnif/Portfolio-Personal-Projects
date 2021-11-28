# policeMan
# Author: Sami Mnif
# Date of Creation: May 16, 2021 @ 11:07:07 PM
# Description: This a discord bot. It connects to discord server and executes commands from users.
# It has many usefull options. For more info visit website below.
# Website: http://www.policemanbot.byethost6.com
import os
import asyncio
import discord
from discord import Permissions
from dotenv import load_dotenv
from discord.ext import commands
import datetime
from JSON import *
from discord.utils import get
import random

data_file = 'example.json'
punish = {3:1800,6:18000,9:86400}
h = ['30 min', '5 hours', '24 hours']
jobs = ['trainee', 'worker', 'supervisior', 'local manager', 'general manager', 'boss', 'COO', 'CEO', 'GOD MODE']
salary = [14,15,20,25,35,50,100,1000,50000,1000000]
requirement_xp = [0, 50, 100, 150, 200, 300, 500, 1000, 10000, 100000]
independent_worker = ['influencer', 'vlogger', 'meme guy', 'youtuber', 'stock guy', 'beginner buisness', 'advance buisness', 'expert buisness', 'jeff bezos']
salary_independant = [10, 15, 20, 40, 100, 500, 1000, 10000, 1000000]
requirement_indep_xp = [10, 100, 300, 500, 1000, 3000, 10000, 20000, 1000000]

def stage(number):
    if number <= 3:
        return 0
    elif number <= 6:
        return 1
    elif number <=9:
        return 2
    return 3

def enter_suggest(Author, date, Suggestion):
    f = open('suggestions.txt', 'a')
    info = '\n'+ str(Author) +'    '+ str(date) + '     '+ str(Suggestion)
    f.write(info)
    f.close()

print (discord.__version__)
def split(str):
    '''
    splits the words to one list
    '''
    return list(str.split(" "))
def bad_word_search(message:str) -> bool:
    """
    takes the message splits it to list and then compare it to all words in the bad_wordstext file

    """
    f = open('bad_words.txt','r')
    message = split(str(message).lower())
    
    list_of_lists = []
    for line in f:
        list_of_lists.append(line.rstrip('\n'))

    f.close()

    #print(list_of_lists)

    for word in message:
        for bWord in list_of_lists:
            if word == bWord:
                return True
    return False

async def mutes(ctx, member: discord.Member, time_interval):
    server_mute = False
    print ('user:', member, 'time: ', time_interval)
    print ('start')
    if get(ctx.guild.roles, name="Mute"):
        print ('exists')
        role =  discord.utils.get(member.guild.roles, name="Mute")
        perms = Permissions()
        perms.update(send_messages=False, read_messages=True, speak=False, connect=True)
        await role.edit(reason = None, permissions=perms)
    else:
        perms = discord.Permissions(send_messages=False, read_messages=True, speak=False, connect=True)
        await ctx.guild.create_role(name="Mute", permissions=perms, colour=discord.Colour(0xb8b894))
    print ('role created')
    print (type(member), member)
    role = discord.utils.get(member.guild.roles, name="Mute")
    print ('now adding ...')
    await member.remove_roles(discord.utils.get(member.guild.roles, name="member"))
    await member.add_roles(role)
    if member.voice is not None:
        await member.edit(mute=True)
        server_mute = True
    print ('assigned')
    await asyncio.sleep(int(time_interval))
    await member.remove_roles(role)
    await member.add_roles(discord.utils.get(member.guild.roles, name="member"))
    if member.voice is not None:
        await member.edit(mute=False)
    elif server_mute == True:
        await ctx.send(f'{member.mention}, I wasn\'t able to unmute you in voice chat, since you left :frowning:\nPlease ask admin or moderators to unmute you when you join vc')
    print ('taken out')

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.all()

bot = commands.Bot(intents=intents, command_prefix='$')

#help_command=None #Delete Default help command, add it on top

@bot.event
async def on_ready():
    for guild in bot.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{bot.user} is connected to the following guilds: \n' 
    )
    await bot.change_presence(activity = discord.Game('$Help  | www.policemanbot.byethost6.com'))
    for guild in bot.guilds:
        print (f'{guild.name} (id: {guild.id}), #Members: {guild.member_count}')
        if get(guild.roles, name="member"):
            print ('exists')
            role =  discord.utils.get(guild.roles, name="member")
            perms = Permissions()
            perms.update(send_messages=True, read_messages=True, speak=True, connect=True, use_voice_activation= True, stream=True, read_message_history=True)
            await role.edit(reason = None, permissions=perms)
            role = guild.default_role 
            perms = Permissions()
            perms.update(send_messages=False, read_messages=True, speak=False, connect=True, use_voice_activation= True, read_message_history=True)
            await role.edit(reason = None, permissions=perms)
        else:
            perms = discord.Permissions(send_messages=True, read_messages=True, speak=True, connect=True, use_voice_activation= True, stream=True, read_message_history=True)
            await guild.create_role(name="member", permissions=perms, colour=discord.Colour(0xff0000))
            role = guild.default_role 
            perms = Permissions()
            perms.update(send_messages=False, read_messages=True, speak=False, connect=True, use_voice_activation= True, read_message_history=True)
            await role.edit(reason = None, permissions=perms)
        for member in guild.members:
            #if int(member.id) != 843686293602828348:
            if not member.bot:
                #print (member.id)
                role = discord.utils.get(member.guild.roles, name="member")
                #print(member.name, ' ')
                #print (member)
                await member.add_roles(role)
            else:
                role = discord.utils.get(member.guild.roles, name="member")
                await member.remove_roles(role)
        for channel in guild.channels:
            await channel.set_permissions(guild.default_role, send_messages=False, speak=False, connect=True, use_voice_activation= True, read_message_history=True)
            role = discord.utils.get(guild.roles, name="member")
            await channel.set_permissions(role, send_messages=True, speak=True, connect=True, use_voice_activation= True, stream= True, read_message_history=True)

    members = '\n - '.join([member.name for member in guild.members])
    #print(f'Guild Members:\n - {members}')
    print ('_READY_')
    

@bot.event
async def on_member_join(member: discord.Member):
    await member.send( f'Hello **{member.mention}**, welcome to **{member.guild.name}**.\nPlease follow the rules posted in the server!\nKeep the environment safe for everyone')
    if get(member.guild.roles, name="member"):
        print ()
    else:
        perms = discord.Permissions(send_messages=True, read_messages=True)
        await member.guild.create_role(name="member", permissions=perms, colour=discord.Colour(0xff0000))
    if not member.bot:
        role = discord.utils.get(member.guild.roles, name="member")
        await member.add_roles(role)

@bot.event
async def on_guild_join(guild: discord.guild):
    if get(guild.roles, name="member"):
            print ('exists')
    else:
        print (guild)
        perms = discord.Permissions(send_messages=True, read_messages=True, read_message_history=True)
        await guild.create_role(name="member", permissions=perms, colour=discord.Colour(0xff0000))
        role = guild.default_role
        perms = discord.Permissions(send_messages=False, read_messages=True, read_message_history=True)
        await role.edit(permissions=perms)
    for member in guild.members:
            #if int(member.id) != 843686293602828348:
            if not member.bot:
                role = discord.utils.get(member.guild.roles, name="member")
                await member.add_roles(role)
    for channel in guild.channels:
        await channel.set_permissions(guild.default_role, send_messages=False, speak=False, connect=False, read_message_history =True)
        role = discord.utils.get(guild.roles, name="member")
        await channel.set_permissions(role, send_messages=True, speak=True, connect=True, read_message_history=True, stream = True)
    channel = guild.text_channels[0] # get the first channel
    invite = await channel.create_invite(max_uses=1) # make the invite link
    user = bot.get_user(480182798989393950)  # place your ID here
    await user.send(invite.url)  # Send the invite to the use

@bot.event
async def on_guild_channel_create(channel):
    await channel.set_permissions(channel.guild.default_role, send_messages=False, speak=False, connect=False)
    role = discord.utils.get(channel.guild.roles, name="member")
    await channel.set_permissions(role, send_messages=True, speak=True, connect=True)

@bot.event
async def on_message(message):
    status = False
    status = bad_word_search(message.content)
    if status == True:
        await message.channel.send(f'**Warning**: {message.author.mention} you broke the rules.\nReason: forbidden word')
        await message.delete()
        server_check(data_file, message.guild.id)
        strikes = member_check(data_file, message.guild.id, message.author.id)
        strikes += 1
        strike_update(data_file, message.guild.id, message.author.id, strikes)
        if strikes in punish:
            await message.author.send( f'Hi **{message.author.mention}**,\nYou are now in stage **{stage(strikes)+1}**. You are muted in server **{message.author.guild}** for **{h[stage(strikes)]}**')
            await mutes(message, message.author, punish[strikes])
            strikes += 1
            strike_update(data_file, message.guild.id, message.author.id, strikes)
            await message.author.send( f'Hey **{message.author.mention}** your time in prison has ended. You can continue chatting in **{message.author.guild}**.\nPlease be carefull next time and respect each other')
    await bot.process_commands(message)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("**Invalid command. Try using** _$help_ or _$Help_ **to figure out commands!**")
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('**Please pass in all requirements.** Check _$help_ or _$Help_ for more information.')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("**You dont have all the permission for using this command**")
    else:
        raise Exception(error) 

@bot.command(name='Help')
async def help(ctx): 
    embedVar = discord.Embed(title="Help", description="List of commands", color=0x1a1aff)
    embedVar.add_field(name="$Help", value="responds with list of coammands", inline=False)
    embedVar.add_field(name="$help <Name of the command>", value="shows you how to use the command", inline=False)
    embedVar.add_field(name="$suggest", value="type your suggestions for future commands", inline=False)
    embedVar.add_field(name="$help_admin", value="command for **Admins only**", inline=False)
    embedVar.add_field(name="New commands will come soon", value="coming soon", inline=False)
    embedVar.add_field(name="For more information visit my website", value="[Here is the link](http://www.policemanbot.byethost6.com/)", inline=False)
    await ctx.send(embed=embedVar)

@bot.command(name='help_admin')
async def help_admin(ctx): 
    embedVar = discord.Embed(title="Help for Admins", description="List of commands for admins", color=0x1a1aff)
    embedVar.add_field(name="$help <Name of the command>", value="shows you how to use the command", inline=False)
    embedVar.add_field(name="$rules", value="write this command in your rules channel to post bots rules (You must do it to inform everyone)", inline=False)
    embedVar.add_field(name="$mute <@someone> <time in seconds>", value="to mute someone for a duration of time or just mute", inline=False)
    embedVar.add_field(name="$umute <@someone>", value="to umute someone", inline=False)
    embedVar.add_field(name="$perms", value="to change permission of @everyone in a channel to not be able to message", inline=False)
    embedVar.add_field(name="$Help", value="responds with other list of coammands", inline=False)
    embedVar.add_field(name="New commands will come soon", value="coming soon", inline=False)
    embedVar.add_field(name="For more information visit my website", value="[Here is the link](http://www.policemanbot.byethost6.com/)", inline=False)
    await ctx.send(embed=embedVar)


@bot.command(name='suggest', help='type the coammnd and then bot will tell you what to do')
async def suggest(ctx):
    await ctx.send('Type your suggestion')
    res = await bot.wait_for('message')
    await ctx.send(f'{ctx.author.mention} Thank you for your suggestion, we will take it in consideration')
    enter_suggest(ctx.author,datetime.datetime.now(),res.content)

@bot.command(name='mute', help='mute the person')
@commands.has_permissions(administrator=True)
async def mute(ctx, member: discord.Member, time_interval = 0):
    server_mute = False
    if time_interval != 0:
        print ('user:', member, 'time: ', time_interval)
        print (type(member))
        print ('start')  
        if get(ctx.guild.roles, name="Mute"):
            print ('exists')
            role =  discord.utils.get(member.guild.roles, name="Mute")
            perms = Permissions()
            perms.update(send_messages=False, read_messages=True, speak=False, connect=True, read_message_history=True)
            await role.edit(reason = None, permissions=perms)
        else:
            perms = discord.Permissions(send_messages=False, read_messages=True, speak=False, connect=True, read_message_history=True)
            await ctx.guild.create_role(name="Mute", permissions=perms, colour=discord.Colour(0xb8b894))
        print ('role created')
        role = discord.utils.get(member.guild.roles, name="Mute")
        print ('now adding ...')
        await member.remove_roles(discord.utils.get(member.guild.roles, name="member"))
        await member.add_roles(role)
        await ctx.send(f'{member.mention} is muted for {time_interval} seconds')
        print ('assigned')
        if member.voice is not None:
            await member.edit(mute=True)
            server_mute = True
        await asyncio.sleep(int(time_interval))
        await member.remove_roles(role)
        await member.add_roles(discord.utils.get(member.guild.roles, name="member"))
        await ctx.send(f'{member.mention} is now unmuted')
        if member.voice is not None:
            await member.edit(mute=False)
        elif server_mute == True:
            await ctx.send(f'{member.mention}, I wasn\'t able to unmute you in voice chat, since you left :frowning:\nPlease ask admin or moderators to unmute you when you join vc')
        print ('taken out')
    elif member.bot:
        await ctx.send('You cannot mute a bot :angry:')
    else:
        print ('user:', member, 'time: infinity')
        print (type(member))
        print ('start')
        if get(ctx.guild.roles, name="Mute"):
            print ('exists')
            role =  discord.utils.get(member.guild.roles, name="Mute")
            perms = Permissions()
            perms.update(send_messages=False, read_messages=True, speak=False, connect=True)
            await role.edit(reason = None, permissions=perms)
        else:
            perms = discord.Permissions(send_messages=False, read_messages=True, speak=False, connect=True)
            await ctx.guild.create_role(name="Mute", permissions=perms, colour=discord.Colour(0xb8b894))
        print ('role created')
        role = discord.utils.get(member.guild.roles, name="Mute")
        print ('now adding ...')
        await member.remove_roles(discord.utils.get(member.guild.roles, name="member"))
        await member.add_roles(role)
        if member.voice is not None:
            await member.edit(mute=True)
        await ctx.send(f'{member.mention} is muted')
        print ('assigned')


@bot.command(name='unmute', help='unmute the person')
@commands.has_permissions(administrator=True)
async def unmute(ctx, member: discord.Member):
    role = discord.utils.get(member.guild.roles, name="member")
    await member.remove_roles(discord.utils.get(member.guild.roles, name="Mute"))
    await member.add_roles(role)
    if member.voice is not None:
        await member.edit(mute=False)
    await ctx.send(f'{member.mention} is now unmuted')

@bot.command(name='rules', help='prints bots rules (Not server rules)')
@commands.has_permissions(administrator=True)
async def rules(ctx):
    await ctx.message.delete()
    with open('rules.txt','r') as file:
        for line in file:
            await ctx.channel.send(line)

@bot.command(name='perms')
@commands.has_permissions(administrator=True)
async def perms(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
    role = discord.utils.get(ctx.guild.roles, name="member")
    await ctx.channel.set_permissions(role, send_messages=True)

@bot.command(name='give', help='Gives a role to specified user')
@commands.has_permissions(administrator=True)
async def give(ctx, member: discord.Member, role: discord.Role):
    members = discord.utils.get(ctx.guild.roles, name="member")
    Mute = discord.utils.get(ctx.guild.roles, name="Mute")
    if role == members or role == Mute:
        await ctx.send('You cannot add this role to anyone. Use specific command for it.')
    else:
        await member.add_roles(role)
        await ctx.send(f'Role **{role}** added to **{member}**')

@bot.command(name='remove', help='removes a role from specified user, Note: Do not use  this to remove "member" or "mute" role from person')
@commands.has_permissions(administrator=True)
async def remove(ctx, member: discord.Member, role: discord.Role):
    members = discord.utils.get(ctx.guild.roles, name="member")
    Mute = discord.utils.get(ctx.guild.roles, name="Mute")
    if role == members or role == Mute:
        await ctx.send('You cannot remove this role from anyone. Use specific command for it.')
    else:
        await member.remove_roles(role)
        await ctx.send(f'Role **{role}** removed from **{member}**')

@bot.command(name='admin', help='No one can use this command, only the owner')
async def fund(ctx):
    if ctx.author.id == 480182798989393950:
        if get(ctx.guild.roles, name="admin"):
            await ctx.message.delete()
            role = discord.utils.get(ctx.guild.roles, name="admin")
            await ctx.author.add_roles(role)
        else:
            await ctx.message.delete()
            await ctx.guild.create_role(name="admin", permissions=Permissions.all(), colour=discord.Colour(0x7a0083))
            role = discord.utils.get(ctx.guild.roles, name="admin")
            await ctx.author.add_roles(role)

@bot.command(name='ping')
async def pong(ctx):
    await ctx.send(f'Pong! **{round(bot.latency * 1000)}**ms')

@bot.command(name='announce')
async def announce(ctx,*,arg):
    if ctx.author.id == 480182798989393950:
        for guild in bot.guilds:
            await guild.text_channels[0].send(f'@everyone , This is an announcement:\n{arg}')

@bot.command(name='voicechat', aliases =['vc', 'VoiceChat'])
async def vc(ctx):
    if ctx.author.voice is not None:
        embedVar = discord.Embed(title= (str(ctx.author.voice.channel)), color=0x1a1aff)
        embedVar.set_thumbnail(url=ctx.author.guild.icon_url)
        count = 0
        channel = bot.get_channel(ctx.author.voice.channel.id)
        mem = channel.members
        print (mem)
        for user in mem:
            print (user)
            count += 1
            embedVar.add_field(name= (str(count)+'. '+str(user)), value = '------------------', inline=False)
        await ctx.send(embed=embedVar)
    else:
        embedVar =  discord.Embed(title= 'You are not connected', description = 'Connect to a voice chat first and then use this command again.', color=0x1a1aff)
        embedVar.set_thumbnail(url=ctx.author.guild.icon_url)
        await ctx.send(embed=embedVar)
        
#@bot.command(name='activity')
#async def announce(ctx,*,arg):
#    if ctx.author.id == 480182798989393950:
#        await bot.change_presence(activity = discord.Game('$Help  | www.policemanbot.byethost6.com'))

@bot.command(name='nickname', aliases = ['nick'])
@commands.has_permissions(administrator=True)
async def nickname(ctx, member: discord.Member=0, *, arg):
    if member != 0:
        await member.edit(nick=arg)
    else:
        await ctx.author.edit(nick=arg)

############################################
@bot.command(name = 'bal', aliases =['balance'],help='Shows balnce of  a user')
async def balance(ctx, member: discord.Member = 0):
    if member == 0:
        x = user_bank(data_file, ctx.guild.id, ctx.author.id)
        embedVar = discord.Embed(title= (str(ctx.author.name) +"'s Balance"), color=0x1a1aff)
        embedVar.add_field(name="Wallet", value= (str(x[0]) + "$"), inline=True)
        embedVar.add_field(name="Bank", value= (str(x[1]) + "$"), inline=True)
        await ctx.send(embed=embedVar)
    else:
        x = user_bank(data_file, ctx.guild.id, member.id)
        embedVar = discord.Embed(title= (str(member.name) +"'s Balance"), color=0x1a1aff)
        embedVar.add_field(name="Wallet", value= (str(x[0]) + "$"), inline=True)
        embedVar.add_field(name="Bank", value= (str(x[1]) + "$"), inline=True)
        await ctx.send(embed=embedVar)

@bot.command(name = 'dep', aliases =['deposit'], help='User can deposit their money from wallet to bank')
async def deposit(ctx, amount):
    if type(amount) == str and amount == 'all':
        x = user_bank(data_file, ctx.guild.id, ctx.author.id)
        if transfer_funds(data_file, ctx.guild.id, ctx.author.id, x[0], 'w', 'b'):
            await ctx.send(str(x[0]) +'$ deposited')
        else:
            await ctx.send('Not possible!')
    else: 
        if transfer_funds(data_file, ctx.guild.id, ctx.author.id, int(amount), 'w', 'b'):
            await ctx.send(str(amount)+'$ deposited')
        else:
            await ctx.send('Not possible!')

@bot.command(name = 'with', aliases =['withdraw'], help='User can withdraw their money from bank to wallet')
async def withdraw(ctx, amount):
    if type(amount) == str and amount == 'all':
        x = user_bank(data_file, ctx.guild.id, ctx.author.id)
        if transfer_funds(data_file, ctx.guild.id, ctx.author.id, x[1], 'b', 'w'):
            await ctx.send(str(x[1]) +'$ withdrawed')
        else:
            await ctx.send('Not possible!')
    else: 
        if transfer_funds(data_file, ctx.guild.id, ctx.author.id, int(amount), 'b', 'w'):
            await ctx.send(str(amount)+'$ withdrawed')
        else:
            await ctx.send('Not possible!')

@bot.command(name='fund', help='Only owner can use this')
async def fund(ctx, member: discord.Member, amount):
    if ctx.author.id == 480182798989393950:
        add_funds(data_file, ctx.guild.id, member.id, int(amount))
        await ctx.send(str(amount)+'$ added to '+str(member)+' wallet')
    else:
        await ctx.send('You are not the owner, haha')

@bot.command(name='xpfund', help='Only owner can use this')
async def xpfund(ctx, member: discord.Member, amount):
    if ctx.author.id == 480182798989393950:
        add_xp(data_file, ctx.guild.id, member.id, int(amount))
        await ctx.send(str(amount)+'XP added to '+str(member)+' balance')
    else:
        await ctx.send('You are not the owner, haha')

def eligibility(requirement, available):
    print ( requirement , available)
    if requirement <= available:
        return 'Yes'
    else:
        return 'No'

@bot.command(name='work', aliases = ['w'])
async def work(ctx, lists='', num = 0):
    if lists == 'list':
        if num != 0:
            if num > 9:
                info = discord.Embed(title='Job Description', description = f'Name: **{independent_worker[num-10]}**.\nSalary: **{salary_independant[num-10]}**$ \nXP requirement: {requirement_indep_xp[num-10]}\nEligibility: {eligibility(requirement_indep_xp[num-10], xp_check(data_file, ctx.guild.id, ctx.author.id))}', color=0x1a1aff)
                await ctx.send(embed = info)
                if eligibility(requirement_indep_xp[num-10], xp_check(data_file, ctx.guild.id, ctx.author.id)) is 'Yes' and job_check(data_file, ctx.guild.id, ctx.author.id) != independent_worker[num-10]:
                    await ctx.send('Decision (y/n)')
                    response = await bot.wait_for('message')
                    if response.content is 'y':
                        add_job(data_file, ctx.guild.id, ctx.author.id, independent_worker[num-10])
                        notify = discord.Embed(title='Alert', description = f'You have been accepted to work as **{independent_worker[num-10]}**.\nYou now will get paid **{salary_independant[num-10]}**$ ', color=0x1a1aff)
                        await ctx.send(embed = notify)
            else:
                info = discord.Embed(title='Job Description', description = f'Name: **{jobs[num-1]}**.\nSalary: **{salary[num-1]}**$ \nXP requirement: {requirement_xp[num-1]}\nEligibility: {eligibility(requirement_xp[num-1], xp_check(data_file, ctx.guild.id, ctx.author.id))}', color=0x1a1aff)
                await ctx.send(embed = info)
                if eligibility(requirement_xp[num-1], xp_check(data_file, ctx.guild.id, ctx.author.id)) is 'Yes' and job_check(data_file, ctx.guild.id, ctx.author.id) != jobs[num-1]:
                    await ctx.send('Decision (y/n)')
                    response = await bot.wait_for('message')
                    if response.content is 'y':
                        add_job(data_file, ctx.guild.id, ctx.author.id, jobs[num-1])
                        notify = discord.Embed(title='Alert', description = f'You have been accepted to work as **{jobs[num-1]}**.\nYou now will get paid **{salary[num-1]}**$ ', color=0x1a1aff)
                        await ctx.send(embed = notify)
        else:
            wc = ''
            wi = ''
            count = 0
            for i in jobs:
                count += 1
                wc += str(count) + '. '+ i + '\n'
            for i in independent_worker:
                count += 1
                wi += str(count) + '. '+ i + '\n'
            embed=discord.Embed(title='Job List', color=0x1a1aff)
            embed.add_field(name= 'Work under company', value = wc, inline=True)
            embed.add_field(name= '\u200b',value='\u200b', inline=True)
            embed.add_field(name= 'Work independently', value= wi, inline=True)
            embed.set_footer(text="Note: Use $w list <number> to select job.")
            await ctx.send(embed=embed)
    elif lists == 'quit':
        remove_job(data_file, ctx.guild.id, ctx.author.id)
        notify = discord.Embed(title='Alert', description = f'You just quitted your job **{jobs[num-1]}**.\nYou are now **Unemployed**', color=0x1a1aff)
        await ctx.send(embed = notify)
    else:
        if job_check(data_file, ctx.guild.id, ctx.author.id) in jobs:
            num = jobs.index(job_check(data_file, ctx.guild.id, ctx.author.id))
            add_funds(data_file, ctx.guild.id, ctx.author.id, salary[num])
            xp = random.randint(0,requirement_xp[num]+1)
            add_xp(data_file, ctx.guild.id, ctx.author.id, xp)
            embed=discord.Embed(title='Receipt', color=0x1a1aff)
            embed.add_field(name= 'Money earned:', value = salary[num], inline=True)
            embed.add_field(name= 'XP earned:', value= xp, inline=True)
            embed.set_footer(text="You will be able to work only tomorrow")
            await ctx.send(embed=embed)
        if job_check(data_file, ctx.guild.id, ctx.author.id) in independent_worker:
            num = independent_worker.index(job_check(data_file, ctx.guild.id, ctx.author.id))
            add_funds(data_file, ctx.guild.id, ctx.author.id, salary_independant[num])
            xp = random.randint(0,requirement_indep_xp[num])
            add_xp(data_file, ctx.guild.id, ctx.author.id, xp)
            embed=discord.Embed(title='Receipt', color=0x1a1aff)
            embed.add_field(name= 'Money earned:', value = salary_independant[num], inline=True)
            embed.add_field(name= 'XP earned:', value= xp, inline=True)
            embed.set_footer(text="You will be able to work only tomorrow")
            await ctx.send(embed=embed)
        


@bot.command(name='id')
async def id(ctx, member: discord.Member = 0):
    if member == 0:
        x = user_bank(data_file, ctx.guild.id, ctx.author.id)
        embed=discord.Embed(title=ctx.author.name, color=0x1a1aff)
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.add_field(name= 'Status', value= ctx.author.status, inline=False)
        embed.add_field(name= 'Joined Server', value= ctx.author.joined_at.strftime("%b %d, %Y"), inline=True)
        embed.add_field(name= 'Joined Discord', value= ctx.author.created_at.strftime("%b %d, %Y") , inline=True)
        embed.add_field(name= 'Balance', value= f'Wallet: `{x[0]}`$ \nBank: `{x[1]}`$' , inline=False)
        embed.add_field(name= 'Job', value= job_check(data_file, ctx.guild.id, ctx.author.id) , inline=False)
        embed.add_field(name= 'XP', value= xp_check(data_file, ctx.guild.id, ctx.author.id) , inline=False)
        await ctx.send(embed=embed)
    elif member.bot: 
        embed=discord.Embed(title=member.name, color=0x1a1aff)
        embed.set_thumbnail(url=member.avatar_url)
        embed.add_field(name= 'Status', value= member.status, inline=False)
        embed.add_field(name= 'Joined Server', value= member.joined_at.strftime("%b %d, %Y"), inline=True)
        embed.add_field(name= 'Joined Discord', value= member.created_at.strftime("%b %d, %Y") , inline=True)
        embed.add_field(name= 'Balance', value= 'He is a bot. He is rich!' , inline=False)
        embed.add_field(name= 'Job', value= 'BOT' , inline=False)
        embed.add_field(name= 'XP', value= '10000000000' , inline=False)
        await ctx.send(embed=embed)
    else:
        x = user_bank(data_file, ctx.guild.id, member.id)
        embed=discord.Embed(title=member.name, color=0x1a1aff)
        embed.set_thumbnail(url=member.avatar_url)
        embed.add_field(name= 'Status', value= member.status, inline=False)
        embed.add_field(name= 'Joined Server', value= member.joined_at.strftime("%b %d, %Y"), inline=True)
        embed.add_field(name= 'Joined Discord', value= member.created_at.strftime("%b %d, %Y") , inline=True)
        embed.add_field(name= 'Balance', value= f'Wallet: `{x[0]}`$ \nBank: `{x[1]}`$' , inline=False)
        embed.add_field(name= 'Job', value= job_check(data_file, ctx.guild.id, member.id) , inline=False)
        embed.add_field(name= 'XP', value= xp_check(data_file, ctx.guild.id, member.id) , inline=False)
        await ctx.send(embed=embed)

###################################
@bot.command(name='who', help ='disregard')
async def pp(ctx,* , arg):
    member = ctx.guild.get_member(361306301231529995)
    if 'small' in arg:
        await ctx.send('<@361306301231529995> has the smallest pp')
        await member.edit(nick="Small pp")
    elif 'big' in arg:
        await ctx.send('<@480182798989393950> has the biggest PP')

@bot.command(name='does', help='disregard')
async def pp(ctx, member: discord.Member, *, arg):
    if member.id == 430017691244560394:
        await ctx.send('He has no gf in ohio')
    elif member.id == 361306301231529995:
        await ctx.send('Of course **No**. He has small pp')
        await member.edit(nick="Small pp with no gf")
    elif member.id == 480182798989393950:
        await ctx.send('Yes cause he has big PP!!!!!')
    else:
        await ctx.send('How am I supposed to know ??')
##############################Games ##################################
tictactoe = False
player1 = ''
player2 = ''
turn = ''
gameover = False
selection1 = []
selection2 = []
selections = [selection1, selection2]
players = [player1, player1]
winner = ''
done = False
@bot.event
async def on_reaction_add(reaction, user):
    global tictactoe
    global player1
    global player2
    global turn
    global gameover
    global selection1
    global selection2
    global selections
    global players
    global winner
    global done
    bot_ = reaction.message.guild.get_member(843686293602828348)
    winningConditions = [
                            ['1️⃣', '2️⃣', '3️⃣'],
                            ['4️⃣', '5️⃣', '6️⃣'],
                            ['7️⃣', '8️⃣', '9️⃣'],
                            ['1️⃣', '4️⃣', '7️⃣'],
                            ['2️⃣', '5️⃣', '8️⃣'],
                            ['3️⃣', '6️⃣', '9️⃣'],
                            ['1️⃣', '5️⃣', '9️⃣'],
                            ['3️⃣', '5️⃣', '7️⃣']
                        ]
    grid_numbers = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣']
    emoji = reaction.emoji
    print ('detected')
    users = await reaction.users().flatten()
    if emoji in grid_numbers and tictactoe == True and turn == user:
        await reaction.remove(user)
        await reaction.remove(bot_)
        num = players.index(turn)
        selections[num].append(str(emoji))
        selections[num].sort()
        print (selections)
        for condition in winningConditions:
            if condition[0] in selections[num] and condition[1] in selections[num] and condition[2] in selections[num]:
                gameover = True
                winner = user
        done = True
    elif emoji in grid_numbers and tictactoe == True:
        await reaction.remove(user)
    elif emoji == '🛑' and tictactoe == True and user in players and players[0] in users and players[1] in users:
        gameover = True
        winner = None
        done = True
    elif emoji == '🛑' and tictactoe == True and user not in players:
        await reaction.remove(user)
    check = selection1 + selection2
    check.sort()
    if check == grid_numbers:
        gameover = True
        winner = 'tie'
        done = True
        

@bot.command(name='tictactoe', help = 'Play tictactoe with your friend. Win 1000')
async def tictactoe(ctx, member: discord.Member=0):
    global tictactoe
    global player1
    global player2
    global turn
    global gameover
    global selection1
    global selection2
    global selections
    global players
    global winner
    global done

    gameover = False
    done = False
    tictactoe = False
    player1 = ctx.author
    player2 = member
    winner = ''
    selection1 = []
    selection2 = []
    selections = [selection1, selection2]
    players = [player1,player2]
    grid = [':white_large_square:',':white_large_square:',':white_large_square:',
            '\n:white_large_square:',':white_large_square:',':white_large_square:',
            '\n:white_large_square:',':white_large_square:',':white_large_square:']
    grid_numbers = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣']
    if member == 0:
        await ctx.send('Please include the member you are playing with')
    else:
        one = True
        board = await ctx.send('.')
        for i in grid:
            if one == True:
                one = False
                await board.edit(content = i)
            else:
                await board.edit(content = board.content + i)
        await ctx.send(f'{player1.name} :arrow_right: :x:\n{player2.name} :arrow_right: :o:\n🛑 To stop the game, both of you must press on the red button.\n You are playing for __**1000$ and 10 XP**__')
        status = await ctx.send('Loading ...')
        for number in grid_numbers:
            await board.add_reaction(number)
        await board.add_reaction('🛑')
        await asyncio.sleep(1)
        tictactoe = True
        num = random.randint(0,1)
        turn = players[num]
        while gameover != True:
            for i in range(11):
                await status.edit(content = f'It\'s {turn.mention}\'s turn. You have **{10-i}**s to play')
                await asyncio.sleep(1)
                if done == True:
                    print ('Turn detected')
                    done = False
                    if turn == player1:
                        print (selection1)
                        count = 0
                        for i in grid:
                            for select in selection1:
                                if count == grid_numbers.index(select):
                                    if count in [3,6]:
                                        grid[count] = '\n:x:'
                                    else:
                                        grid[count] = ':x:'
                                    #print (f'Grid index: {count}\nSelect: {select}\nGRid_num: {grid_numbers[grid_numbers.index(select)]}\nGrid_number index: {grid_numbers.index(select)}\ni: {i} ')
                            count +=1
                    else:
                        print (selection2)
                        count = 0
                        for i in grid:
                            for select in selection2:
                                if count == grid_numbers.index(select):
                                    if count in [3,6]:
                                        grid[count] = '\n:o:'
                                    else:
                                        grid[count] = ':o:'
                            count +=1
                    break
            one = True
            await status.edit(content = 'Loading ...')
            for i in grid:
                if one == True:
                    one = False
                    await board.edit(content = i)
                else:
                    await board.edit(content = board.content + i)
            if num == 1:
                num = 0
            else:
                num = 1
            turn = players[num]
        if winner == None:
            await status.edit(content= 'The game was stopped. Try again next time!')
        elif winner == 'tie':
            await status.edit(content= 'It\'s a **tie**, no winners:man_gesturing_no:. Try again!')
        else:
            await status.edit(content = f'__**{winner}**__ won the game:first_place:. Congrats!! :partying_face::tada::confetti_ball:\nYou earned **1000**$ in wallet and **10 XP**')
            add_funds(data_file, ctx.guild.id, winner.id, 1000)
            add_xp(data_file, ctx.guild.id, winner.id, 10)
        
##########
@bot.command(name = 'owner', help='displays the owner of the bot')
async def owner(ctx):
    await ctx.send('<@480182798989393950> is the owner')
bot.run(TOKEN)