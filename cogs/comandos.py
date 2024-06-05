import discord
from discord.ext import commands
import variables
import datetime

class Comandos(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def lobby(self, ctx, canal: discord.abc.GuildChannel):
        if isinstance(canal, discord.TextChannel):
            embed = discord.Embed(title="El canal especificado no existe o no es un canal de voz.", color=discord.Color.red())
            await ctx.send(embed=embed)
        elif isinstance(canal, discord.VoiceChannel):
            variables.lobby_id = canal.id
            embed = discord.Embed(title="Nuevo canal asignado como lobby.", color=discord.Color.green())
            embed.add_field(name="Nombre:", value=canal.name)
            embed.add_field(name="ID:", value=canal.id)
            await ctx.send(embed=embed)
            print("\033[36m" + "LOBBY " + "\033[0m" f"[{variables.fecha_actual}] Se ha asignado el canal `{canal}` con id `{canal.id}` como lobby.")
        else:
            await ctx.send(f'El canal {canal.mention} no es ni de voz ni de texto')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def log_eliminados(self, ctx, canal: discord.abc.GuildChannel):
        if isinstance(canal, discord.TextChannel):
            variables.log_eliminados = canal.id
            embed = discord.Embed(title="Nuevo canal asignado para log de mensajes eliminados.", color=discord.Color.green())
            embed.add_field(name="Nombre:", value=canal.name)
            embed.add_field(name="ID:", value=canal.id)
            await ctx.send(embed=embed)
            print("\033[36m" + "LOG ELIMINADOS " + "\033[0m" f"[{variables.fecha_actual}] Se ha asignado el canal `{canal}` con id `{canal.id}` para log de mensajes eliminados.")
        else:
            embed = discord.Embed(title="El canal especificado no es un canal de texto.", color=discord.Color.red())
            await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def log_editados(self, ctx, canal: discord.abc.GuildChannel):
        if isinstance(canal, discord.TextChannel):
            variables.log_editados = canal.id
            embed = discord.Embed(title="Nuevo canal asignado para log de mensajes editados.", color=discord.Color.green())
            embed.add_field(name="Nombre:", value=canal.name)
            embed.add_field(name="ID:", value=canal.id)
            await ctx.send(embed=embed)
            print("\033[36m" + "LOG EDITADOS " + "\033[0m" f"[{variables.fecha_actual}] Se ha asignado el canal `{canal}` con id `{canal.id}` para log de mensajes editados.")
        else:
            embed = discord.Embed(title="El canal especificado no es un canal de texto.", color=discord.Color.red())
            await ctx.send(embed=embed)


    #Comando para detener el bot (SOLO ADMINS)
    @commands.command(name='stop')
    @commands.has_permissions(administrator=True)
    async def stop(self, ctx):
        #Guarda el log en el archivo de logs
        with open("logs/logLogin.txt", "a") as archivo:
            print(f'[{variables.fecha_actual}] Desconectado de Discord como {self.bot.user}', file=archivo)
        print("\033[31m" + "# " + "\033[0m" f'[{variables.fecha_actual}] Sesión finaliza como {self.bot.user}')

        #Recoge el canal en el que se ha ejecutado el comando
        #Luego muestra el mensaje de desconexion y desconecta el bot
        admin_channel=ctx.channel
        embed = discord.Embed(title="Mini Sanz desconectado.", color=discord.Color.red())
        embed.set_footer(text=f'[{variables.fecha_actual}]')
        await admin_channel.send(embed=embed)
        await self.bot.close()

    @commands.command(name='sincronizar')
    @commands.has_permissions(administrator=True)
    async def sincronizar(self, ctx):
        try:
            # Sincroniza los comandos con el árbol de comandos del bot
            synced = await ctx.bot.tree.sync()
        
            # Crea un embed para notificar la sincronización exitosa
            embed = discord.Embed(
                title="Slash commands sincronizados",
                description=f"Se han sincronizado {len(synced)} comandos.",
                color=discord.Color.blue()
            )
            embed.set_footer(text=f'[{variables.fecha_actual}]')
            await ctx.send(embed=embed)
        except Exception as e:
            # En caso de error, envía un mensaje con la descripción del error
            embed = discord.Embed(
                title="Error al sincronizar",
                description=str(e),
                color=discord.Color.red()
            )
            embed.set_footer(text=f'[{variables.fecha_actual}]')
            await ctx.send(embed=embed)


    #Errores de permisos de ejecuccion
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(title="No tiene permisos para ejecutar este comando.", color=discord.Color.red())
            await ctx.send(embed=embed)
            print("\033[31m" + "PERMISOS " + "\033[0m" f"[{variables.fecha_actual}] El usuario {ctx.author.name} ejecutó el comando {ctx.command.name} sin exito.")

