# ------------------------------------------Instagram Following Bot-----------------------------------------------------

from InstaFollower import InstaFollower


chrome_driver_path = "C:\Program Files (x86)\chromedriver_win32\chromedriver.exe"
# -------------------------------------------Add Your instagram username and password-----------------------------------

username = "username"
password = "password"
# ----------------------------------------------------------------------------------------------------------------------
instagram_url = "https://www.instagram.com/"
# -----------------------------------------------Add similar account----------------------------------------------------
# To attract audience find account with similarities with your profile. add username of that name of account.
similar_account = "your favourite instagram account name"



insta_follower = InstaFollower()
insta_follower.login(username=username, password=password)
insta_follower.find_followers(account_name=similar_account)
insta_follower.follow()
# instagram allows only 60 following/un-followings actions per hour.
# So make sure to not run this program very often, it may lead to ban yr account.
