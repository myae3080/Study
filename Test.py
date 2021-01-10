from flask import Flask
# flask 인스턴스 생성.
app = Flask(__name__)

@app.route('/')
def Test() -> str:
    return 'Testing!!'

if __name__ == '__main__':
    app.run()
