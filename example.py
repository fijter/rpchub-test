import grpc
from proto import hub_pb2_grpc
from proto import messages_pb2

chan = grpc.insecure_channel('localhost:50051')
stub = hub_pb2_grpc.HubStub(chan)

# This creates a new user and generates a deposit address
# stub.CreateUser(messages_pb2.CreateUserRequest(userId='1'))
# response = stub.GetDepositAddress(messages_pb2.GetDepositAddressRequest(userId='1', includeChecksum=True))
# print(response.address)

# This gets the balance in IOTA for user 1
response = stub.GetBalance(messages_pb2.GetBalanceRequest(userId='1'))

print('{}i available for user 1'.format(response.available))


response = stub.GetUserHistory(messages_pb2.GetUserHistoryRequest(userId='1', newerThan=0))
print('History:')
print(response)
