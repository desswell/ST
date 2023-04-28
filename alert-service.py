from concurrent import futures

import grpc

from alert_service_pb2 import NotificationResponse

import alert_service_pb2_grpc


class AlertService(
    alert_service_pb2_grpc.AlertServiceServicer
):

    def ScheduleNotification(self, request, context):
        return NotificationResponse(send_status=228)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    alert_service_pb2_grpc.add_AlertServiceServicer_to_server(
        AlertService(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()