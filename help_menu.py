from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

HELP_HOME_TEXT = (
    "❓ **Help Menu**\n\n"
    "Neeche category chuno, sab commands wahi mil jayenge."
)

HELP_SECTIONS = {
    "general": (
        "ℹ️ **General Commands**\n\n"
        "`/start` — Bot start karo, welcome message dekho\n"
        "`/help` — Ye help menu kholo"
    ),
    "music": (
        "🎵 **Music & Video Commands**\n\n"
        "`/play <naam/link>` — VC me audio stream karo\n"
        "`/vplay <naam/link>` — VC me video (audio ke saath) stream karo\n"
        "`/song <naam/link>` — Seedha MP3 file bhejo\n"
        "`/pause` `/resume` `/skip` `/stop` — playback control\n"
        "`/seek <seconds>` — audio ko position par le jao; `/seekback <seconds>` — peeche jao\n"
        "`/auth` `/unauth` `/authlist` — music controls ke liye users authorize karo\n"
        "`/autoplay` — queue khatam hone par current track repeat toggle\n"
        "`/queue` — current queue dekho\n"
        "`/playlist` — saved playlist dekho/chalao (`/playlist play <n>`, "
        "`/playlist remove <n>`, `/playlist clear`)\n\n"
        "💡 Har gaane ke saath ek **Now Playing card** aata hai jisme progress bar aur "
        "⏸️ 🔁 ⏭️ ⏹️ ❌ ➕ jaise buttons hote hain — seedha waha se control karo.\n"
        "💡 Kisi audio/video message par **reply** karke `/play` ya `/vplay` bhejo — "
        "wahi media VC me chalega, YouTube search ki zaroorat nahi.\n"
        "💡 `/play` aur `/vplay` dono me YouTube link seedha diya ja sakta hai."
    ),
    "admin": (
        "🛠 **Group Management**\n\n"
        "`/kick` `/ban` `/unban` `/mute` `/unmute` — reply/tag/@username/user_id se\n"
        "`/pin` `/unpin` — reply kiye gaye message par\n"
        "`/purge` — reply se lekar is message tak sab delete\n"
        "`/warn` `/warnings` `/resetwarn` — warning system (3 warnings par auto-ban)\n"
        "`/admins` — group ke admins dikhata hai\n"
        "`/settings` — group ki settings (welcome message, clean service messages)\n\n"
        "Ye sab sirf group admins ya sudo users use kar sakte hain — sudo/owner ke liye "
        "group me actual admin hona zaroori nahi hai."
    ),
    "sudo": (
        "👑 **Owner & Sudo**\n\n"
        "`/addsudo` `/delsudo` — reply/tag/@username/user_id se, sirf owner use kar sakta hai\n"
        "`/sudolist` — sudo users ki list, naam par tap karke unki profile khulegi\n"
        "`/gban` `/ungban` `/gbanlist` — global ban across all groups\n"
        "`/selfpromote` `/selfadmin` — bot/khud ko admin banao\n"
        "`/whois <reply/tag/@username/id>` — kisi ek user ka current info (naam, id, sudo/gban status)\n"
        "`/groupadmins` — sab groups ke admins ka cached overview (har 10 min me refresh hota hai)\n"
        "`/broadcast <text>` (ya kisi message par reply) — sab groups + personal chats me bhejo, "
        "groups me automatically pin bhi ho jayega\n\n"
        "Ye sab sirf owner (aur sudo, jaha likha hai) use kar sakte hain.\n"
        "💡 Owner aur sudo users kisi bhi group me **saare commands** use kar sakte hain, "
        "chahe wo waha admin ho ya na ho."
    ),
}


def help_home_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("ℹ️ General", callback_data="help_general")],
            [InlineKeyboardButton("🎵 Music & Video", callback_data="help_music")],
            [InlineKeyboardButton("🛠 Group Management", callback_data="help_admin")],
            [InlineKeyboardButton("👑 Owner & Sudo", callback_data="help_sudo")],
            [InlineKeyboardButton("❌ Close", callback_data="help_close")],
        ]
    )


def help_section_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [[InlineKeyboardButton("⬅️ Back", callback_data="help_main")]]
    )
