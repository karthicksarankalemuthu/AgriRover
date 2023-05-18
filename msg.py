from twilio.rest import Client



account_sid = 'AC0c228c92c51a2ec0f68388287e69e4e4'
auth_token = 'b4104194a0dc91e0580a66526ee0001b'

class_names=['Tomato_Bacterial_spot',
                   'Tomato_Early_blight',
                    'Tomato_Late_blight',
                   'Tomato_Leaf_Mold',
                   'Tomato_Septoria_leaf_spot',
                   'Tomato_Spider_mites',
                   'Tomato_Target_Spot',
                   'Tomato_Tomato_Yellow_Leaf_Curl_Virus',
                  'Tomato_Tomato_mosaic_virus',
                 'Tomato_healthy']

antibiotics=["Streptomycin sulphate 90% + Tetracylin hydrocloride 10% SP @ 500ml / ha after the appearance of first true leaves followed by two sprays of streptocycline, one before transplanting and another after transplanting","Spray hexaconazole 5% SC @ 1ml/l (or)Propiconazole 25% EC @ 500 ml/ha at 30 and 50 days after planting (or)Metiram 70% WG 2.5kg/ha","Apply any one of the follwoing fungicide Azoxystrobin 23% SC - 500ml / ha .Cyazofamid 34.5% SC - 200ml / ha.Mancozeb 3% SC- 25l / ha.Zineb 75% WP - 1Kg / ha.Azoxystrobin 18.2% + Difenoconazole 11.4% w/w SC - 500ml / ha","Ensure good drainage facility In the greenhouse, maintain a RH of less than 80%, during the night Remove decaying plant material from the plant bed Avoid bruising during packing and transport Pre harvest spray 0.2% captan at monthly intervals","Destruction of disease debris and avoiding excessive irrigation is recommended","Spray wettable sulphur 50 WP 2g/lit or dicofol 18.5 EC 2.5 ml/lit","Dimethoate 30 EC @ 1 ml /l Malathion 50 EC @ 1.5 ml / l Methyl demeton 25 EC @ 1.0 ml/l Thiamethoxam 25 WG @ 4 ml/10 l Cyantraniliprole 10.26 OD @ 1.8 ml/l Imidacloprid 17.8 SL @ 3 ml/10l Spiromesifen 22.9 SC @ 1.25 ml/l to control white fly vector","Streptomycin sulphate 90% + Tetracylin hydrocloride 10% SP @ 500ml / ha after the appearance of first true leaves followed by two sprays of streptocycline, one before transplanting and another after transplanting","Spray Imidacloprid 70 WG- 1.0g / ha in field","healthy"]

def sendmsg(num):
      msg=antibiotics[num]
      dis=class_names[num]
      client = Client(account_sid, auth_token)
      message1 = client.messages.create(
        from_='whatsapp:+14155238886',
        body =dis,
        to='whatsapp:+918098008619'
      )
      message = client.messages.create(
        from_='whatsapp:+14155238886',
        body =msg,
        to='whatsapp:+918098008619'
      )
      
      print(message)
      print(message1)

