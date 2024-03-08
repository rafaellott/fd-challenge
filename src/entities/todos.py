"""
Schemas file.

In this file you will find all Schemas related to the Request and Response for serialization.
Usually I use the Schema on the POST Request to treat the receiving data, to do the validations.
"""
from marshmallow import Schema, fields, EXCLUDE, INCLUDE


class TodoSchema(Schema):
    id = fields.Int(required=True)
    title = fields.Str(required=True)

    class Meta:
        # remove unknown fields
        unknown = INCLUDE
