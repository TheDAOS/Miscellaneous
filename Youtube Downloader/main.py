import yt_dlp as youtube_dl
import os

def download_audio(yt_url, download_folder):
    # Ensure the download folder exists
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)
    
    # Set up options for yt_dlp
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),  # Template for output file path
    }

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([yt_url])
        print(f"Successfully downloaded: {yt_url}")
    except Exception as e:
        print(f"Failed to download {yt_url}. Error: {e}")

def main():
    yt_urls = [
        # part 1
        # "https://youtu.be/fdubeMFwuGs?si=Tl5B2mAPWRilTGAv",
        # "https://youtu.be/A66TYFdz8YA?si=uRq-vaLFf9ZqWmRM",
        # "https://youtu.be/6mr4cYJ7yew?si=CWpisIMJ_aUfQW2d",
        # "https://youtu.be/5Eqb_-j3FDA?si=kXCVaV3FTFqE01A1",
        # "https://youtu.be/4tYktXxNspo?si=aNP2QVDbl-FrMcwO",

        # "https://youtu.be/ofTxceS4wLI?si=KDI7DKx80ZAXC7H6",
        # "https://youtu.be/9JDSGhhiOwI?si=EkXXCMO_59wuiUrq",
        # "https://youtu.be/vr8RaNuWjWc?si=b366ediLX-l9ms3P",
        # "https://youtu.be/xitd9mEZIHk?si=4N3560NHk9ikko3G",
        # "https://youtu.be/xfMN4SpIxIA?si=r84iLuye7rI6Lgt2",
        
        # "https://youtu.be/bSAlE_WgHxY?si=g5QJvNNbsB6kFd-d",
        # "https://youtu.be/YxWlaYCA8MU?si=15sPvTdWYeQvSw6Z",
        # "https://youtu.be/zBlklssMFEo?si=B6OrwHEf2nqs6sTC",
        # "https://youtu.be/VOLKJJvfAbg?si=iqsf5q6hnbrADnVm",
        # "https://youtu.be/_iqHUSQ6eng?si=OpWKiIXEubuO1P1t",

        # "https://youtu.be/qoq8B8ThgEM?si=3FbTzlVG9sNocDy4",
        # "https://youtu.be/XgdY_s1LsZc?si=ky6ZD7Wqv1y_a6aY",
        # "https://youtu.be/gvyUuxdRdR4?si=zZ1pqatQXYvXqN42",
        # "https://youtu.be/V7LwfY5U5WI?si=S_5VJMZAMYOTf8fX",
        # "https://youtu.be/vgm1u2gPxzw?si=rsoCePZDZnT9oW0I", # 20

        # "https://youtu.be/ilNt2bikxDI?si=TltlZgfmT9531isg", # Don
        # "https://youtu.be/8olIVQpia3A?si=prIQPMzeOsnIBHvX", # Don


        # part 2
        # "https://youtu.be/cgmhimjsczk?si=6pbIHFjlEUA1Xyfy",
        # "https://youtu.be/w8LcxY43N5Y?si=jbUoBO2sMqSBm_66",
        # "https://youtu.be/DMH-GARKr1U?si=JruxQTWmIiKqP8oL",
        # "https://youtu.be/a9Hxkc9YxGE?si=ll35JGLABCykCwmr",
        # "https://youtu.be/DAYszemgPxc?si=Ts49HjAyXIp_98e5",

        # "https://youtu.be/Mv3SZDP7QUo?si=sPlDk3GDxoljtIpe",
        # "https://youtu.be/8v-TWxPWIWc?si=xnU3rOPfmRoOEDOZ",
        # "https://youtu.be/zFdi834FiZ4?si=ythqzH6KCSegG444",
        # "https://youtu.be/MJyKN-8UncM?si=VNoJ5MZH8gPgjQKd",
        # "https://youtu.be/9-AKLAfpjrI?si=V58aAtUN7QarkWHk",

        # "https://youtu.be/vD1bPSjFAQM?si=rJez1fBAnxdBWENx",
        # "https://youtu.be/uzS3WG6__G4?si=JNZSo93ReIZ5_LXI",
        # "https://youtu.be/gLEOwksK2ik?si=42B6I-gX8h6hueHE",
        # "https://youtu.be/0SVaz8VWE84?si=6hLDIv2_NXzuFBGK",
        # "https://youtu.be/nyuo9-OjNNg?si=RPe6XYLP-SPePFWR",

        # "https://youtu.be/2Vv-BfVoq4g?si=XzxN-Ywo472K9kHq",
        # "https://youtu.be/07fhkAoCnig?si=CYwFnXqhw9YCSkYK",
        # "https://youtu.be/x9lvT3b065g?si=ymfbKCJcHE_Rq9qI",
        # "https://youtu.be/b0xIZ5O-9Lk?si=7WO-SHFJEinANT-e",
        # "https://youtu.be/WgTMeICssXY?si=9qGjjQGKb9lvwyF2", # 40 + 2

        # part 3
        "",
        "",
        "",
        "",
        "",

        "",
        "",
        "",
        "",
        "",

        "",
        "",
        "",
        "",
        "",

        "",
        "",
        "",
        "",
        "",
    ]
    
    download_folder = 'audio_files'  # Specify the folder where files will be saved

    for url in yt_urls:
        download_audio(url, download_folder)

main()
