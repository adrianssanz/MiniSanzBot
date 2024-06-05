from discord.ext import commands
import discord
import variables
import asyncio

class Eventos(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Log mensajes borrados
    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.author.bot:
            return  # Si el autor del mensaje es un bot, no hace nada.
        
        log_channel = self.bot.get_channel(variables.log_eliminados)
        if log_channel:
            embed = discord.Embed(
                title="Mensaje Eliminado",
                description=f"Mensaje de {message.author} en {message.channel.mention} ha sido eliminado.",
                color=discord.Color.red()
            )
            embed.add_field(name="Contenido:", value=message.content)
            embed.set_footer(text=f'[{variables.fecha_actual}]')
            await log_channel.send(embed=embed)

    # Log mensajes editados
    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if before.author.bot:
            return  # Si el autor del mensaje es un bot, no hace nada.
        
        log_channel = self.bot.get_channel(variables.log_editados)
        if log_channel:
            embed = discord.Embed(
                title="Mensaje Editado",
                description=f"Mensaje de {before.author} en {before.channel.mention} ha sido editado.",
                color=discord.Color.blue()
            )
            embed.add_field(name="Antes:", value=before.content)
            embed.add_field(name="Después:", value=after.content)
            embed.set_footer(text=f'[{variables.fecha_actual}]')
            await log_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if after.channel and after.channel.id == variables.lobby_id:
            category = after.channel.category
            count = len(category.voice_channels) + 1
            channel_name = f"#{count-1} - Canal de {member.name}"
            voice_channel = await category.guild.create_voice_channel(channel_name, category=category)
            with open("logs/logCanales.txt", "a") as archivo:
                print(f"[{variables.fecha_actual}] Canal creado: {channel_name}")
            print("\033[32m" + "# " + "\033[0m" f"[{variables.fecha_actual}] Canal creado: {channel_name}")
            await member.move_to(voice_channel)

            def check_empty(channel):
                return len(channel.members) == 0

            while not check_empty(voice_channel):
                await asyncio.sleep(5)

            await voice_channel.delete()
            with open("logs/logCanales.txt", "a") as archivo:
                print(f"[{variables.fecha_actual}] Canal borrado: {channel_name}")
            print("\033[31m" + "CANAL " + "\033[0m" f"[{variables.fecha_actual}] Canal borrado: {channel_name}")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        # Agrega aquí tus eventos personalizados

