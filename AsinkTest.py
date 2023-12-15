import asyncio
import pytest
import aiohttp
import aiopg
#1
async def promice():
    return "Horosho"
@pytest.mark.acsynco
async def event_loop():
    result = await promice()
    assert result == "Ne Horosho"
asyncio.run(event_loop())

#2
async def promice(x, y):
    return x / y
@pytest.mark.acsynco 
async def event_loop():
     with pytest.raises(TypeError):
        result = await promice(10, "a")
asyncio.run(event_loop())

#3

async def Errorecode(code):
    url = f"https://http.cat/{code}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return code
@pytest.mark.asyncio
async def event_loop():
    code = await Errorecode(102)
    assert code == 102
asyncio.run(event_loop())

#5

async def aaaa(x):
     return operation(x)
async def operation(x):
    return x * x

@pytest.mark.asyncio
async def event_loop():
    result = await operation(10)
    assert result == 100
asyncio.run(event_loop())