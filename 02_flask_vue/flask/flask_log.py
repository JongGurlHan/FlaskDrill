from flask import Flask
import requests

app = Flask(__name__)

if not app.debug:
    import logging
    from logging.handlers import RotatingFileHandler #logging 핸들러 이름을 적어줌
    file_handler = RotatingFileHandler('James_server.log', maxBytes=2000, backupCount=10)
    file_handler.setLevel(logging.WARNING) #어느 단계까지 로깅을 할지를 적어줌 , default는 warning
    app.logger.addHandler(file_handler)


@app.errorhandler(404)
def page_not_found(errorhandler):
    app.logger.error('page_not_found에서 일어났습니다.')
    return "<h3>해당 경로에 맞는 페이지를 찾지 못했습니다, 관리자에게 연락주세요</h3>"

if __name__ == "__main__":
    app.run(port="8090", debug=False)