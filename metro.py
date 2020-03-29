import requests
import nexmo
import time
while True:
    url = "https://www.metro.ca/fr/service-and-timeslot/timeslot?_=1585423307392"

    payload = {}
    headers = {
    'Cookie': '__cfduid=d0d97751098823e2f4e391333cb28492e1584373913; METRO_ANONYMOUS_COOKIE=45374623-1053-4a7d-9196-80c333fbefec; hprl=en; hide-store-banner=true; nbVisited=1; NSC_JOqrpj5ubudv2fpeodwdbrdxp2rrpei=ffffffff09023b1c45525d5f4f58455e445a4a423660; firstPageAlreadyVisited=false; sto__session=1585444931922; JSESSIONID=D8588216902F07F23A39DCD1ECC98985; sto__count=2'
    }
    response = requests.request("GET", url, headers=headers, data = payload)
    retour = str(response.text.encode('utf8'))
    if response.status_code != 200:
        print("Error Sending SMS and exiting ...")
        client = nexmo.Client(key='d8f089a6', secret='1BUTd1KgHnlzixEV')
        client.send_message({
                'from': '15792690732',
                'to': '15147991390',
                'text': 'Erreur Changer le cookie !',
        })
        exit()
    else:
        print(response.status_code)
        print(retour)
        if not "Aucune plage horaire disponible" in retour:
            client = nexmo.Client(key='d8f089a6', secret='1BUTd1KgHnlzixEV')
            client.send_message({
                'from': '15792690732',
                'to': '15147991390',
                'text': 'Slot de dispo !',
            })
        else:
            print ("Aucun slot dispo")
        time.sleep(20)
