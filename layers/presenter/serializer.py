from marshmallow import Schema, fields


class CompanySchema(Schema):

    name = fields.Str()
    email = fields.Email()
    phone = fields.Str()
    is_active = fields.Boolean()
    dummy_card = fields.Boolean()
