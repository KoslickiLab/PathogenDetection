# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.log_entry import LogEntry
from openapi_server.models.message import Message
from openapi_server.models.any_type import AnyType
from openapi_server.models.operations import Operations
from openapi_server import util

from openapi_server.models.log_entry import LogEntry  # noqa: E501
from openapi_server.models.message import Message  # noqa: E501

class Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, message=None, status=None, description=None, logs=None, workflow=None, submitter=None, operations=None, job_id=None, resource_id=None, tool_version=None, schema_version=None, biolink_version=None, datetime=None, table_column_names=None, original_question=None, restated_question=None, query_options=None, context=None, type=None, id=None, validation_result=None, total_results_count=None, info=None):  # noqa: E501
        """Response - a model defined in OpenAPI

        :param message: The message of this Response.  # noqa: E501
        :type message: Message
        :param status: The status of this Response.  # noqa: E501
        :type status: str
        :param description: The description of this Response.  # noqa: E501
        :type description: str
        :param logs: The logs of this Response.  # noqa: E501
        :type logs: List[LogEntry]
        :param workflow: The workflow of this Response.  # noqa: E501
        :type workflow: List[AnyType]
        :param submitter: The submitter of this Response.  # noqa: E501
        :type submitter: str
        :param operations: The operations of this Response.  # noqa: E501
        :type operations: Operations
        :param job_id: The job_id of this Response.  # noqa: E501
        :type job_id: str
        :param resource_id: The resource_id of this Response.  # noqa: E501
        :type resource_id: str
        :param tool_version: The tool_version of this Response.  # noqa: E501
        :type tool_version: str
        :param schema_version: The schema_version of this Response.  # noqa: E501
        :type schema_version: str
        :param biolink_version: The biolink_version of this Response.  # noqa: E501
        :type biolink_version: str
        :param datetime: The datetime of this Response.  # noqa: E501
        :type datetime: str
        :param table_column_names: The table_column_names of this Response.  # noqa: E501
        :type table_column_names: List[str]
        :param original_question: The original_question of this Response.  # noqa: E501
        :type original_question: str
        :param restated_question: The restated_question of this Response.  # noqa: E501
        :type restated_question: str
        :param query_options: The query_options of this Response.  # noqa: E501
        :type query_options: object
        :param context: The context of this Response.  # noqa: E501
        :type context: str
        :param type: The type of this Response.  # noqa: E501
        :type type: str
        :param id: The id of this Response.  # noqa: E501
        :type id: str
        :param validation_result: The validation_result of this Response.  # noqa: E501
        :type validation_result: object
        :param total_results_count: The total_results_count of this Response.  # noqa: E501
        :type total_results_count: int
        :param info: The info of this Response.  # noqa: E501
        :type info: str
        """
        self.openapi_types = {
            'message': Message,
            'status': str,
            'description': str,
            'logs': List[LogEntry],
            'workflow': List[AnyType],
            'submitter': str,
            'operations': Operations,
            'job_id': str,
            'resource_id': str,
            'tool_version': str,
            'schema_version': str,
            'biolink_version': str,
            'datetime': str,
            'table_column_names': List[str],
            'original_question': str,
            'restated_question': str,
            'query_options': object,
            'context': str,
            'type': str,
            'id': str,
            'validation_result': object,
            'total_results_count': int,
            'info': str
        }

        self.attribute_map = {
            'message': 'message',
            'status': 'status',
            'description': 'description',
            'logs': 'logs',
            'workflow': 'workflow',
            'submitter': 'submitter',
            'operations': 'operations',
            'job_id': 'job_id',
            'resource_id': 'resource_id',
            'tool_version': 'tool_version',
            'schema_version': 'schema_version',
            'biolink_version': 'biolink_version',
            'datetime': 'datetime',
            'table_column_names': 'table_column_names',
            'original_question': 'original_question',
            'restated_question': 'restated_question',
            'query_options': 'query_options',
            'context': 'context',
            'type': 'type',
            'id': 'id',
            'validation_result': 'validation_result',
            'total_results_count': 'total_results_count',
            'info': 'info'
        }

        self._message = message
        self._status = status
        self._description = description
        self._logs = logs
        self._workflow = workflow
        self._submitter = submitter
        self._operations = operations
        self._job_id = job_id
        self._resource_id = resource_id
        self._tool_version = tool_version
        self._schema_version = schema_version
        self._biolink_version = biolink_version
        self._datetime = datetime
        self._table_column_names = table_column_names
        self._original_question = original_question
        self._restated_question = restated_question
        self._query_options = query_options
        self._context = context
        self._type = type
        self._id = id
        self._validation_result = validation_result
        self._total_results_count = total_results_count
        self._info = info

    @classmethod
    def from_dict(cls, dikt) -> 'Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Response of this Response.  # noqa: E501
        :rtype: Response
        """
        return util.deserialize_model(dikt, cls)

    @property
    def message(self):
        """Gets the message of this Response.


        :return: The message of this Response.
        :rtype: Message
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this Response.


        :param message: The message of this Response.
        :type message: Message
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

    @property
    def status(self):
        """Gets the status of this Response.

        One of a standardized set of short codes, e.g. Success, QueryNotTraversable, KPsNotAvailable  # noqa: E501

        :return: The status of this Response.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Response.

        One of a standardized set of short codes, e.g. Success, QueryNotTraversable, KPsNotAvailable  # noqa: E501

        :param status: The status of this Response.
        :type status: str
        """

        self._status = status

    @property
    def description(self):
        """Gets the description of this Response.

        A brief human-readable description of the outcome  # noqa: E501

        :return: The description of this Response.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Response.

        A brief human-readable description of the outcome  # noqa: E501

        :param description: The description of this Response.
        :type description: str
        """

        self._description = description

    @property
    def logs(self):
        """Gets the logs of this Response.

        A list of LogEntry items, containing errors, warnings, debugging information, etc. List items MUST be in chronological order with earliest first.  # noqa: E501

        :return: The logs of this Response.
        :rtype: List[LogEntry]
        """
        return self._logs

    @logs.setter
    def logs(self, logs):
        """Sets the logs of this Response.

        A list of LogEntry items, containing errors, warnings, debugging information, etc. List items MUST be in chronological order with earliest first.  # noqa: E501

        :param logs: The logs of this Response.
        :type logs: List[LogEntry]
        """

        self._logs = logs

    @property
    def workflow(self):
        """Gets the workflow of this Response.

        A list of operations that were executed.  # noqa: E501

        :return: The workflow of this Response.
        :rtype: List[AnyType]
        """
        return self._workflow

    @workflow.setter
    def workflow(self, workflow):
        """Sets the workflow of this Response.

        A list of operations that were executed.  # noqa: E501

        :param workflow: The workflow of this Response.
        :type workflow: List[AnyType]
        """

        self._workflow = workflow

    @property
    def submitter(self):
        """Gets the submitter of this Response.

        Any string for self-identifying the submitter of a query. The purpose of this optional field is to aid in the tracking of the source of queries for development and issue resolution.  # noqa: E501

        :return: The submitter of this Response.
        :rtype: str
        """
        return self._submitter

    @submitter.setter
    def submitter(self, submitter):
        """Sets the submitter of this Response.

        Any string for self-identifying the submitter of a query. The purpose of this optional field is to aid in the tracking of the source of queries for development and issue resolution.  # noqa: E501

        :param submitter: The submitter of this Response.
        :type submitter: str
        """

        self._submitter = submitter

    @property
    def operations(self):
        """Gets the operations of this Response.

        Container for one or more Message objects or identifiers for one or more Messages along with the processing plan and options for how those messages were processed and returned  # noqa: E501

        :return: The operations of this Response.
        :rtype: Operations
        """
        return self._operations

    @operations.setter
    def operations(self, operations):
        """Sets the operations of this Response.

        Container for one or more Message objects or identifiers for one or more Messages along with the processing plan and options for how those messages were processed and returned  # noqa: E501

        :param operations: The operations of this Response.
        :type operations: Operations
        """

        self._operations = operations

    @property
    def job_id(self):
        """Gets the job_id of this Response.

        An identifier for the submitted job that can be used with /async_query_status to receive an update on the status of the job.  # noqa: E501

        :return: The job_id of this Response.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this Response.

        An identifier for the submitted job that can be used with /async_query_status to receive an update on the status of the job.  # noqa: E501

        :param job_id: The job_id of this Response.
        :type job_id: str
        """

        self._job_id = job_id

    @property
    def resource_id(self):
        """Gets the resource_id of this Response.

        Identifier string of the resource that provided this response (one of ARAX, Aragorn, etc.)  # noqa: E501

        :return: The resource_id of this Response.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this Response.

        Identifier string of the resource that provided this response (one of ARAX, Aragorn, etc.)  # noqa: E501

        :param resource_id: The resource_id of this Response.
        :type resource_id: str
        """

        self._resource_id = resource_id

    @property
    def tool_version(self):
        """Gets the tool_version of this Response.

        Version label of the tool that generated this response  # noqa: E501

        :return: The tool_version of this Response.
        :rtype: str
        """
        return self._tool_version

    @tool_version.setter
    def tool_version(self, tool_version):
        """Sets the tool_version of this Response.

        Version label of the tool that generated this response  # noqa: E501

        :param tool_version: The tool_version of this Response.
        :type tool_version: str
        """

        self._tool_version = tool_version

    @property
    def schema_version(self):
        """Gets the schema_version of this Response.

        Version label of this TRAPI schema  # noqa: E501

        :return: The schema_version of this Response.
        :rtype: str
        """
        return self._schema_version

    @schema_version.setter
    def schema_version(self, schema_version):
        """Sets the schema_version of this Response.

        Version label of this TRAPI schema  # noqa: E501

        :param schema_version: The schema_version of this Response.
        :type schema_version: str
        """

        self._schema_version = schema_version

    @property
    def biolink_version(self):
        """Gets the biolink_version of this Response.

        Version label of the Biolink model used in this document  # noqa: E501

        :return: The biolink_version of this Response.
        :rtype: str
        """
        return self._biolink_version

    @biolink_version.setter
    def biolink_version(self, biolink_version):
        """Sets the biolink_version of this Response.

        Version label of the Biolink model used in this document  # noqa: E501

        :param biolink_version: The biolink_version of this Response.
        :type biolink_version: str
        """

        self._biolink_version = biolink_version

    @property
    def datetime(self):
        """Gets the datetime of this Response.

        Datetime string for the time that this response was generated  # noqa: E501

        :return: The datetime of this Response.
        :rtype: str
        """
        return self._datetime

    @datetime.setter
    def datetime(self, datetime):
        """Sets the datetime of this Response.

        Datetime string for the time that this response was generated  # noqa: E501

        :param datetime: The datetime of this Response.
        :type datetime: str
        """

        self._datetime = datetime

    @property
    def table_column_names(self):
        """Gets the table_column_names of this Response.

        List of column names that corresponds to the row_data for each result  # noqa: E501

        :return: The table_column_names of this Response.
        :rtype: List[str]
        """
        return self._table_column_names

    @table_column_names.setter
    def table_column_names(self, table_column_names):
        """Sets the table_column_names of this Response.

        List of column names that corresponds to the row_data for each result  # noqa: E501

        :param table_column_names: The table_column_names of this Response.
        :type table_column_names: List[str]
        """

        self._table_column_names = table_column_names

    @property
    def original_question(self):
        """Gets the original_question of this Response.

        The original question text typed in by the user  # noqa: E501

        :return: The original_question of this Response.
        :rtype: str
        """
        return self._original_question

    @original_question.setter
    def original_question(self, original_question):
        """Sets the original_question of this Response.

        The original question text typed in by the user  # noqa: E501

        :param original_question: The original_question of this Response.
        :type original_question: str
        """

        self._original_question = original_question

    @property
    def restated_question(self):
        """Gets the restated_question of this Response.

        A precise restatement of the question, as understood by the Translator, for which the answer applies. The user should verify that the restated question matches the intent of their original question (it might not).  # noqa: E501

        :return: The restated_question of this Response.
        :rtype: str
        """
        return self._restated_question

    @restated_question.setter
    def restated_question(self, restated_question):
        """Sets the restated_question of this Response.

        A precise restatement of the question, as understood by the Translator, for which the answer applies. The user should verify that the restated question matches the intent of their original question (it might not).  # noqa: E501

        :param restated_question: The restated_question of this Response.
        :type restated_question: str
        """

        self._restated_question = restated_question

    @property
    def query_options(self):
        """Gets the query_options of this Response.

        Dict of options that can be sent with the query. Options are tool specific and not stipulated here  # noqa: E501

        :return: The query_options of this Response.
        :rtype: object
        """
        return self._query_options

    @query_options.setter
    def query_options(self, query_options):
        """Sets the query_options of this Response.

        Dict of options that can be sent with the query. Options are tool specific and not stipulated here  # noqa: E501

        :param query_options: The query_options of this Response.
        :type query_options: object
        """

        self._query_options = query_options

    @property
    def context(self):
        """Gets the context of this Response.

        JSON-LD context URI  # noqa: E501

        :return: The context of this Response.
        :rtype: str
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this Response.

        JSON-LD context URI  # noqa: E501

        :param context: The context of this Response.
        :type context: str
        """

        self._context = context

    @property
    def type(self):
        """Gets the type of this Response.

        Entity type of this response  # noqa: E501

        :return: The type of this Response.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Response.

        Entity type of this response  # noqa: E501

        :param type: The type of this Response.
        :type type: str
        """

        self._type = type

    @property
    def id(self):
        """Gets the id of this Response.

        URI for this response  # noqa: E501

        :return: The id of this Response.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Response.

        URI for this response  # noqa: E501

        :param id: The id of this Response.
        :type id: str
        """

        self._id = id

    @property
    def validation_result(self):
        """Gets the validation_result of this Response.

        Validation results and other summary stats computed for this Response.  # noqa: E501

        :return: The validation_result of this Response.
        :rtype: object
        """
        return self._validation_result

    @validation_result.setter
    def validation_result(self, validation_result):
        """Sets the validation_result of this Response.

        Validation results and other summary stats computed for this Response.  # noqa: E501

        :param validation_result: The validation_result of this Response.
        :type validation_result: object
        """

        self._validation_result = validation_result

    @property
    def total_results_count(self):
        """Gets the total_results_count of this Response.

        The total number of results that were generated prior to any filtering.  # noqa: E501

        :return: The total_results_count of this Response.
        :rtype: int
        """
        return self._total_results_count

    @total_results_count.setter
    def total_results_count(self, total_results_count):
        """Sets the total_results_count of this Response.

        The total number of results that were generated prior to any filtering.  # noqa: E501

        :param total_results_count: The total_results_count of this Response.
        :type total_results_count: int
        """

        self._total_results_count = total_results_count

    @property
    def info(self):
        """Gets the info of this Response.

        A placholder for including some additional information  # noqa: E501

        :return: The info of this Response.
        :rtype: str
        """
        return self._info

    @info.setter
    def info(self, info):
        """Sets the info of this Response.

        A placholder for including some additional information  # noqa: E501

        :param info: The info of this Response.
        :type info: str
        """

        self._info = info