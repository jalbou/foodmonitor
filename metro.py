import requests
import nexmo
import time
while True:
    url = "https://www.metro.ca/fr/service-and-timeslot/timeslot?_=1585423307392"

    payload = {}
    headers = {
    'Cookie': '__cfduid=d4a4f50d770186b055fe7be5c6bf4a0941585410447; METRO_ANONYMOUS_COOKIE=230af30e-dca7-4e64-a1b3-b72cec3c46d3; NSC_JOqrpj5ubudv2fpeodwdbrdxp2rrpei=ffffffff09023b0345525d5f4f58455e445a4a423660; firstPageAlreadyVisited=false; hide-store-banner=true; _gcl_au=1.1.1901223543.1585410494; sto__vuid=61c886e482b755b10a81d18a57a3228c; _ga=GA1.2.827530042.1585410495; _gid=GA1.2.1781070790.1585410495; _fbp=fb.1.1585410494650.1597290669; _hjid=4038234f-b5d7-4a4b-a264-87ec2462baaa; __sonar=6157287068393680578; InterceptVisited=1; nbVisited=1; __gads=ID=397fcf1e168c5b3e:T=1585410815:S=ALNI_MavNXnVzuxRxujpYcn6R8cQCHx6xA; hprl=fr; sto__session=1585428243319; JSESSIONID=089E78EBFA418471F9480F7F61A441FD; ADRUM=s=1585428291387&r=https%3A%2F%2Fwww.metro.ca%2Faccueil%3F0; sto__count=2; _gat_UA-664008-1=1'
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