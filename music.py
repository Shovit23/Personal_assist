import os
import assistance_details as ad
import file_search

music_path = "/root/"


def play_music():
    if ad.is_linux():
        os.system("rhythmbox-client --play")
        return "Playing Music from local"

    else:
        return "can't play right now"


def pause_music():
    if ad.is_linux():
        os.system("rhythmbox-client --pause")
        return "Music Paused"

    else:
        return "can't play right now"

def stop_music():
    if ad.is_linux():
        os.system("rhythmbox-client --stop")
        return "Music Stopped"

    else:
        return "can't play right now"

def next_music():
    if ad.is_linux():
        os.system("rhythmbox-client --next")
        return "Playing Next song" 

    else:
        return "can't play right now"

def specfic_music(song):
    song = song.replace('play','')
    if ad.is_linux():
        file_search.set_root(music_path)
        songs = file_search.searchFile(song)
        try:
            song_uri = songs[0]
            command = 'rhythmbox-client --play-uri="' + song_uri + '"'
            os.system(command)
            return("Playing " + song) 
        except:
            return("Song not found in your system.")

    else:
        return "can't play right now"

