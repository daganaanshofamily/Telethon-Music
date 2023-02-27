import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6213538"))
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6013621408:AAHxJ8csck_T1FwuGf98gtmAXXp1Vud2rkE")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BJWap1wBuw73aoKy284svD_fECZBByMkDEvGBGHyHp6J258KRhoGBD7MDjSLHKHoevdlZAqMdtE9ASDYxrelCSYE0mbkfwqaV3xTnEAG-dmQnqLU43c_4FM3ssP4j_NB-tTjA4qKH0GLTtM9FUW2l22WkqGlRlZCZtCiNGjyT_42V_QQiVhO5Y_mbWSoGzhYu2DkOw6ZewRn6onGD_r2YPcJtPB35CyMB4r5-QMVNw1RCiXe1uc1vPoFm5Dsa6ENcvDlgNrI6LYmpTSRSopVNuu_JZxG_0jEsSrtKlg766tYvaQ3Xzu89MUXWqANYnE6Y93naZNM396SFefRYGTHoIGwjyZxkqc=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
