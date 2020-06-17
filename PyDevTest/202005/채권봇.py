# -*- coding: utf-8 -*-
import asyncio
import discord
import pandas as pd
import requests
import json
import time
import datetime
from bs4 import BeautifulSoup as bs

client = discord.Client()
bond_linkA = 'https://archeage.xlgames.com/play/worldinfo/EANNA'
bond_linkB = 'https://archeage.xlgames.com/play/worldinfo/NUI'
bond_linkC = 'https://archeage.xlgames.com/play/worldinfo/ORCHIDNA'
bond_linkD = 'https://archeage.xlgames.com/play/worldinfo/HAJE'
bond_linkE = 'https://archeage.xlgames.com/play/worldinfo/DAMIAN'
bond_linkF = 'https://archeage.xlgames.com/play/worldinfo/GARDEN'
bond_linkG = 'https://archeage.xlgames.com/play/worldinfo/GARDEN2'

list_cloth = [
    '마리아노플',
    '릴리엇 구릉지',
    '두 왕관',
    '황금 평원',
    '무지개 벌판',
    '매사냥 고원'
    ]

list_leath = [
    '뼈의 땅',
    '태초의 요람',
    '긴 모래톱',
    '하늬 마루',
    '마하데비',
    '노래의 땅',
    '초원의 띠',
    '로카의 장기말들'
    ]

list_wood = [
    '그위오니드 숲',
    '솔즈리드 반도',
    '하얀 숲',
    '지옥 늪지대',
    '하리하랄라야의 폐허',
    '이니스테르',
    '하슬라',
    '고대의 숲'
    ]

list_iron = [
    '가랑돌 평원',
    '청동 바위산',
    '십자별 평원',
    '동틀녘 반도',
    '불볕 황야',
    '호랑이 등뼈 산맥',
    '로칼로카 산맥'
    ]

def bond_message(bond_list):
    str1 = '옷감: '
    str2 = '가죽: '
    str3 = '목재: '
    str4 = '철 주괴: '
    for a in bond_list:
        for b in list_cloth:
            if a == b:
                str1 += a + ' '
        for b in list_leath:
            if a == b:
                str2 += a + ' '
        for b in list_wood:
            if a == b:
                str3 += a + ' '
        for b in list_iron:
            if a == b:
                str4 += a + ' '
    return str1 + '\n' + str2 + '\n' + str3 + '\n' +str4

def html(url):
    with requests.Session() as s:
            p = s.get(url, verify=False)
            html = p.text
            soup = bs(html, 'html.parser')
            return soup


def bond_get(soup, case):
    sentence = ""
    list_20 = []
    list_60 = []
    list_100 = []
    for a in range(1, 3):
        for b in range(1, 5): 
            bond_full = soup.select('#container-common > div > div > div > div.bond-info > (' + str(a) + ') > tbody > ('+str(b)+') > td > ul')
            sentence += bond_full[0].text.strip()
            sentence += '\n'
    bond_list = sentence.split('\n')
    bond_list.remove('')

    for i in bond_list:
        text = i.split(': ')


        if text[1] == '20개':
            list_20.append(text[0])
            
        if text[1] == '60개':
            list_60.append(text[0])
            
        if text[1] == '100개':
            list_100.append(text[0])
            

    if case == '1':
        return list_20
    if case == '2':
        return list_60
    if case == '3':
        return list_100

"""
bond_get(html(bond_linkA, bond_linkB, bond_linkC, bond_linkD, bond_linkE))
print(bond_message(bond_lis))
"""



@client.event
async def on_ready():
    print("Logged in as ") 
    print(client.user.name)
    print(client.user.id)
    print("===========")
    await client.change_presence(activity=discord.Game(name="일", type=1))


