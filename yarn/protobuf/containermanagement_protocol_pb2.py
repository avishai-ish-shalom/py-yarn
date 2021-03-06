# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: containermanagement_protocol.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import service as _service
from google.protobuf import service_reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import yarn_service_protos_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='containermanagement_protocol.proto',
  package='hadoop.yarn',
  serialized_pb='\n\"containermanagement_protocol.proto\x12\x0bhadoop.yarn\x1a\x19yarn_service_protos.proto2\xe8\x02\n\"ContainerManagementProtocolService\x12\x66\n\x0fstartContainers\x12(.hadoop.yarn.StartContainersRequestProto\x1a).hadoop.yarn.StartContainersResponseProto\x12\x63\n\x0estopContainers\x12\'.hadoop.yarn.StopContainersRequestProto\x1a(.hadoop.yarn.StopContainersResponseProto\x12u\n\x14getContainerStatuses\x12-.hadoop.yarn.GetContainerStatusesRequestProto\x1a..hadoop.yarn.GetContainerStatusesResponseProtoBD\n\x1corg.apache.hadoop.yarn.protoB\x1b\x43ontainerManagementProtocol\x88\x01\x01\x90\x01\x01\xa0\x01\x01')





DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\n\034org.apache.hadoop.yarn.protoB\033ContainerManagementProtocol\210\001\001\220\001\001\240\001\001')

_CONTAINERMANAGEMENTPROTOCOLSERVICE = _descriptor.ServiceDescriptor(
  name='ContainerManagementProtocolService',
  full_name='hadoop.yarn.ContainerManagementProtocolService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=79,
  serialized_end=439,
  methods=[
  _descriptor.MethodDescriptor(
    name='startContainers',
    full_name='hadoop.yarn.ContainerManagementProtocolService.startContainers',
    index=0,
    containing_service=None,
    input_type=yarn_service_protos_pb2._STARTCONTAINERSREQUESTPROTO,
    output_type=yarn_service_protos_pb2._STARTCONTAINERSRESPONSEPROTO,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='stopContainers',
    full_name='hadoop.yarn.ContainerManagementProtocolService.stopContainers',
    index=1,
    containing_service=None,
    input_type=yarn_service_protos_pb2._STOPCONTAINERSREQUESTPROTO,
    output_type=yarn_service_protos_pb2._STOPCONTAINERSRESPONSEPROTO,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='getContainerStatuses',
    full_name='hadoop.yarn.ContainerManagementProtocolService.getContainerStatuses',
    index=2,
    containing_service=None,
    input_type=yarn_service_protos_pb2._GETCONTAINERSTATUSESREQUESTPROTO,
    output_type=yarn_service_protos_pb2._GETCONTAINERSTATUSESRESPONSEPROTO,
    options=None,
  ),
])

class ContainerManagementProtocolService(_service.Service):
  __metaclass__ = service_reflection.GeneratedServiceType
  DESCRIPTOR = _CONTAINERMANAGEMENTPROTOCOLSERVICE
class ContainerManagementProtocolService_Stub(ContainerManagementProtocolService):
  __metaclass__ = service_reflection.GeneratedServiceStubType
  DESCRIPTOR = _CONTAINERMANAGEMENTPROTOCOLSERVICE

# @@protoc_insertion_point(module_scope)
