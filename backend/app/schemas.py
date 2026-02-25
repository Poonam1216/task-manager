from marshmallow import fields, validate
from .extensions import ma

VALID_STATUS = ["pending", "completed"]
VALID_PRIORITY = ["low", "medium", "high"]


class TaskSchema(ma.Schema):

    id = fields.Int(dump_only=True)

    title = fields.Str(
        required=True,
        validate=validate.Length(min=1)
    )

    description = fields.Str()

    status = fields.Str(
        validate=validate.OneOf(VALID_STATUS)
    )

    priority = fields.Str(
        validate=validate.OneOf(VALID_PRIORITY)
    )

    created_at = fields.DateTime(dump_only=True)


task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)
