from . import discord as discord

class NotifyGuilded(discord.NotifyDiscord):
    """A wrapper to Guilded Notifications."""
    service_name: str
    service_url: str
    setup_url: str
    secure_protocol: str
    notify_url: str
    @staticmethod
    def parse_native_url(url):
        """
        Support https://media.guilded.gg/webhooks/WEBHOOK_ID/WEBHOOK_TOKEN
        """
