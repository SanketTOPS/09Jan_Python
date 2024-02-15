import instaloader

insta=instaloader.Instaloader()

pname=input("Enter any insta ID:")

insta.download_profile(pname,profile_pic_only=False)

print("Download successfully!")