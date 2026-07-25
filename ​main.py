import os
import re
from telethon import Button, TelegramClient

# ==========================================
# Credentials & Setup
# ==========================================
API_ID = int(os.environ.get("API_ID", "12345678"))  # Telegram API ID
API_HASH = os.environ.get("API_HASH", "YOUR_API_HASH")  # Telegram API Hash
SESSION_STRING = os.environ.get("SESSION_STRING", "userbot")

SOURCE_CHANNEL = "@target_source_channel"  # উৎস চ্যানেল ইউজারনেম
MY_CHANNEL = "@your_channel_username"  # আপনার চ্যানেল ইউজারনেম

# ==========================================
# আপনার ৫৭টি গেমের সম্পূর্ণ ডাটাবেস
# ==========================================
GAME_DATABASE = {
    "yono rummy": {
        "title": "Yono Rummy",
        "bonus": "UPTO ₹100+₹300",
        "link": "https://yonorummyaa.com/?code=VIPQSYFW1U7&t=1747967855",
    },
    "yono slots": {
        "title": "Yono Slots",
        "bonus": "UPTO ₹120+₹320",
        "link": "https://www.yonoslot.com/?code=PJBAVZSMQKB&t=1743101854",
    },
    "yono games": {
        "title": "Yono Games",
        "bonus": "UPTO ₹140+₹340",
        "link": "https://yonogames8.com/?code=NG8WTHRW&t=1743102015",
    },
    "yono arcade": {
        "title": "Yono Arcade",
        "bonus": "UPTO ₹150+₹350",
        "link": "https://uonoarcadeagent4.com/?code=F55GHL6LQ3G&t=1743100813",
    },
    "yes spin": {
        "title": "YES SPIN",
        "bonus": "UPTO ₹160+₹360",
        "link": "https://yesspin4.com/?code=47T6XCNANE1&t=1757709283",
    },
    "jaiho 91": {
        "title": "Jaiho 91",
        "bonus": "UPTO ₹180+₹380",
        "link": "https://jaiho91.cc/?code=C42MT6VF7ZN&t=1778035597",
    },
    "yono vip": {
        "title": "Yono VIP",
        "bonus": "UPTO ₹200+₹400",
        "link": "https://yonovipcash.net/?code=9U8CSBE7UHB&t=1782879074",
    },
    "jaiho 777 vip": {
        "title": "Jaiho 777 VIP",
        "bonus": "UPTO ₹210+₹410",
        "link": "https://jaiho777vip.site/?code=GC2MC1NHPHZ&t=1780716165",
    },
    "jaiho arcade": {
        "title": "Jaiho Arcade",
        "bonus": "UPTO ₹220+₹420",
        "link": "https://jaihoarcade26.com/?code=AZDDMDV26V4&t=1741079971",
    },
    "jaiho win": {
        "title": "Jaiho Win",
        "bonus": "UPTO ₹230+₹430",
        "link": "https://www.jaihowin5.com/?code=4J69ZG2DK5H&t=1752209730",
    },
    "jaiho slots": {
        "title": "Jaiho Slots",
        "bonus": "UPTO ₹240+₹440",
        "link": "https://jahoslotsagent1.com/?code=EGPEZKXT838&t=1748230888",
    },
    "jaiho spin": {
        "title": "Jaiho Spin",
        "bonus": "UPTO ₹250+₹450",
        "link": "https://jaihospin1.com/?code=7TAJN64H9LP&t=1741079885",
    },
    "jaiho rummy": {
        "title": "Jaiho Rummy",
        "bonus": "UPTO ₹260+₹460",
        "link": "https://jaiho-rummy.com/?code=E74M53JS26R&t=1776974460",
    },
    "joy rummy": {
        "title": "JOY Rummy",
        "bonus": "UPTO ₹270+₹470",
        "link": "https://joyrummy.cc/?code=J5KNNUXTNLW&t=1768444922",
    },
    "rummy 888": {
        "title": "Rummy 888",
        "bonus": "UPTO ₹280+₹480",
        "link": "https://rummy888vip10.com/?code=EVSZMHU9AC2&t=1764567211",
    },
    "rummy 77": {
        "title": "Rummy 77",
        "bonus": "UPTO ₹290+₹490",
        "link": "https://rummy77a.com/?code=F3V7TB9KD5H&t=1763692367",
    },
    "rummy ludo": {
        "title": "Rummy Ludo",
        "bonus": "UPTO ₹300+₹500",
        "link": "https://ludorummy.download/?code=UWPH29LC845&t=1762829766",
    },
    "rummy 91": {
        "title": "Rummy 91",
        "bonus": "UPTO ₹110+₹310",
        "link": "https://www.ynrummy91g.com/?code=4KT7BTMD2ZY&t=1765972799",
    },
    "boss rummy": {
        "title": "Boss Rummy",
        "bonus": "UPTO ₹130+₹330",
        "link": "https://bossrummyn.com/?code=9HFEUHFV6JD&t=1766370231",
    },
    "ever 777": {
        "title": "Ever 777",
        "bonus": "UPTO ₹170+₹370",
        "link": "https://ever777J.COM/?code=ARH67JG55DZ&t=1765419366",
    },
    "777 game": {
        "title": "777 Game",
        "bonus": "UPTO ₹190+₹390",
        "link": "https://www.777game3.com/?code=H531GHAXED9&t=1761877821",
    },
    "ok rummy": {
        "title": "OK Rummy",
        "bonus": "UPTO ₹100+₹400",
        "link": "https://www.okrummy10.com/?code=H2GH1YUWWTH&t=1761013779",
    },
    "hindi 777": {
        "title": "Hindi 777",
        "bonus": "UPTO ₹120+₹420",
        "link": "https://hindi777refer.cc/?code=7LFYD743VCA&t=1764895429",
    },
    "club inr": {
        "title": "Club INR",
        "bonus": "UPTO ₹140+₹440",
        "link": "https://clubinr3.vip/?code=9VCQ27ABC5Q&t=1759199409",
    },
    "game rummy": {
        "title": "Game Rummy",
        "bonus": "UPTO ₹150+₹450",
        "link": "https://gamesrummy.app/?code=Q6WJ5M6UA4J&t=1758335492",
    },
    "rumble rummy": {
        "title": "Rumble Rummy",
        "bonus": "UPTO ₹160+₹460",
        "link": "https://rumblerummyofficial.vip/?code=UC0E2CABAJD&t=1756696218",
    },
    "spin winner": {
        "title": "Spin Winner",
        "bonus": "UPTO ₹180+₹480",
        "link": "https://spinwinnerfreecash2.com/?code=SDNHN67187V&t=1743101371",
    },
    "love rummy": {
        "title": "Love Rummy",
        "bonus": "UPTO ₹200+₹500",
        "link": "https://www.loverummy6.com/?code=AFC6FQSG7VX&t=1755829901",
    },
    "share slots": {
        "title": "Share Slots",
        "bonus": "UPTO ₹100+₹250",
        "link": "https://shareslots66.com/?code=GFV2UHKQ3XL&t=1754885021",
    },
    "maha games": {
        "title": "Maha Games",
        "bonus": "UPTO ₹110+₹260",
        "link": "https://mahagames.store/?code=J24VEQEGY9F&t=1776974564",
    },
    "hi rummy": {
        "title": "Hi Rummy",
        "bonus": "UPTO ₹120+₹270",
        "link": "https://hirummyrefer.vip/?code=RX389XDH2V6&t=1753063336",
    },
    "gogo rummy": {
        "title": "Gogo Rummy",
        "bonus": "UPTO ₹130+₹280",
        "link": "https://www.gogorummy8.com/?code=8FWMTAM8CUF&t=1743101440",
    },
    "ind club": {
        "title": "IND CLUB",
        "bonus": "UPTO ₹140+₹290",
        "link": "https://indclubc.com/?code=34UZ2SRRL2A&t=1751337884",
    },
    "top rummy": {
        "title": "TOP Rummy",
        "bonus": "UPTO ₹150+₹300",
        "link": "https://toprummy.cc/?code=7K9BTEX2Z7J&t=1750740391",
    },
    "ind rummy": {
        "title": "Ind Rummy",
        "bonus": "UPTO ₹160+₹310",
        "link": "https://indrummy7.com/?code=2BA8ADDPWEJ&t=1749436463",
    },
    "abc rummy": {
        "title": "ABC Rummy",
        "bonus": "UPTO ₹170+₹320",
        "link": "https://www.abcrummy1.com/?code=75CN7R7Y8PY&t=1743100250",
    },
    "ind slots": {
        "title": "IND Slots",
        "bonus": "UPTO ₹180+₹330",
        "link": "https://indslots3.com/?code=EYMCJP1NA2C&t=1743100179",
    },
    "101z": {
        "title": "101Z",
        "bonus": "UPTO ₹190+₹340",
        "link": "https://101zvip9.com/?code=398FPM6Q9PM&t=1747968336",
    },
    "spin gold": {
        "title": "Spin Gold",
        "bonus": "UPTO ₹200+₹350",
        "link": "https://spingoldagents.net/?code=HLTS5ALTUNW&t=1743100758",
    },
    "spin crush": {
        "title": "Spin Crush",
        "bonus": "UPTO ₹210+₹360",
        "link": "https://spincrush45.com/?code=ADEX467GURD&t=1743101621",
    },
    "mbm bet": {
        "title": "MBM BET",
        "bonus": "UPTO ₹220+₹370",
        "link": "https://mbmbet7.com/?code=UPHMEWS56EM&t=1748511523",
    },
    "spin101": {
        "title": "Spin101",
        "bonus": "UPTO ₹230+₹380",
        "link": "https://spin101-c.net/?code=3511UCZEPM1&t=1743099784",
    },
    "spin777": {
        "title": "Spin777",
        "bonus": "UPTO ₹240+₹390",
        "link": "https://spin777t.com/?code=7V9J2PJ16FK&t=1743101407",
    },
    "bet213": {
        "title": "Bet213",
        "bonus": "UPTO ₹250+₹400",
        "link": "https://bet213app.com/?code=2QTF2EVJQWF&t=1767409426",
    },
    "bingo101": {
        "title": "Bingo101",
        "bonus": "UPTO ₹260+₹410",
        "link": "https://bingo101o.com/?code=6YFGBDZHMPT&t=1753165795",
    },
    "789jackpots": {
        "title": "789JackPots",
        "bonus": "UPTO ₹270+₹420",
        "link": "https://789jackpotsrefer.cc/?code=J7ZG3A2XLFE&t=1743099633",
    },
    "567slots": {
        "title": "567Slots",
        "bonus": "UPTO ₹280+₹430",
        "link": "https://567slotsagents.net/?code=4NYT1UY68JN&t=1743099721",
    },
    "slots spin": {
        "title": "Slots Spin",
        "bonus": "UPTO ₹290+₹440",
        "link": "https://slotsspino.com/?code=XJBWC8R516C&t=1743100644",
    },
    "neta vip": {
        "title": "Neta VIP",
        "bonus": "UPTO ₹300+₹450",
        "link": "https://neta2.vip/?code=DR0FVH8VBKP&t=1743099907",
    },
    "slots winner": {
        "title": "Slots Winner",
        "bonus": "UPTO ₹100+₹450",
        "link": "https://slotswinnerf.com/?code=K4EHSWHN9C1&t=1778259858",
    },
    "inr rummy": {
        "title": "Inr Rummy",
        "bonus": "UPTO ₹150+₹400",
        "link": "https://inrrummy.cc/?code=JMQESK3J5UR&t=1767494008",
    },
    "saga slots": {
        "title": "Saga Slots",
        "bonus": "UPTO ₹200+₹450",
        "link": "https://sagaslotsw.com/?code=0QHPZS4EJXM&t=1747969670",
    },
    "yono 777": {
        "title": "YONO 777",
        "bonus": "UPTO ₹120+₹350",
        "link": "https://freeyono777bonus.com/?code=F9MQW121H9H&t=1750740205",
    },
    "yn777": {
        "title": "YN777",
        "bonus": "UPTO ₹180+₹450",
        "link": "https://www.y754.com/?code=4SWJ2Z2RNC2&t=1759154214",
    },
    "max rummy": {
        "title": "Max Rummy",
        "bonus": "UPTO ₹220+₹480",
        "link": "https://www.maxrummy444.com/?code=QUMF17KD7HQ&t=1784174750",
    },
    "dhan game": {
        "title": "Dhan Game",
        "bonus": "UPTO ₹220+₹480",
        "link": "https://www.dhanwinplay.com/?code=L2V36G8J9AR&t=1784782987",
    },
    "win rummy": {
        "title": "Win Rummy",
        "bonus": "UPTO ₹220+₹480",
        "link": "https://www.winrummy.com/?code=k2e36G8J9AR&t=1784785487",
    },
}

