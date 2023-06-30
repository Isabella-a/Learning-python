import analytics


analytics.write_key = "EC49BKs3wIDrlXOAHX5HFjMXCOXnW6u1"
ID_USUARIO = 'bDF1oDL9GpAPwdfxNC4MJe'
evento = 'Teste segment 2'
body = {
    'email': f'emailteste@freelaw.work',
}


def segment(event, data):
    analytics.track(ID_USUARIO, event, data)

