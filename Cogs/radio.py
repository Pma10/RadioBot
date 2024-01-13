import os
import discord
from Commands.getStreamUrl import GetStreamUrl
from Embed.radioEmbed import RadioEmbed
from discord.ext import commands
from discord.commands import Option, SlashCommandGroup
from discord import FFmpegPCMAudio

class Radio(commands.Cog):
    def __init__(self, app):
        self.app = app
        self.KBSCH = {
            "KBS1" : "21",
            "KBS2" : "22",
            "KBS3" : "23",
            "KBS1FM" : "24",
            "KBS2FM" : "25"
        }
    RADIO = SlashCommandGroup(name='라디오', description='라디오를 들을 수 있도록 해주는 명령어에요!')
 
    @RADIO.command(name='듣기')
    async def _듣기(self, ctx, 채널: Option(str, "듣고 싶은 채널을 선택해주세요!", choices=['KBS1',"KBS2","KBS3",'KBS1FM',"KBS2FM","SBSLOVEFM","SBSPOWERFM","MBC","MBCFM4U"])):
        await ctx.defer()
        voiceCh = ctx.author.voice
        voiceClient = ctx.voice_client

        if voiceClient is None:
            if voiceCh:
                voiceClient = await voiceCh.channel.connect()
            else:
                return await ctx.respond(':exclamation: 음성채널에 접속한 뒤 실행해주세요',ephemeral = True)

        elif voiceClient.is_playing():
            voiceClient.stop()

        if 'KBS' in 채널:
            radioUrl = await GetStreamUrl.getKBS(self.KBSCH[채널])
        elif 'SBS' in 채널:
            radioUrl = await GetStreamUrl.getSBS(채널)
        elif "MBC" in 채널:
            radioUrl = await GetStreamUrl.getMBC(채널)
            
        voiceClient.play(FFmpegPCMAudio(radioUrl, executable="C:\\WorkDesktop\\Py\\discord\\RadioBot\\ffmpeg\\bin\\ffmpeg.exe"))
        embed = RadioEmbed.EmbedRadio(채널)
        return await ctx.respond(embed=embed)
        
    @RADIO.command(name='나가기')
    async def _나가기(self, ctx):
        voiceCh = ctx.author.voice
        voiceClient = ctx.voice_client
        if voiceCh is False:
            return await ctx.respond("음성채널에 접속한뒤 사용해주세요" , ephemeral = True)
        if voiceClient:
            await voiceClient.disconnect()
            return await ctx.respond('라디오 봇이 음성 채널에서 나갔습니다.', ephemeral = True)
        else:
            return await ctx.respond(':exclamation: 라디오 봇이 음성 채널에 접속해 있지 않습니다.', ephemeral = True)
def setup(app):
    app.add_cog(Radio(app))
    print('[RADIO] Cogs Loaded')
