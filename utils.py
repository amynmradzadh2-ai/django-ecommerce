from kavenegar import KavenegarAPI, APIException, HTTPException
def send_otp_code(phone_number, code):
    try:
        api = KavenegarAPI('39466148576D4D3677515876614E583639797A336979564C7A3245473045734E383871524F712B553649453D')
        params = {
        'sender': '2000660110',#optional
        'receptor': phone_number,#multiple mobile number, split by comma
        'message': f'{code}کد تایید شما ',
        }
        response = api.sms_send(params)
        print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)
