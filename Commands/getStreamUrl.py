import asyncio
import aiohttp
import json

class GetStreamUrl:
    @staticmethod
    async def getKBS(id):
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://cfpwwwapi.kbs.co.kr/api/v1/landing/live/channel_code/{id}') as response:
                ret = await response.json()
                return ret["channel_item"][0]["service_url"]

    @staticmethod
    async def getSBS(name):
        async with aiohttp.ClientSession() as session:
            if name == 'SBSLOVEFM':
                async with session.get('https://apis.sbs.co.kr/play-api/1.0/livestream/lovepc/lovefm?protocol=hls&ssl=Y') as response:
                    return await response.text()
            elif name == 'SBSPOWERFM':
                async with session.get('https://apis.sbs.co.kr/play-api/1.0/livestream/powerpc/powerfm?protocol=hls&ssl=Y') as response:
                    return await response.text()

    @staticmethod
    async def getMBC(name):
        async with aiohttp.ClientSession() as session:
            if name == "MBC":
                async with session.get('https://sminiplay.imbc.com/aacplay.ashx?agent=webapp&channel=sfm') as response:
                    return await response.text()
            elif name == 'MBCFM4U':
                async with session.get('https://sminiplay.imbc.com/aacplay.ashx?agent=webapp&channel=mfm') as response:
                    return await response.text()
