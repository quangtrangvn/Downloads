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
