# Tích hợp service download video vào telegram bot bằng python trên Cloud VPS, Cloud server ubuntu 22.04

#### Cách thực hiện chi tiết:
#### Chuẩn bị 1 VPS ubuntu 22.04 TLS, 1 bot telegram được tạo bởi https://t.me/BotFather lưu lại TOKEN bot.
1. **SSH vào VPS bằng terminal hoặc các phần mèm chuyên dụng: ssh user@you-ip**
2. **Cập nhật hệ thống:**
   - **Lệnh**:
     ```bash
     sudo apt update && sudo apt upgrade -y 
     ```
3. **cài đặt các thư viện cần thiết cho hệ thống:**
   - **Lệnh**:
     ```bash
     sudo apt-get install python3 python3-pip
     ```
   - **Lệnh**:
     ```bash
     pip install python-telegram-bot youtube-dl requests
     ```
   - **Lệnh**:
     ```bash
     pip install yt-dlp
     ```
4. **Dowload file python chứa thư viện chạy bot vô VPS bằng curl:**
   - **Lệnh**:
     ```bash
     sudo apt-get install curl -y
     ```
     ```bash
     curl -O https://raw.githubusercontent.com/quangtrangvn/Downloads/main/download_bot.py
     ```
5. **Mở file download_bot.py bằng công cụ vi, vim hoặc nano:**
   - **Lệnh**:
     ```bash
     vi download_bot.py
     ```
     ```bash
     vim download_bot.py
     ```
     ```bash
     nano download_bot.py
     ```
     - **sửa các tham số TELEGRAM_BOT_TOKEN đúng với tham số đã lưu lại ở bước chuẩn bị.**
     - Sau khi sửa lưu lại :wq đối với vi & vim, Ctrl + x sau đó bấm y và chọn enter để lưu và thoát đối với nano.
     - Chạy bot với lệnh:
     ```bash
     python3 download_bot.py
     ```
6. **Sử dụng PM2 để quản lý bot:**
- Để đảm bảo rằng cả hai bot hoặc nhiều bot đều chạy liên tục và khởi động lại khi hệ thống khởi động lại, bạn có thể sử dụng PM2.
   - **Lệnh**:
     ```bash
     sudo apt install nodejs npm
     ```
     ```bash
     sudo npm install -g pm2
     ```
- Chạy các bot với PM2, Khởi động bot.
   - **Lệnh**:
     ```bash
     pm2 start /root/download_bot.py --name download_bot
     ```
- Lưu trạng thái của PM2 để tự động khởi động lại khi hệ thống khởi động lại.
  - **Lệnh**:
     ```bash
     pm2 save
     pm2 startup
     ```
   Lệnh pm2 startup sẽ hướng dẫn bạn các bước cần thiết để cấu hình hệ thống để tự động khởi động PM2 khi hệ thống khởi động lại.
- Kiểm tra và quản lý các bot, Kiểm tra trạng thái các tiến trình PM2.
  - **Lệnh**:
     ```bash
     pm2 status
     ```
- Xem logs của một bot cụ thể.
  - **Lệnh**:
     ```bash
     pm2 logs download_bot
     ```
# CHÚC CÁC BẠN THÀNH CÔNG!
