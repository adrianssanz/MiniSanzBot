import discord
from discord import interactions
from discord.ext import commands
import cogs.comandos
import cogs.eventos
import cogs.comandosBarra
import variables


# Habilitar los intents necesarios
intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix='!', help_command=None, intents=intents)

@bot.event
async def on_ready():
    guilds = len(bot.guilds)
    # Escribir en el archivo utilizando la sentencia with
    with open("logs/logLogin.txt", "a") as archivo:
        print(f'[{variables.fecha_actual}] Conectado a Discord como {bot.user} en {guilds} servidor/es', file=archivo)

    await bot.change_presence(activity=discord.Game(
    name='/ayuda'))

    await bot.tree.sync()

    print("\033[32m" + "# " + "\033[0m" f'[{variables.fecha_actual}] Sesión iniciada como {bot.user} en {guilds} servidor/es')
    await bot.add_cog(cogs.comandos.Comandos(bot))
    await bot.add_cog(cogs.eventos.Eventos(bot))
    await bot.add_cog(cogs.comandosBarra.ComandosBarra(bot))


bot.run(variables.token)
