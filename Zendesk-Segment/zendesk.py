import requests
import base64
import json

# curl https://freelaw2157.zendesk.com/api/v2/users/me.json \
#   -v -u isabella@freelaw.work:freelaw123

url = "https://freelaw2157.zendesk.com/"
email = 'isabella@freelaw.work'
pwd = 'freelaw123'
token = '5hxYTmFJn4GKYroxv89HTkAgOZJIbq9EVjLSfx56'
auth_token = base64.b64encode(f'{email}/token:{token}'.encode()).decode()
Headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": f"Basic {auth_token}"
}


def zendesk_ticket(body, subject):
    data = {
        "ticket": {
            "comment": {
                "body": body
            },
            "subject": subject,
        }
    }

    response = requests.get(f"{url}api/v2/tickets.json", headers=Headers)
    res = requests.post(f"{url}api/v2/tickets", json=data, headers=Headers)
    print(response)
    if res.status_code != 201:
        print('Status:', res.status_code, 'Problem with the request. Exiting.')
        exit()
    try:
        result_data = {
            "Info": res.json()
        }
    except json.decoder.JSONDecodeError:
        result_data = {
            "erro_json": True,
            "Info": res.text
        }
    return result_data


body = 'Erro no envio de serviço'
subject = 'Teste envio'
zendesk_ticket(body, subject)