@client.event   
async def on_message(message):
    if message.content.startswith("!에안나 20"):        #에안나
        channel = message.channel
        def is_me(m):
            return m.author == message.author
        deleted = await channel.purge(limit = 1, check=is_me)
        sentence = bond_message(bond_get(html(bond_linkA), '1'))
        print(bond_message(bond_get(html(bond_linkA), '1')))
        title = '에안나 채권 20개 현황'
        description = sentence
        embed = discord.Embed(title=title, description=description, color=0x00ff00)
        embed.set_footer(text = '에안나' + str(datetime.date.today()) + ' 기준')
        await message.channel.send(embed=embed)

    if message.content.startswith("!에안나 60"):
        channel = message.channel
        def is_me(m):
            return m.author == message.author
        deleted = await channel.purge(limit = 1, check=is_me)
        sentence = bond_message(bond_get(html(bond_linkA), '2'))
        print(bond_message(bond_get(html(bond_linkA), '2')))
        title = '에안나 채권 60개 현황'
        description = sentence
        embed = discord.Embed(title=title, description=description, color=0x00ff00)
        embed.set_footer(text = '에안나 ' + str(datetime.date.today()) + ' 기준')
        await message.channel.send(embed=embed)

    if message.content.startswith("!에안나 100"):
        channel = message.channel
        def is_me(m):
            return m.author == message.author
        deleted = await channel.purge(limit = 1, check=is_me)
        sentence = bond_message(bond_get(html(bond_linkA), '3'))
        print(bond_message(bond_get(html(bond_linkA), '3')))
        title = '에안나 채권 100개 현황'
        description = sentence
        embed = discord.Embed(title=title, description=description, color=0x00ff00)
        embed.set_footer(text = '에안나 ' + str(datetime.date.today()) + ' 기준')
        await message.channel.send(embed=embed)


    if message.content.startswith("!누이 20"):            #누이
        channel = message.channel
        def is_me(m):
            return m.author == message.author
        deleted = await channel.purge(limit = 1, check=is_me)
        sentence = bond_message(bond_get(html(bond_linkB), '1'))
        print(bond_message(bond_get(html(bond_linkB), '1')))
        title = '누이 채권 20개 현황'
        description = sentence
        embed = discord.Embed(title=title, description=description, color=0x00ff00)
        embed.set_footer(text = '누이 ' + str(datetime.date.today()) + ' 기준')
        await message.channel.send(embed=embed)

    if message.content.startswith("!누이 60"):
        channel = message.channel
        def is_me(m):
            return m.author == message.author
        deleted = await channel.purge(limit = 1, check=is_me)
        sentence = bond_message(bond_get(html(bond_linkB), '2'))
        print(bond_message(bond_get(html(bond_linkB), '2')))
        title = '누이 채권 60개 현황'
        description = sentence
        embed = discord.Embed(title=title, description=description, color=0x00ff00)
        embed.set_footer(text = '누이 ' + str(datetime.date.today()) + ' 기준')
        await message.channel.send(embed=embed)

    if message.content.startswith("!누이 100"):
        channel = message.channel
        def is_me(m):
            return m.author == message.author
        deleted = await channel.purge(limit = 1, check=is_me)
        sentence = bond_message(bond_get(html(bond_linkB), '3'))
        print(bond_message(bond_get(html(bond_linkB), '3')))
        title = '누이 채권 100개 현황'
        description = sentence
        embed = discord.Embed(title=title, description=description, color=0x00ff00)
        embed.set_footer(text = '누이 ' + str(datetime.date.today()) + ' 기준')
        await message.channel.send(embed=embed)
    

    if message.content.startswith("!오키드나 20"):      #오키드나
        channel = message.channel
        def is_me(m):
            return m.author == message.author
        deleted = await channel.purge(limit = 1, check=is_me)
        sentence = bond_message(bond_get(html(bond_linkC), '1'))
        print(bond_message(bond_get(html(bond_linkC), '1')))
        title = '오키드나 채권 20개 현황'
        description = sentence
        embed = discord.Embed(title=title, description=description, color=0x00ff00)
        embed.set_footer(text = '오키드나 ' + str(datetime.date.today()) + ' 기준')
        await message.channel.send(embed=embed)

    if message.content.startswith("!오키드나 60"):            
        channel = message.channel
        def is_me(m):
            return m.author == message.author
        deleted = await channel.purge(limit = 1, check=is_me)
        sentence = bond_message(bond_get(html(bond_linkC), '2'))
        print(bond_message(bond_get(html(bond_linkC), '2')))
        title = '오키드나 채권 60개 현황'
        description = sentence
        embed = discord.Embed(title=title, description=description, color=0x00ff00)
        embed.set_footer(text = '오키드나 ' + str(datetime.date.today()) + ' 기준')
        await message.channel.send(embed=embed)

    if message.content.startswith("!오키드나 100"):
        channel = message.channel
        def is_me(m):
            return m.author == message.author
        deleted = await channel.purge(limit = 1, check=is_me)
        sentence = bond_message(bond_get(html(bond_linkC), '3'))
        print(bond_message(bond_get(html(bond_linkC), '3')))
        title = '오키드나 채권 100개 현황'
        description = sentence
        embed = discord.Embed(title=title, description=description, color=0x00ff00)
        embed.set_footer(text = '오키드나 ' + str(datetime.date.today()) + ' 기준')
        await message.channel.send(embed=embed)



    if message.content.startswith("!하제 20"):      #하제
        channel = message.channel
        def is_me(m):
            return m.author == message.author
        deleted = await channel.purge(limit = 1, check=is_me)
        sentence = bond_message(bond_get(html(bond_linkD), '1'))
        print(bond_message(bond_get(html(bond_linkD), '1')))
        title = '하제 채권 20개 현황'
        description = sentence
        embed = discord.Embed(title=title, description=description, color=0x00ff00)
        embed.set_footer(text = '하제 ' + str(datetime.date.today()) + ' 기준')
        await message.channel.send(embed=embed)

    if message.content.startswith("!하제 60"):            
        channel = message.channel
        def is_me(m):
            return m.author == message.author
        deleted = await channel.purge(limit = 1, check=is_me)
        sentence = bond_message(bond_get(html(bond_linkD), '2'))
        print(bond_message(bond_get(html(bond_linkD), '2')))
        title = '하제 채권 60개 현황'
        description = sentence
        embed = discord.Embed(title=title, description=description, color=0x00ff00)
        embed.set_footer(text = '하제 ' + str(datetime.date.today()) + ' 기준')
        await message.channel.send(embed=embed)

    if message.content.startswith("!하제 100"):
        channel = message.channel
        def is_me(m):
            return m.author == message.author
        deleted = await channel.purge(limit = 1, check=is_me)
        sentence = bond_message(bond_get(html(bond_linkD), '3'))
        print(bond_message(bond_get(html(bond_linkD), '3')))
        title = '하제 채권 100개 현황'
        description = sentence
        embed = discord.Embed(title=title, description=description, color=0x00ff00)
        embed.set_footer(text = '하제 ' + str(datetime.date.today()) + ' 기준')
        await message.channel.send(embed=embed)




    if message.content.startswith("!다미안 20"):     #다미안
        channel = message.channel
        def is_me(m):
            return m.author == message.author
        deleted = await channel.purge(limit = 1, check=is_me)
        sentence = bond_message(bond_get(html(bond_linkE), '1'))
        print(bond_message(bond_get(html(bond_linkE), '1')))
        title = '다미안 채권 20개 현황'
        description = sentence
        embed = discord.Embed(title=title, description=description, color=0x00ff00)
        embed.set_footer(text = '다미안 ' + str(datetime.date.today()) + ' 기준')
        await message.channel.send(embed=embed)

    if message.content.startswith("!다미안 60"):            
        channel = message.channel
        def is_me(m):
            return m.author == message.author
        deleted = await channel.purge(limit = 1, check=is_me)
        sentence = bond_message(bond_get(html(bond_linkE), '2'))
        print(bond_message(bond_get(html(bond_linkE), '2')))
        title = '다미안 채권 60개 현황'
        description = sentence
        embed = discord.Embed(title=title, description=description, color=0x00ff00)
        embed.set_footer(text = '다미안 ' + str(datetime.date.today()) + ' 기준')
        await message.channel.send(embed=embed)

    if message.content.startswith("!다미안 100"):
        channel = message.channel
        def is_me(m):
            return m.author == message.author
        deleted = await channel.purge(limit = 1, check=is_me)
        sentence = bond_message(bond_get(html(bond_linkE), '3'))
        print(bond_message(bond_get(html(bond_linkE), '3')))
        title = '다미안 채권 100개 현황'
        description = sentence
        embed = discord.Embed(title=title, description=description, color=0x00ff00)
        embed.set_footer(text = '다미안 ' + str(datetime.date.today()) + ' 기준')
        await message.channel.send(embed=embed)


    if message.content.startswith("!정원 20"):      #정원
        channel = message.channel
        def is_me(m):
            return m.author == message.author
        deleted = await channel.purge(limit = 1, check=is_me)
        sentence = bond_message(bond_get(html(bond_linkF), '1'))
        print(bond_message(bond_get(html(bond_linkF), '1')))
        title = '정원 채권 20개 현황'
        description = sentence
        embed = discord.Embed(title=title, description=description, color=0x00ff00)
        embed.set_footer(text = '정원 ' + str(datetime.date.today()) + ' 기준')
        await message.channel.send(embed=embed)

    if message.content.startswith("!정원 60"):            
        channel = message.channel
        def is_me(m):
            return m.author == message.author
        deleted = await channel.purge(limit = 1, check=is_me)
        sentence = bond_message(bond_get(html(bond_linkF), '2'))
        print(bond_message(bond_get(html(bond_linkF), '2')))
        title = '정원 채권 60개 현황'
        description = sentence
        embed = discord.Embed(title=title, description=description, color=0x00ff00)
        embed.set_footer(text = '정원 ' + str(datetime.date.today()) + ' 기준')
        await message.channel.send(embed=embed)

    if message.content.startswith("!정원 100"):
        channel = message.channel
        def is_me(m):
            return m.author == message.author
        deleted = await channel.purge(limit = 1, check=is_me)
        sentence = bond_message(bond_get(html(bond_linkF), '3'))
        print(bond_message(bond_get(html(bond_linkF), '3')))
        title = '정원 채권 100개 현황'
        description = sentence
        embed = discord.Embed(title=title, description=description, color=0x00ff00)
        embed.set_footer(text = '정원 ' + str(datetime.date.today()) + ' 기준')
        await message.channel.send(embed=embed)

