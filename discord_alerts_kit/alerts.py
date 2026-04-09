import discord
from discord.ext import tasks
from .embed import build_embed
from .config import load_config
from .storage import is_duplicate, mark_sent
from .commands import setup_commands

class AlertBot(discord.Client):
    def __init__(self, config_path="config.yaml"):
        intents = discord.Intents.default()
        intents.members = True
        super().__init__(intents=intents)
        self.config = load_config(config_path)
        self.subscribers = set()
        self._alert_sources = []
        self.tree = setup_commands(self)

    def add_source(self, func):
        self._alert_sources.append(func)
        return func

    async def setup_hook(self):
        await self.tree.sync()
        print("✅ Commandes slash synchronisées")

    async def on_ready(self):
        print(f"✅ Connecté en tant que {self.user}")
        self.alert_loop.start()

    @tasks.loop(minutes=10)
    async def alert_loop(self):
        channel_id = self.config.get("alert_channel")
        if not channel_id:
            return
        channel = self.get_channel(int(channel_id))
        if not channel:
            return
        for source in self._alert_sources:
            try:
                if discord.utils.is_coroutine_function(source):
                    alerts = await source()
                else:
                    alerts = source()
                for alert in alerts:
                    if is_duplicate(alert):
                        continue
                    embed = build_embed(
                        title=alert.get("title", "Alerte"),
                        description=alert.get("description", ""),
                        url=alert.get("url"),
                        color=self.config.get("color", 0x00ff00),
                        footer=alert.get("footer")
                    )
                    await channel.send(embed=embed)
                    mark_sent(alert)
                    if self.config.get("dm_subscribers"):
                        for user_id in self.subscribers:
                            user = await self.fetch_user(user_id)
                            if user:
                                await user.send(embed=embed)
            except Exception as e:
                print(f"❌ Erreur source {source.__name__}: {e}")

    def subscribe(self, user_id):
        self.subscribers.add(user_id)

    def unsubscribe(self, user_id):
        self.subscribers.discard(user_id)

    def run_bot(self):
        self.run(self.config.get("token"))