from marshmallow import Schema, fields


class details_Schema(Schema):
    job_title = fields.Str()
    phone_number = fields.Int()
    employee_name = fields.Str()
    location = fields.Str()


album = dict(employee_name="chaitanya", job_title="developer", phone_number=9963640627, location= "office" )

robert = details_Schema()
result = robert.dump(album)
print(result)