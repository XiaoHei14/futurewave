from flask import Flask, request, jsonify
import socket

app = Flask(__name__)

def send_magic_packet(mac, ip):
    # 格式化MAC地址
    mac = mac.replace(":", "").replace("-", "")
    if len(mac) != 12:
        return False

    # 创建Magic Packet
    packet = bytes.fromhex("FF" * 6 + mac * 16)

    # 发送Magic Packet
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.sendto(packet, (ip, 9))
        return True
    except Exception as e:
        print(f"Error sending packet: {e}")
        return False

@app.route('/wake', methods=['POST'])
def wake():
    data = request.json
    mac = data.get('mac')
    ip = data.get('ip')
    if send_magic_packet(mac, ip):
        return jsonify({"message": "Magic Packet sent successfully"}), 200
    else:
        return jsonify({"message": "Failed to send Magic Packet"}), 400

if __name__ == '__main__':
    app.run(debug=True)
