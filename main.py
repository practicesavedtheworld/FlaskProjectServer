from flask import Flask, request

app = Flask(__name__)
LIST_OF_MASSAGES = []


@app.route('/')
def fa():
    return 'Messenger on Flask Framework is running'\
            '<a href="/status">Check server status</a>'


@app.route('/status')
def status():
    return {
        'messages_count': len(LIST_OF_MASSAGES)
    }


@app.route("/api/Messanger", methods=['POST'])
def send_message():
    msg = request.json
    print(msg)
    LIST_OF_MASSAGES.append(msg)
    msgtext = f"{msg['UserName']} <{msg['TimeStamp']}>:{msg['MessageText']}"
    print(f"Всего сообщений: {len(LIST_OF_MASSAGES)}, Посланное сообщение: {msgtext}")
    return f"Сообщение отослано успешно. Всего сообщений: {len(LIST_OF_MASSAGES)}"


@app.route("/api/Messanger/<int:id>")
def get_message(id):
    print(id)
    if id >= 0 < len(LIST_OF_MASSAGES):
        print(LIST_OF_MASSAGES[id])
        return LIST_OF_MASSAGES[id], 200
    else:
        return "Not found", 404


if __name__ == '__main__':
    app.run()
