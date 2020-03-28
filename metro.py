import requests
import nexmo
import time
while True:
    url = "https://www.metro.ca/fr/service-and-timeslot/timeslot?_=1585423307392"

    payload = {}
    headers = {
    'Cookie': '__cfduid=d0d97751098823e2f4e391333cb28492e1584373913; METRO_ANONYMOUS_COOKIE=45374623-1053-4a7d-9196-80c333fbefec; hprl=en; hide-store-banner=true; nbVisited=1; NSC_JOqrpj5ubudv2fpeodwdbrdxp2rrpei=ffffffff09023b1c45525d5f4f58455e445a4a423660; sto__session=1585437026467; firstPageAlreadyVisited=false; JSESSIONID=80A09818AE5E25727D8ECDDAB9B0677B; sto__count=1; ADRUM_BTa=R:23|g:e9587403-e4c2-4d35-8b44-58ce106f203b|n:metrorichelieuinc-prod_c22980fa-c09c-4712-b489-98164bef9f11; ADRUM_BT1=R:23|i:268162|e:78'
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
