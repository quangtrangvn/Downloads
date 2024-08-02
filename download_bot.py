from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import yt_dlp as youtube_dl
import requests
import os

# Nhập mã token của bot
TOKEN = '7380021997:AAG6-X6Ey32BmH9KnnQ2ie8PFUk_BiS4GEg'

# Hàm khởi tạo bot
def start(update, context):
    update.message.reply_text('HÍ ANH EM! Gửi cho TRẠNG link video từ Facebook, TikTok, hoặc YouTube để TRẠNG tải xuống cho bạn nha.')

# Hàm xử lý link video
def download_video(update, context):
    url = update.message.text
    chat_id = update.message.chat_id

    update.message.reply_text('Đang tải video, anh em vui lòng đợi, vì lí do máy chủ chạy bot hơi cùi nên có thể video nặng sẽ báo lỗi nhé!...')

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
            context.bot.send_video(chat_id=chat_id, video=video)

        # Xóa video sau khi gửi
        os.remove(os.path.join('downloads', video_file))

    except Exception as e:
        update.message.reply_text('Có lỗi xảy ra khi tải video: {}'.format(str(e)))

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, download_video))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

