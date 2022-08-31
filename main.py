from pytube import YouTube
import PySimpleGUI as sg
sg.theme('DarkAmber')
layout = [
          [sg.Text('Önce Linki girin, ardından platformu seçin ve bekleyin. İçerik uygulama ile aynı klasöre indirilecektir.'), sg.Text(size=(15, 1))],
          [sg.Text('Dosya boyutuna göre uzun sürebilir. Downsalka güven ve bekle. Bilgisayarda garip hareketler yapma bozulur.'), sg.Text(size=(15, 1))],
          [sg.Text('Link Girin'), sg.Text(size=(15,1))],
          [sg.InputText(size=(35, 3))],
          [sg.Text('Platform Seçin'), sg.Text(size=(15, 1))],
          [[sg.Button('Youtube')],
           [sg.Button('İnstagram')]]]
window = sg.Window("DownSalk").Layout(layout)
event, values = window.read()
linkadress = values[0]
window.close()
if event == "Youtube":
    yt = YouTube(linkadress)

    print("Title: ", yt.title)
    print("Number of views: ", yt.views)
    print("Length of video: ", yt.length)
    print("Rating of video: ", yt.rating)

    ys = yt.streams.get_highest_resolution()

    print("Downloading...")
    ys.download()
    print("Download completed!!")
elif event == "Instagram":
    print("onu daha yapmadık")