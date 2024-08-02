from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import yt_dlp as youtube_dl
import requests
import os

# Nhập mã token của bot
TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

# Hàm khởi tạo bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('HÍ ANH EM! Gửi cho TRẠNG link video từ Facebook, TikTok, hoặc YouTube để TRẠNG tải xuống giúp nhé.')

# Hàm xử lý link video
async def download_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text
    chat_id = update.message.chat_id

    await update.message.reply_text('Đang tải video, AE vui lòng đợi, vì máy chủ chạy bot cấu hình basic nên video nặng sẽ báo lỗi nhé!...')

    try:
        # Tạo một thư mục tạm thời để lưu video
        os.makedirs('downloads', exist_ok=True)
        ydl_opts = {
            'outtmpl': 'downloads/%(title)s.%(ext)s',
            'format': 'best'
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        # Tìm video vừa tải xuống
        video_file = max([f for f in os.listdir('downloads')], key=lambda f: os.path.getctime(os.path.join('downloads', f)))

        # Gửi video cho người dùng
        with open(os.path.join('downloads', video_file), 'rb') as video:
            await context.bot.send_video(chat_id=chat_id, video=video)

        # Xóa video sau khi gửi
        os.remove(os.path.join('downloads', video_file))

    except Exception as e:
        await update.message.reply_text('Có lỗi xảy ra khi tải video: {}'.format(str(e)))

def main():
    application = ApplicationBuilder().token(TOKEN).build()

    start_handler = CommandHandler('start', start)
    download_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, download_video)

    application.add_handler(start_handler)
    application.add_handler(download_handler)

    application.run_polling()

if __name__ == '__main__':
    main()
