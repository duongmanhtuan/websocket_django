# ## game/consumers.py
# import json
# from channels.generic.websocket import AsyncJsonWebsocketConsumer

# class TicTacToeConsumer(AsyncJsonWebsocketConsumer):
#     async def connect(self):
#         # self.room_name = self.scope['url_route']['kwargs']['room_code']
#         # self.room_name = "123"
#         # self.room_group_name = 'room_%s' % 'test'
#         print('ok')
#         # Join room group
#         await self.channel_layer.group_add(
#             'Fii',
#             self.channel_name
#         )
#         await self.accept()

#     async def disconnect(self, close_code):
#         print("Disconnected")
#         # Leave room group
#         await self.channel_layer.group_discard(
#             'Fii',
#             self.channel_name
#         )

#     async def receive(self, text_data):
#         """
#         Receive message from WebSocket.
#         Get the event and send the appropriate event
#         """
#         response = json.loads(text_data)
#         data = 'testneeee'
#         while True:
#             self.send(text_data=json.dumps({
#                 "payload": {
#                                 'type': 'send_data',
#                                 'data': data
#                             },
#             }))
#             # await self.channel_layer.group_send('Fii', {
#             #     'type': 'send_data',
#             #     'data': data
#             # })

#     async def send_data(self, res):
#         """ Receive message from room group """
#         # Send message to WebSocket
#         await self.send(text_data=json.dumps({
#             "payload": res,
#         }))
        
        
# import pyhik
import base64
import time
import channels.generic.websocket
import cv2

class TicTacToeConsumer(channels.generic.websocket.WebsocketConsumer):
    def connect(self):
        # Connect to Hikvision NVR
        # self.nvr = pyhik.HikCamera("<nvr_ip>", "<nvr_port>", "<nvr_user>", "<nvr_password>")
        # self.nvr.login()
        self.channel = None
        self.channel_name = 'test'
        self.accept()

    def disconnect(self, close_code):
        # Close the connection to Hikvision NVR
        self.disconnect(code=close_code)
        self.channel.stop()
        # self.nvr.logout()

    def receive(self, text_data):
        # Control Hikvision NVR and send video frames to client
        rtsp_url = 'rtsp://192.168.22.119:8554/'
        video_capture = cv2.VideoCapture(rtsp_url)
        video_capture.set(cv2.CAP_PROP_FPS, 25)
        while True:
            ret, frame = video_capture.read()

            if not ret:
                break
            # image = cv2.imread('Untitled.png')
            # frame = self.channel.get_frame()
            # frame = b'Hello, World!'
            # Chuyển đổi ảnh thành base64
            retval, buffer = cv2.imencode('.jpg', frame)
            base64_image = base64.b64encode(buffer).decode('utf-8')
            # encoded_frame = base64.b64encode(frame).decode('utf-8')
            encoded_frame = base64_image
            
            self.send(encoded_frame)