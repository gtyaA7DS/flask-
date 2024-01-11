import os

import json



def getconfigdata():
  path=os.path.join('config/config.json')

  with open(path,'r') as file:
      config_data=json.load(file)
      file.close()
      return config_data



def setconfigdata(smtpservice1,email,pwd):
  try:
    path = os.path.join('config/config.json')

    with open(path, 'r') as file:
        config_data=json.load(file)
        file.close()
    config_data['host_server']=smtpservice1
    config_data['sender_email']=email
    config_data['pwd'] = pwd
    with open(path, 'w') as file:
        json.dump(config_data,file,indent=4)
        file.close()
    return  True
  except:
      return False
