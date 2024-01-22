import requests
import json

##############
usr = 'your email'
passwd = 'your password'

outfile = open('path_to_csv','a')

food_type_list = ['gut_boosters','gut_suppressors','proteins','snacks','eggs_and_dairy','vegetables','fruits_and_dried_fruits',
                  'meat_and_poultry','beans_and_legumes','breads_and_flours','fish_and_seafood','pasta_and_grains','beverages',
                  'sauces_and_condiments','spreads_and_nut_butters','nuts_and_seeds','oils']

##############

##logging in
login_url = 'https://api.joinzoe.com/api/zoe_app/v3/auth/login/'

login_data = {
  "username": usr,
  "password": passwd
}
r = requests.post(login_url,login_data)

response = json.loads(str(r.text))

#parsing authentification data given in the post request response
token = response['key']

cookie = str(r.cookies)[27:-2]

spltcookies = cookie.split(',')
csrf = spltcookies[0].split('=')[1].split(' for ')[0]
sesh = spltcookies[1].split('=')[1].split(' for ')[0]

cookiedict = {'csrftoken':csrf,'sessionid':sesh}


#pulling data from api of certain food group
def get_food_vals(foodType):
  get_url = 'https://api.joinzoe.com/api/zoe_app/v3/foods/by-tag/{}/'.format(foodType)


  headers = {'Accept-Encoding':'gzip  ',
            'authorization': 'Token {}'.format(token),
            'Connection':'Keep-Alive',
            'content-type':'application/json ',
            'Cookie':'sessionid={};csrftoken={}'.format(sesh,csrf),
            'Host':'api.joinzoe.com',
            'User-Agent':'okhttp/4.11.0'
  }


  def parse_food(text):
      out = ''
      foods= []

      for i in text:
          foodname = str(i['name']).replace(', ','-')
        
          score = i['score']
          foods.append([foodname,int(score)])


      foods = sorted(foods, key=lambda x: -x[1])
      for food in foods:
          out = '{},{}\n'.format(food[0],food[1])
          outfile.write(out)

  get= requests.get(get_url,cookies = cookiedict, headers=headers)
  
  vals = json.loads(str(get.text))

  parse_food(vals)
  


for food in food_type_list:
   
   outfile.write('\n'+food + ',\n')
   get_food_vals(food)
   outfile.write('\n,'*3)
outfile.close()


