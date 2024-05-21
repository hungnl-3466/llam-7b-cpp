FROM python:3.8

# Set môi trường Python không in ra output không cần thiết
# ENV PYTHONUNBUFFERED=1

# Sao chép mã ứng dụng vào thư mục làm việc trong Docker
# Cài đặt các thư viện cần thiết
RUN pip install gradio

WORKDIR /gradio_ui
COPY . /gradio_ui
RUN cd /gradio_ui
# Expose cổng mặc định cho Gradio (7878)
# EXPOSE 3000

# Chạy ứng dụng Gradio khi container được khởi động
CMD ["python", "UI.py"]
