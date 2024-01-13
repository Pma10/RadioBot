import discord

class RadioEmbed:
    def EmbedRadio(name):
        return discord.Embed(title=f'📻︎ {name}',description=f"{name} 라디오를 실행했어요!",color=0xbff5e2)