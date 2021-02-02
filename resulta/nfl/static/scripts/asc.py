import asyncio
import json


async def fetch(session, url):
    async with session.get(url) as response:
        resp = await response.json()
        print('1', resp)
        return resp

async def fetch_all(urls):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(
                fetch(
                    session,
                    url,
                )
            )
        responses = await asyncio.gather(*tasks, return_exceptions=True)
        
        return responses

def run(urls):
    responses = await fetch_all(urls)
    return responses
        
