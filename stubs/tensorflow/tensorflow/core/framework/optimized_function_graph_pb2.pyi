"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import sys
import tensorflow.core.framework.graph_pb2
import tensorflow.core.framework.types_pb2

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class OptimizedFunctionGraph(google.protobuf.message.Message):
    """Optimized function graph after instantiation-related graph optimization
    passes (up till before graph partitioning). The first half of the proto is
    representing a GraphDef and the rest of the fields are extra information from
    graph optimizations.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class NodeNameToControlRetEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.str | None = ...,
            value: builtins.str | None = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    NAME_FIELD_NUMBER: builtins.int
    FUNCTION_GRAPH_FIELD_NUMBER: builtins.int
    NODE_NAME_TO_CONTROL_RET_FIELD_NUMBER: builtins.int
    RET_TYPES_FIELD_NUMBER: builtins.int
    NUM_RETURN_NODES_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Function name. It can be a human-readable SignatureDef's method name, or a
    FunctionDef name.
    """
    @property
    def function_graph(self) -> tensorflow.core.framework.graph_pb2.GraphDef:
        """Optimized function graph."""
    @property
    def node_name_to_control_ret(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Maps from node name to control ret. This is an output from running TF/XLA
        bridge.
        """
    @property
    def ret_types(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[tensorflow.core.framework.types_pb2.DataType.ValueType]:
        """Return node types of the function. This is an output of graph
        preprocessing.
        """
    num_return_nodes: builtins.int
    """Number of return nodes. This is an output of graph preprocessing."""
    def __init__(
        self,
        *,
        name: builtins.str | None = ...,
        function_graph: tensorflow.core.framework.graph_pb2.GraphDef | None = ...,
        node_name_to_control_ret: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        ret_types: collections.abc.Iterable[tensorflow.core.framework.types_pb2.DataType.ValueType] | None = ...,
        num_return_nodes: builtins.int | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["function_graph", b"function_graph"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["function_graph", b"function_graph", "name", b"name", "node_name_to_control_ret", b"node_name_to_control_ret", "num_return_nodes", b"num_return_nodes", "ret_types", b"ret_types"]) -> None: ...

global___OptimizedFunctionGraph = OptimizedFunctionGraph