@client.event   
async def on_message(message):
    if message.content.startswith("!정원2 20"):        #정원2
        channel = message.channel
        def is_me(m):
            return m.author == message.author
        deleted = await channel.purge(limit = 1, check=is_me)
        sentence = bond_message(bond_get(html(bond_linkG), '1'))
        print(bond_message(bond_get(html(bond_linkG), '1')))
        title = '정원2 채권 20개 현황'
        description = sentence
        embed = discord.Embed(title=title, description=description, color=0x00ff00)
        embed.set_footer(text = '정원2' + str(datetime.date.today()) + ' 기준')
        await message.channel.send(embed=embed)

    if message.content.startswith("!정원2 60"):
        channel = message.channel
        def is_me(m):
            return m.author == message.author
        deleted = await channel.purge(limit = 1, check=is_me)
        sentence = bond_message(bond_get(html(bond_linkG), '2'))
        print(bond_message(bond_get(html(bond_linkG), '2')))
        title = '정원2 채권 60개 현황'
        description = sentence
        embed = discord.Embed(title=title, description=description, color=0x00ff00)
        embed.set_footer(text = '정원2 ' + str(datetime.date.today()) + ' 기준')
        await message.channel.send(embed=embed)

    if message.content.startswith("!정원2 100"):
        channel = message.channel
        def is_me(m):
            return m.author == message.author
        deleted = await channel.purge(limit = 1, check=is_me)
        sentence = bond_message(bond_get(html(bond_linkG), '3'))
        print(bond_message(bond_get(html(bond_linkG), '3')))
        title = '정원2 채권 100개 현황'
        description = sentence
        embed = discord.Embed(title=title, description=description, color=0x00ff00)
        embed.set_footer(text = '정원2 ' + str(datetime.date.today()) + ' 기준')
        await message.channel.send(embed=embed)
   
        
client.run(token)

