import random
import datetime

from discord.ext import commands

from cogs.language_commands import get_language
from database import User


def get_random_color():
    """Random generate color"""
    return random.choice(['white', 'black'])


class CommonCommands(commands.Cog):

    def __init__(self, client):
        """Initialisation client"""
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        """Return you latency"""
        User().check_user(ctx.message.author.name, str(ctx.guild.id))
        await ctx.send(f'Ping: {round(self.client.latency * 1000)}ms')

    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question):
        """8ball game"""
        User().check_user(ctx.message.author.name, str(ctx.guild.id))
        if get_language(ctx.message.author.name, str(ctx.guild.id)) == "RU":
            responses_ru = ["Бесспорно...",
                            "Предрешено...",
                            "Никаких сомнений...",
                            "Определённо да...",
                            "Можешь быть уверен в этом...",
                            "Мне кажется — «да»...",
                            "Вероятнее всего...",
                            "Хорошие перспективы...",
                            "Знаки говорят — «да»...",
                            "Да...",
                            "Пока не ясно, попробуй снова...",
                            "Спроси позже...",
                            "Лучше не рассказывать...",
                            "Сейчас нельзя предсказать...",
                            "Сконцентрируйся и спроси опять...",
                            "Даже не думай...",
                            "Мой ответ — «нет»...",
                            "По моим данным — «нет»...",
                            "Перспективы не очень хорошие...",
                            "Весьма сомнительно..."]
            await ctx.send(f'Вопрос: {question}\nОтвет: {random.choice(responses_ru)}')
        else:
            responses_en = ["It is certain...",
                            "It is decidedly so...",
                            "Without a doubt...",
                            "Yes — definitely...",
                            "You may rely on it...",
                            "As I see it, yes...",
                            "Most likely...",
                            "Outlook good...",
                            "Signs point to yes...",
                            "Yes...",
                            "Reply hazy, try again...",
                            "Ask again later...",
                            "Better not tell you now...",
                            "Cannot predict now...",
                            "Concentrate and ask again...",
                            "Don’t count on it...",
                            "My reply is no...",
                            "My sources say no...",
                            "Outlook not so good...",
                            "Very doubtful..."]
            await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses_en)}')

    @commands.command()
    async def clear(self, ctx, amount=5):
        """Clear chat"""
        User().check_user(ctx.message.author.name, str(ctx.guild.id))
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send(f"*Cleared {amount + 1} messages*")

    @commands.command()
    async def users(self, ctx):
        """Return bot users"""
        User().check_user(ctx.message.author.name, str(ctx.guild.id))

        channel = ctx.channel
        members = "".join(f'\t*{str(member)}*\n' for member in channel.members)

        if get_language(ctx.message.author.name, str(ctx.guild.id)) == "RU":
            await ctx.send(f'**Участники канала:**\n{str(members)}')
        else:
            await ctx.send(f'**Channel members:**\n{str(members)}')

    @commands.command(aliases=['wbg'])
    async def what_by_game(self, ctx):
        """Function for choice game"""
        User().check_user(ctx.message.author.name, str(ctx.guild.id))

        responses = ["Fortnite", "CS:GO", "GTAV", "GTA:SA",
                     "PUBG", "SAR", "Rust", "RDR2", "Assassin's creed",
                     "Call of Duty:Warzone", "Minecraft"]

        if get_language(ctx.message.author.name, str(ctx.guild.id)) == "RU":
            await ctx.send(f'Поиграй в {random.choice(responses)}')
        else:
            await ctx.send(f'Play to {random.choice(responses)}')

    @commands.command(aliases=['gg'])
    async def good_game(self, ctx, *, games):
        """Random choice game"""
        User().check_user(ctx.message.author.name, str(ctx.guild.id))

        if get_language(ctx.message.author.name, str(ctx.guild.id)) == "RU":
            await ctx.send(f'Поиграй в {random.choice(games.split())}')
        else:
            await ctx.send(f'Play to {random.choice(games.split())}')

    @commands.command(aliases=['wb'])
    async def white_black(self, ctx, question):
        """White/Black game"""
        User().check_user(ctx.message.author.name, str(ctx.guild.id))
        result = get_random_color()
        if question == result:
            if get_language(ctx.message.author.name, str(ctx.guild.id)) == "RU":
                await ctx.send(f'Ты выйграл ({result})')
            else:
                await ctx.send(f'You winner ({result})')
        elif get_language(ctx.message.author.name, str(ctx.guild.id)) == "RU":
            await ctx.send(f'Ты проиграл({result})')
        else:
            await ctx.send(f'You lose ({result})')

    @commands.command()
    async def help(self, ctx):
        """Return commands"""
        User().check_user(ctx.message.author.name, str(ctx.guild.id))

        if get_language(ctx.message.author.name, str(ctx.guild.id)) == "RU":
            await ctx.send('**Обычные команды**'
                           '\n\t - $8ball `question` - Предсказывающий шар'
                           '\n\t - $about - О боте'
                           '\n\t - $admin_help - Команды администратора'
                           '\n\t - $clear `Qty` - Очитить чат'
                           '\n\t - $gg `[game1 game2 ... gameN]` - Выбирает случайную игру'
                           '\n\t - $help - Команды бота'
                           '\n\t - $lang `(EN/RU)` - Устанавливает язык'
                           '\n\t - $ping - Ваш пинг'
                           '\n\t - $splash_commands - Slash-команды'
                           '\n\t - $users - Пользователи бота'
                           '\n\t - $wb `(white/black)` - Игра Черное/Белое'
                           '\n\t - $wbg - Предлагает во что поиграть')
        else:
            await ctx.send('**Common Commands**'
                           '\n\t - $8ball `question` - Ball of predictions'
                           '\n\t - $about - About bot'
                           '\n\t - $admin_help - Admin commands'
                           '\n\t - $clear `Qty` - Clear chat'
                           '\n\t - $gg `[game1 game2 ... gameN]` - Randomly chooses a game'
                           '\n\t - $help - Bot commands'
                           '\n\t - $lang `(EN/RU)` - Set language'
                           '\n\t - $ping - You ping'
                           '\n\t - $splash_commands - Slash-commands'
                           '\n\t - $users - Bot users'
                           '\n\t - $wb `(white/black)` - Game Black/White'
                           '\n\t - $wbg - Advice on what to play')

    @commands.command()
    async def slash_help(self, ctx):
        """Return slash commands"""
        User().check_user(ctx.message.author.name, str(ctx.guild.id))

        if get_language(ctx.message.author.name, str(ctx.guild.id)) == "RU":
            await ctx.send('**Slash команды**'
                           '\n\t - /8ball `question` - Предсказывающий шар'
                           '\n\t - /about - О боте'
                           '\n\t - /admin_help - Команды администратора'
                           '\n\t - /clear `Qty` - Очистить чат'
                           '\n\t - /gg `[game1 game2 ... gameN]` - Выбирает случайную игру'
                           '\n\t - /help - Команды бота'
                           '\n\t - /ping - Ваш пинг'
                           '\n\t - /splash_help - Slash-команды'
                           '\n\t - /users - Пользователи бота'
                           '\n\t - /wb `(white/black)` - Игра Черное/Белое'
                           '\n\t - /wbg - Предлагает во что поиграть')
        else:
            await ctx.send('**Slash commands**'
                           '\n\t - /8ball `question` - Ball of predictions'
                           '\n\t - /about - About bot'
                           '\n\t - /admin_help - Admin commands'
                           '\n\t - /clear `Qty` - Clear chat'
                           '\n\t - /gg `[game1 game2 ... gameN]` - Randomly chooses a game'
                           '\n\t - /help - Bot commands'
                           '\n\t - /ping - You ping'
                           '\n\t - /splash_help - Slash-commands'
                           '\n\t - /users - Bot users'
                           '\n\t - /wb `(white/black)` - Game Black/White'
                           '\n\t - /wbg - Advice on what to play')

    @commands.command()
    async def admin_help(self, ctx):
        """Return admin commands"""
        User().check_user(ctx.message.author.name, str(ctx.guild.id))

        if get_language(ctx.message.author.name, str(ctx.guild.id)) == "RU":
            await ctx.send('**Команды админа**'
                           '||\n\t - $ban `@nickname` - Заблокировать пользователя||'
                           '||\n\t - $give_role `@nickname` `role_id` - Выдать роль||'
                           '||\n\t - $nickname `@nickname` `new_nick` - Изменить никнейм||'
                           '||\n\t - $kick `@user` - Выгнать пользователя||'
                           '||\n\t - $set_role `role_id` - Установить стандартную роль||'
                           '||\n\t - $remove_role `role_id` - Убрать стандартную роль||')
        else:
            await ctx.send('**Admin Commands**'
                           '||\n\t - $ban `@nickname` - Ban user||'
                           '||\n\t - $give_role `@nickname` `role_id` - Give role||'
                           '||\n\t - $nickname `@nickname` `new_nick` - Edit nickname||'
                           '||\n\t - $kick `@user` - Kick user||'
                           '||\n\t - $set_role `role_id` - Set default role||'
                           '||\n\t - $remove_role `role_id` - Remove default role||')

    @commands.command()
    async def about(self, ctx):
        """Return bout bot"""
        User().check_user(ctx.message.author.name, str(ctx.guild.id))
        await ctx.send(f"Parzibot is free open source project, created by **@merive_#6187**.\n"
                       f"All source code is on [GitHub](https://github.com/merive/Parzibot)\n"
                       f"Parzibot, {datetime.datetime.now().year}")


def setup(client):
    """Setup function"""
    client.add_cog(CommonCommands(client))
