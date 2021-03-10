from flask import Flask 
import requests, logging

app = Flask(__name__)   

logging.basicConfig(filename='test.log', level=logging.ERROR)

@app.errorhandler(404)
def page_not_found(errorhandler):
    app.logger.error(error)
    return "<h1>페이지가 없습니다</h1>" , 404


@app.route("/google")
def get_google():
    #다른 웹사이트 통째로 html로 가져와서 .text해서 해당 html을 마치 내 서버인것 처럼 보여준다
    response = requests.get("http://www.google.co.kr")

    return response.text 
 
# 로그를 남길 부분에 다음과 같이 로그 레벨에 맞추어 출력해주면 해당 내용이 파일에 들어감
logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")

if __name__ == "__main__":
    app.run(port="8090")