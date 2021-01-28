import redis
import string
import random

ahp = string.ascii_lowercase + string.digits

token_string = ''

token = token_string.join([random.choice(ahp) for n in range(128)])
token_key = 'user_key'

rds = redis.StrictRedis(port=6378)

rds.set(token_key, token)


print(token)
print(token[:5])
print(token[10:16])

# token
user_data = {
    'user_id': '123'

}

print('_'.join(['user', 'token', user_data['user_id']]))


#  request

real_token = rds.get(token_key)
if not token == real_token.decode():
    print("token 不一致")

else:
    print("token 一致")