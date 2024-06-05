import discord
from discord import app_commands
from discord.ext import commands
import variables
import random
# import interactions

class ComandosBarra(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #Comando en barra de musica
    @app_commands.command(name="musica", description="Comandos de musica.")
    async def musica(self, interaction: discord.Interaction):
        embed = discord.Embed(title="COMANDOS MUSICA :notes:",
                          description="",
                          color=0x00ff00)
        embed.add_field(name="+play",
                    value="Reproducir una canción.",
                    inline=False)
        embed.add_field(name="+pause", value="Pausar una canción.", inline=False)
        embed.add_field(name="+resume",
                    value="Reanudar una canción.",
                    inline=False)
        embed.add_field(name="+skip", value="Siguiente canción.", inline=False)
        embed.add_field(name="+queue",
                    value="Consultar la lista de reproducción.",
                    inline=False)
        embed.add_field(name="+skip",
                    value="Siguiente canción en la lista.",
                    inline=False)
        embed.add_field(name="+leave",
                    value="Sacar al bot de la sala.",
                    inline=False)
        embed.add_field(name="+clear",
                    value="Limpiar la lista de reproducción.",
                    inline=False)
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @app_commands.command(name="hola", description="Saluda a Mini Sanz.")
    async def hola(self, interaction: discord.Interaction):
        await interaction.response.send_message(f'Hola {interaction.user.mention}, soy Mini Sanz, no soy una IA extraordinaria,' f' solo soy un bot común sin ideas simples!', ephemeral=True)

    @app_commands.command(name="dado", description="Tira un dado!🎲")
    async def dado(self, interaction: discord.Interaction):
        await interaction.response.send_message(f'{random.randint(1,6)}🎲')
    
    @app_commands.command(name="ayuda", description="Obten los comandos de Mini Sanz")
    async def ayuda(self, interaction: discord.Interaction):
        embed=discord.Embed(title="Comandos de Mini Sanz", description="Estos son todos los comandos disponibles:", color=0x00ff00)
        embed.add_field(name="/hola", value="Saluda a Mini Sanz! ", inline=True)
        embed.add_field(name="/musica", value="Consulta los comandos del bot de musica. ", inline=True)
        embed.add_field(name="/dado", value="Tira un dado y obten un numero. 🎲", inline=True)
        embed.add_field(name="/moneda", value="Tira una moneda y obten cara o cruz. ", inline=True)
        embed.add_field(name="!lobby* [channelId]", value="Asigna el canal que actuará como lobby para los canales temporales.", inline=False)
        embed.add_field(name="!log_editados* [channelId]", value="Asigna el canal que actuará como log para los mensajes editados.", inline=False)
        embed.add_field(name="!log_eliminados* [channelId]", value="Asigna el canal que actuará como log para los mensajes eliminados.", inline=False)
        embed.set_footer(text="*Estos comandos solo los podrá ejecutar un administrador.")
        await interaction.response.send_message(embed=embed, ephemeral=True)
        
    @app_commands.command(name="moneda", description="Tira una moneda!🪙")
    async def moneda(self, interaction: discord.Interaction):
        resultado = None
        if random.random() > 0.5:
            resultado = (f'Ha salido cara! 🪙')
        else:
            resultado = (f'Ha salido cruz! 🪙')
        
        await interaction.response.send_message(resultado)