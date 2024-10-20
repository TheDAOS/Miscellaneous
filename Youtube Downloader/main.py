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
        # "https://youtu.be/MoN9ql6Yymw?si=svEY3EMyyy9N856q",
        # "https://youtu.be/syFZfO_wfMQ?si=bSEF3Ek0PZHyRQln",
        # "https://youtu.be/H5v3kku4y6Q?si=fCXzHl5L0hPWDfxg",
        # "https://youtu.be/LYJDRjEW_V4?si=FeuqCnT6TIhXWB0J",
        # "https://youtu.be/J7ck984Qhso?si=rxfHONN6_ZPo4ya0",

        # "https://youtu.be/_XBVWlI8TsQ?si=HnTYvsBRa7IxkJqN",
        # "https://youtu.be/7c3-Gei5j4w?si=KLfIYmZlaDMZ6fy_",
        # "https://youtu.be/N2cPyl83tkQ?si=81xalTruDvr6NeXT",
        # "https://youtu.be/_Aketl4J03Y?si=Yujvg_y1_Zr8eP-Y",
        # "https://youtu.be/lX3vT_Gm_HE?si=vXTFDHs9bRTEs80n",

        # "https://youtu.be/nqUN530Rgtw?si=jsQSXo01GBik56Qx",
        # "https://youtu.be/7xQCCw5sbdY?si=KZIhBiWmztKsu1Iu",
        # "https://youtu.be/BhUthi9HGjg?si=hVe8lucYCUslOQWa",
        # "https://youtu.be/Dll6VJ2C7wo?si=imIi1NXLuyTDTyEZ",
        # "https://youtu.be/oMKYLxwhAo8?si=GNUO82bq_28BgZom",

        # "https://youtu.be/XR7Ev14vUh8?si=gbBOkyzR1IUkNOQX",
        # "https://youtu.be/9u8a6G0y1fI?si=Esh2bxNdgrQ4cbBo",
        # "https://youtu.be/_WCD3Z9UmJ4?si=i-Lf3h0x-SPe_Azo",
        # "https://youtu.be/7yW_uJOpxww?si=qwEjYfHKDeiTEhsH",
        # "https://youtu.be/urecgzR3P-0?si=qvG3cdinlZJKXzP5", # 60 + 2

        # part 4
        # "https://youtu.be/Kbj2Zss-5GY?si=PsJh-BJFeOxuDNBP",
        # "https://youtu.be/fGqdIPer-ms?si=F6CEn0eZXhooJyIP",
        # "https://youtu.be/ptJVWT6Oco4?si=eaF6dgbwloVmVPge",
        # "https://youtu.be/34Na4j8AVgA?si=dXGjee5Xm9cG75BM",
        # "https://youtu.be/uPD0QOGTmMI?si=hpDpe14E8hob8v13",
        
        # "https://youtu.be/RhU9MZ98jxo?si=ZhqAeZvvMp0aTYmi",
        # "https://youtu.be/4NRXx6U8ABQ?si=l5ETh8M5Cj-utRKO",
        # "https://youtu.be/YQ-qToZUybM?si=M6K8mzX1wvkBiP8x",
        # "https://youtu.be/UuOQ6_MUax0?si=L7mPPH4jL7WWp0Rl",
        # "https://youtu.be/UbMgcdmYC70?si=59CgMnkkThNv55ai",

        # "https://youtu.be/ch8g-sJb6ow?si=IIxVQuaUUA1axePS",
        # "https://youtu.be/HZsRjrYW-lk?si=Pzlofq3Xu9akCOts",
        # "https://youtu.be/SA7AIQw-7Ms?si=yoRTk_kOCZIEp_bY",
        # "https://youtu.be/xRb8hxwN5zc?si=AjGksFE6lInmCC4E",
        # "https://youtu.be/6mr4cYJ7yew?si=kk-vgXbfGP2yueCF",

        # "https://youtu.be/oWKgpB2zpgw?si=YVEUhqlezpMdgrqH",
        # "https://youtu.be/Zvp-VBmoPmI?si=KYUwDB9gsbALZKRI",
        # "https://youtu.be/f3FFOBrMmdg?si=_L_iFVGrm9-LXpIT",
        # "https://youtu.be/CJq1hGSO89A?si=vJ6ab_snkkSpL830",
        # "https://youtu.be/4POvT6O0ygE?si=Cdl9PKSi8KXEkVJk", # 80 + 2 - 1 (Dupicate)

        # part 5
        # "https://youtu.be/aDFEb_W2t1Y?si=HlRGnF5rjTRTmgSV",
        # "https://youtu.be/KsF8EAkvwSs?si=u9aexe0utQBRRPbf",
        # "https://youtu.be/o-Gmhk90JOE?si=egKWUcn6m-7CBXe9",
        # "https://youtu.be/8Q5d0P6x61k?si=i2EQUiji7bAuXzPu",
        # "https://youtu.be/nKEVIuya2kY?si=V5NliIKGB3bwywQ0",

        # "https://youtu.be/FAn2i7gu32w?si=OkcwzvpPd2K8swh2",
        # "https://youtu.be/mQiiw7uRngk?si=kNw0_RlZ_1mHbK2s",
        # "https://youtu.be/Irw8llgSC3s?si=Ln-bw24HbAFOMLq-",
        # "https://youtu.be/SAcpESN_Fk4?si=od8zeboZUAc3grHN",
        # "https://youtu.be/gvyUuxdRdR4?si=yNCM6Umfp8Ty1eFO",

        # "https://youtu.be/wO5j3lv_9Fs?si=iXya4N1HnwXx3DVT",
        # "https://youtu.be/Njq4A5DAqRw?si=cR0lpkuS3lqRKSl-",
        # "https://youtu.be/GYFDRoJtfGM?si=MVfRZjwHyixEN-hh",
        # "https://youtu.be/ZDjpGhiJtio?si=co2iUDedak9BLIiN",
        # "https://youtu.be/MsoXD3F95pM?si=L-cO5SwMjsk2PqlD",

        # "https://youtu.be/YQFEBNqOz7c?si=ZViH10XDiyNJLrEY",
        # "https://youtu.be/V7LwfY5U5WI?si=4u3HQ-7g97ienkVK",
        # "https://youtu.be/9JDSGhhiOwI?si=pWMe8iG-1JzhJU78",
        # "https://youtu.be/vKDsAB1ccn0?si=fq-p7abgjoe2ww6Y",
        # "https://youtu.be/atVof3pjT-I?si=bJOVFI4rV6wP7ADW", # 100 + 2 - 4 (Dupicate)

        # "https://youtu.be/OinGHNpnGtc?si=fiR4NhjhywAjBN3d",
        # "https://youtu.be/WpILgptU4iQ?si=wLcAA2eG5lb2nBU4", # + 2
        # "https://youtu.be/7dESZ5ufAt4?si=Xy9B8w_W6-3NKCVx",
        # "https://youtu.be/p7_GDN6r2OY?si=eki68hMtuWoNwgAD",
        # "https://youtu.be/tGXnuFu2LHU?si=n1ROh5BGQdT7t9gf",
        # "https://youtu.be/5_eAAZ9CgHA?si=fLTAH2HCqLd9-KLF",
        # "https://youtu.be/E_JsaSuK5C8?si=mqV9Yq5O2eZg0a4U",
        # "https://youtu.be/O6dEVqj04E8?si=CA1WPqRModZpC0Sz", # + 6
        # 100 + 10 - 4 (Dupicate)

        # "https://www.youtube.com/watch?v=IKpkXzMxTq0",
        # "https://youtu.be/3q_ijl-aaTI?si=fyLEyk3BdDl-MM7g",
    ]
    
    download_folder = 'audio_files'  # Specify the folder where files will be saved

    for url in yt_urls:
        download_audio(url, download_folder)

main()
