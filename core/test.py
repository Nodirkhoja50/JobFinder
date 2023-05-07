from django.template.loader import render_to_string
sms_body=render_to_string(
                "otp.txt",
                {"otp":1,"id":12}
            )
print(sms_body)