client = TelegramClient(SESSION_STRING, API_ID, API_HASH)


# ==========================================
# স্ক্রিনশটের হুবহু ফরম্যাট জেনারেটর
# ==========================================
def build_custom_post(game_data, promo_code):
    title = game_data["title"]
    bonus = game_data["bonus"]
    link = game_data["link"]

    post_text = f"""<b> {title} ➝</b> New Promo Code Fast Claim Now!!💰 

<b>🎟️ PROMO CODE </b> ➜ <code>{promo_code}</code>

<blockquote><b>🎁 NEW USERS </b>🎉 SIGNUP BONUS {bonus}</blockquote>

<b>🎰 {title.upper()} LINK </b> <a href='{link}'>☞ 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱 𝗡𝗼𝘄</a>📱

<b>💰 Minimum Amount ₹100 First Withdrawal</b> 💸

<blockquote><b>🔥 Join this channel</b> to get promo codes first!  <b>Pin this channel </b>so you never miss any important promo code </blockquote>

<blockquote><tg-spoiler>#Verified #promocode</tg-spoiler></blockquote>"""
    return post_text


# ==========================================
# বাটন সেটআপ (Inline Keyboard Buttons)
# ==========================================
BUTTONS = [
    [
        Button.url("🎰 New Game 45 ↗", "https://t.me/your_channel_username"),
        Button.url("Total Game 70 🎰 ↗", "https://t.me/your_channel_username"),
    ],
    [
        Button.url("👆 ALL GAMES 👆 ↗", "https://t.me/your_channel_username"),
        Button.url("🤖 Promo Code Bot 🤖 ↗", "https://t.me/YourPromoCodeBot"),
    ],
]


