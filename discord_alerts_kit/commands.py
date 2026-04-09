import discord
from discord import app_commands

def setup_commands(bot):
    tree = app_commands.CommandTree(bot)

    @tree.command(name="subscribe", description="S'abonner aux alertes en DM")
    async def subscribe(interaction: discord.Interaction):
        bot.subscribe(interaction.user.id)
        await interaction.response.send_message(
            "✅ Tu es maintenant abonné aux alertes !", ephemeral=True
        )

    @tree.command(name="unsubscribe", description="Se désabonner des alertes")
    async def unsubscribe(interaction: discord.Interaction):
        bot.unsubscribe(interaction.user.id)
        await interaction.response.send_message(
            "❌ Tu es maintenant désabonné des alertes.", ephemeral=True
        )

    @tree.command(name="status", description="Voir le statut du bot")
    async def status(interaction: discord.Interaction):
        count = len(bot.subscribers)
        sources = len(bot._alert_sources)
        await interaction.response.send_message(
            f"📊 **Status**\n👥 Subscribers : {count}\n🔌 Sources actives : {sources}",
            ephemeral=True
        )

    return tree