import grpc

from alert_service_pb2_grpc import AlertServiceStub
from alert_service_pb2 import NotificationRequest
channel = grpc.insecure_channel("localhost:50051")
client = AlertServiceStub(channel)

request = NotificationRequest(notification_id=1, notification_title="dsadsa", description="dsa", username="dsadsa")
print(client.ScheduleNotification(request).send_status)