# ==========================================
# মেসজ এক্সট্রাক্ট এবং অটো-পোস্ট লজিক
# ==========================================
@client.on(events.NewMessage(chats=SOURCE_CHANNEL))
async def promo_listener(event):
    raw_text = event.raw_text or ""
    if not raw_text:
        return

    # ১. পোস্ট থেকে গেমের নাম মেলানো
    matched_game_key = None
    for game_key in GAME_DATABASE.keys():
        if game_key in raw_text.lower():
            matched_game_key = game_key
            break

    if not matched_game_key:
        return  # লিস্টের বাইরে গেম হলে স্কিপ করবে

    # ২. প্রমো কোড আলাদা করা
    code_match = re.search(
        r"(?:PROMO CODE|Claim|code)\s*(?:➜|>>|>|:)?\s*`?([A-Za-z0-9\.-]+)`?",
        raw_text,
        re.IGNORECASE,
    )
    extracted_code = (
        code_match.group(1) if code_match else "Check Mail Box 🎁"
    )

    # ৩. পোস্ট তৈরি করা
    game_info = GAME_DATABASE[matched_game_key]
    final_caption = build_custom_post(game_info, extracted_code)

    # ৪. আপনার চ্যানেলে অটো-পোস্ট করা
    try:
        if event.message.media:
            await client.send_file(
                MY_CHANNEL,
                file=event.message.media,
                caption=final_caption,
                parse_mode="html",
                buttons=BUTTONS,
            )
        else:
            await client.send_message(
                MY_CHANNEL,
                final_caption,
                parse_mode="html",
                buttons=BUTTONS,
            )
        print(
            f"✅ Post Published: {game_info['title']} (Code: {extracted_code})"
        )
    except Exception as e:
        print(f"❌ Post Error: {e}")


print("🤖 Userbot listening to source channel...")
client.start()
client.run_until_disconnected()
