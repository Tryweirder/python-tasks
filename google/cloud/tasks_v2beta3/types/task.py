# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import proto  # type: ignore


from google.cloud.tasks_v2beta3.types import target
from google.protobuf import duration_pb2 as duration  # type: ignore
from google.protobuf import timestamp_pb2 as timestamp  # type: ignore
from google.rpc import status_pb2 as status  # type: ignore


__protobuf__ = proto.module(
    package="google.cloud.tasks.v2beta3", manifest={"Task", "Attempt",},
)


class Task(proto.Message):
    r"""A unit of scheduled work.

    Attributes:
        name (str):
            Optionally caller-specified in
            [CreateTask][google.cloud.tasks.v2beta3.CloudTasks.CreateTask].

            The task name.

            The task name must have the following format:
            ``projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID/tasks/TASK_ID``

            -  ``PROJECT_ID`` can contain letters ([A-Za-z]), numbers
               ([0-9]), hyphens (-), colons (:), or periods (.). For
               more information, see `Identifying
               projects <https://cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects>`__
            -  ``LOCATION_ID`` is the canonical ID for the task's
               location. The list of available locations can be obtained
               by calling
               [ListLocations][google.cloud.location.Locations.ListLocations].
               For more information, see
               https://cloud.google.com/about/locations/.
            -  ``QUEUE_ID`` can contain letters ([A-Za-z]), numbers
               ([0-9]), or hyphens (-). The maximum length is 100
               characters.
            -  ``TASK_ID`` can contain only letters ([A-Za-z]), numbers
               ([0-9]), hyphens (-), or underscores (_). The maximum
               length is 500 characters.
        app_engine_http_request (google.cloud.tasks_v2beta3.types.AppEngineHttpRequest):
            HTTP request that is sent to the App Engine app handler.

            An App Engine task is a task that has
            [AppEngineHttpRequest][google.cloud.tasks.v2beta3.AppEngineHttpRequest]
            set.
        http_request (google.cloud.tasks_v2beta3.types.HttpRequest):
            HTTP request that is sent to the task's target.

            An HTTP task is a task that has
            [HttpRequest][google.cloud.tasks.v2beta3.HttpRequest] set.
        pull_message (google.cloud.tasks_v2beta3.types.PullMessage):
            Pull Message contained in a task in a
            [PULL][google.cloud.tasks.v2beta3.Queue.type] queue type.
            This payload type cannot be explicitly set through Cloud
            Tasks API. Its purpose, currently is to provide backward
            compatibility with App Engine Task Queue
            `pull <https://cloud.google.com/appengine/docs/standard/java/taskqueue/pull/>`__
            queues to provide a way to inspect contents of pull tasks
            through the
            [CloudTasks.GetTask][google.cloud.tasks.v2beta3.CloudTasks.GetTask].
        schedule_time (google.protobuf.timestamp_pb2.Timestamp):
            The time when the task is scheduled to be attempted.

            For App Engine queues, this is when the task will be
            attempted or retried.

            ``schedule_time`` will be truncated to the nearest
            microsecond.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time that the task was created.

            ``create_time`` will be truncated to the nearest second.
        dispatch_deadline (google.protobuf.duration_pb2.Duration):
            The deadline for requests sent to the worker. If the worker
            does not respond by this deadline then the request is
            cancelled and the attempt is marked as a
            ``DEADLINE_EXCEEDED`` failure. Cloud Tasks will retry the
            task according to the
            [RetryConfig][google.cloud.tasks.v2beta3.RetryConfig].

            Note that when the request is cancelled, Cloud Tasks will
            stop listening for the response, but whether the worker
            stops processing depends on the worker. For example, if the
            worker is stuck, it may not react to cancelled requests.

            The default and maximum values depend on the type of
            request:

            -  For [HTTP tasks][google.cloud.tasks.v2beta3.HttpRequest],
               the default is 10 minutes. The deadline must be in the
               interval [15 seconds, 30 minutes].

            -  For [App Engine
               tasks][google.cloud.tasks.v2beta3.AppEngineHttpRequest],
               0 indicates that the request has the default deadline.
               The default deadline depends on the `scaling
               type <https://cloud.google.com/appengine/docs/standard/go/how-instances-are-managed#instance_scaling>`__
               of the service: 10 minutes for standard apps with
               automatic scaling, 24 hours for standard apps with manual
               and basic scaling, and 60 minutes for flex apps. If the
               request deadline is set, it must be in the interval [15
               seconds, 24 hours 15 seconds]. Regardless of the task's
               ``dispatch_deadline``, the app handler will not run for
               longer than than the service's timeout. We recommend
               setting the ``dispatch_deadline`` to at most a few
               seconds more than the app handler's timeout. For more
               information see
               `Timeouts <https://cloud.google.com/tasks/docs/creating-appengine-handlers#timeouts>`__.

            ``dispatch_deadline`` will be truncated to the nearest
            millisecond. The deadline is an approximate deadline.
        dispatch_count (int):
            Output only. The number of attempts
            dispatched.
            This count includes attempts which have been
            dispatched but haven't received a response.
        response_count (int):
            Output only. The number of attempts which
            have received a response.
        first_attempt (google.cloud.tasks_v2beta3.types.Attempt):
            Output only. The status of the task's first attempt.

            Only
            [dispatch_time][google.cloud.tasks.v2beta3.Attempt.dispatch_time]
            will be set. The other
            [Attempt][google.cloud.tasks.v2beta3.Attempt] information is
            not retained by Cloud Tasks.
        last_attempt (google.cloud.tasks_v2beta3.types.Attempt):
            Output only. The status of the task's last
            attempt.
        view (google.cloud.tasks_v2beta3.types.Task.View):
            Output only. The view specifies which subset of the
            [Task][google.cloud.tasks.v2beta3.Task] has been returned.
    """

    class View(proto.Enum):
        r"""The view specifies a subset of
        [Task][google.cloud.tasks.v2beta3.Task] data.

        When a task is returned in a response, not all information is
        retrieved by default because some data, such as payloads, might be
        desirable to return only when needed because of its large size or
        because of the sensitivity of data that it contains.
        """
        VIEW_UNSPECIFIED = 0
        BASIC = 1
        FULL = 2

    name = proto.Field(proto.STRING, number=1)

    app_engine_http_request = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="payload_type",
        message=target.AppEngineHttpRequest,
    )

    http_request = proto.Field(
        proto.MESSAGE, number=11, oneof="payload_type", message=target.HttpRequest,
    )

    pull_message = proto.Field(
        proto.MESSAGE, number=13, oneof="payload_type", message=target.PullMessage,
    )

    schedule_time = proto.Field(proto.MESSAGE, number=4, message=timestamp.Timestamp,)

    create_time = proto.Field(proto.MESSAGE, number=5, message=timestamp.Timestamp,)

    dispatch_deadline = proto.Field(
        proto.MESSAGE, number=12, message=duration.Duration,
    )

    dispatch_count = proto.Field(proto.INT32, number=6)

    response_count = proto.Field(proto.INT32, number=7)

    first_attempt = proto.Field(proto.MESSAGE, number=8, message="Attempt",)

    last_attempt = proto.Field(proto.MESSAGE, number=9, message="Attempt",)

    view = proto.Field(proto.ENUM, number=10, enum=View,)


class Attempt(proto.Message):
    r"""The status of a task attempt.

    Attributes:
        schedule_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time that this attempt was scheduled.

            ``schedule_time`` will be truncated to the nearest
            microsecond.
        dispatch_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time that this attempt was dispatched.

            ``dispatch_time`` will be truncated to the nearest
            microsecond.
        response_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time that this attempt response was
            received.

            ``response_time`` will be truncated to the nearest
            microsecond.
        response_status (google.rpc.status_pb2.Status):
            Output only. The response from the worker for this attempt.

            If ``response_time`` is unset, then the task has not been
            attempted or is currently running and the
            ``response_status`` field is meaningless.
    """

    schedule_time = proto.Field(proto.MESSAGE, number=1, message=timestamp.Timestamp,)

    dispatch_time = proto.Field(proto.MESSAGE, number=2, message=timestamp.Timestamp,)

    response_time = proto.Field(proto.MESSAGE, number=3, message=timestamp.Timestamp,)

    response_status = proto.Field(proto.MESSAGE, number=4, message=status.Status,)


__all__ = tuple(sorted(__protobuf__.manifest))
