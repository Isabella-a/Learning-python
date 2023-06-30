import requests
import base64
import json
import analytics

URL = "https://freelaw2157.zendesk.com/"
EMAIL = 'isabella@freelaw.work'
PWD = 'freelaw123'
TOKEN = '5hxYTmFJn4GKYroxv89HTkAgOZJIbq9EVjLSfx56'
AUTH_TOKEN = base64.b64encode(f'{EMAIL}/token:{TOKEN}'.encode()).decode()
Headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": f"Basic {AUTH_TOKEN}"
}

analytics.write_key = "EC49BKs3wIDrlXOAHX5HFjMXCOXnW6u1"
ID_USUARIO = 'bDF1oDL9GpAPwdfxNC4MJe'



def zendesk_ticket(body, subject):
    data = {
        "ticket": {
            "comment": {
                "body": body
            },
            "subject": subject,
        }
    }

    response = requests.get(f"{URL}api/v2/tickets.json", headers=Headers)
    res = requests.post(f"{URL}api/v2/tickets", json=data, headers=Headers)
    print(res)
    if res.status_code != 201:
        print('Status:', res.status_code, 'Problem with the request. Exiting.')
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


# body = 'Erro no envio de serviço'
# subject = 'Teste envio 3'
# zendesk_ticket(body, subject)


def segment(event, **kwargs):
    if kwargs:
        data = kwargs
    else:
        data = None
    analytics.track(ID_USUARIO, event, data)


def create_ticket_send_segment():
    body_ticket = 'Acionou o ticket que será enviado também para o segment'
    subject = 'Teste zendesk/segment'
    res_ticket = zendesk_ticket(body_ticket, subject)
    print(res_ticket)
    event = 'Resposta do zendesk'

    analytics.track(ID_USUARIO, event, res_ticket)


create_ticket_send_segment()
