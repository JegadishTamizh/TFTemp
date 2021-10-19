#!/usr/bin/env python3

# -*- coding: utf-8 -*-

# @trojanzhex

from helpers.tools import execute, clean_up

from helpers.upload import upload_audio, upload_subtitle

async def extract_audio(client, message, data):

    await message.edit_text("Extracting Stream from file...")

    dwld_loc = data['location']

    out_loc = data['location']

    if data['name'] == "opus":

        out, err, rcode, pid = await execute(f"ffmpeg -i '{dwld_loc}' -map 0:{data['map']} -c copy '{out_loc}' + '.opus' -y")

        if rcode != 0:

            await message.edit_text("**Error Occured. See Logs for more info.**")

            print(err)

            await clean_up(dwld_loc, out_loc)

            return

    if data['name'] == "aac":

        out, err, rcode, pid = await execute(f"ffmpeg -i '{dwld_loc}' -map 0:{data['map']} -c copy '{out_loc}.aac' -y")

        if rcode != 0:

            await message.edit_text("**Error Occured. See Logs for more info.**")

            print(err)

            await clean_up(dwld_loc, out_loc)

            return

    if data['name'] == "ac3":

        out, err, rcode, pid = await execute(f"ffmpeg -i '{dwld_loc}' -map 0:{data['map']} -c copy '{out_loc}.ac3' -y")

        if rcode != 0:

            await message.edit_text("**Error Occured. See Logs for more info.**")

            print(err)

            await clean_up(dwld_loc, out_loc)

            return

    if data['name'] == "eac3":

        out, err, rcode, pid = await execute(f"ffmpeg -i '{dwld_loc}' -map 0:{data['map']} -c copy '{out_loc}.eac3' -y")

        if rcode != 0:

            await message.edit_text("**Error Occured. See Logs for more info.**")

            print(err)

            await clean_up(dwld_loc, out_loc)

            return            

    else:

        out, err, rcode, pid = await execute(f"ffmpeg -i '{dwld_loc}' -map 0:{data['map']} '{out_loc}.mp3' -y")

        if rcode != 0:

            await message.edit_text("**Error Occured. See Logs for more info.**")

            print(err)

            await clean_up(dwld_loc, out_loc)

            return

    await clean_up(dwld_loc)

    await upload_audio(client, message, out_loc)

async def extract_subtitle(client, message, data):

    await message.edit_text("Extracting Stream from file")

    dwld_loc = data['location']

    out_loc = data['location'] + ".srt"   

    out, err, rcode, pid = await execute(f"ffmpeg -i '{dwld_loc}' -map 0:{data['map']} '{out_loc}' -y")

    if rcode != 0:

        await message.edit_text("**Error Occured. See Logs for more info.**")

        print(err)

        await clean_up(dwld_loc, out_loc)

        return

    await clean_up(dwld_loc)  

    await upload_subtitle(client, message, out_loc)

    

