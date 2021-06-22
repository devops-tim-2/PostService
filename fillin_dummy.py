from models.models import Post, User
from common.database import db_session

user1_public = User(public=True)
user2_public = User(public=True)
user3_private = User(public=False)
user4_private = User(public=False)

db_session.add(user1_public)
db_session.add(user2_public)
db_session.add(user3_private)
db_session.add(user4_private)
db_session.commit()

post1_user1 = Post(description='Photo of the Day: Taking on #NationalSelfieDay', image_url='http://www.nistagram.com/CQZOZWynVfZ.jpg', user_id=user1_public.id)
post2_user1 = Post(description='Party laps + filming hacks for #SkateboardingDay', image_url='http://www.nistagram.com/CQY2rQlnsxv.jpg', user_id=user1_public.id)

post1_user2 = Post(description='Photo of the Day: Dads lift us up', image_url='http://www.nistagram.com/CQWlqL8gzMc.jpg', user_id=user2_public.id)
post2_user2 = Post(description='Photo of the Day: Sunflower season is upon us', image_url='http://www.nistagram.com/CQJxF37HCz0.jpg', user_id=user2_public.id)
post3_user2 = Post(description='Photo of the Day: Posted up for the weekend', image_url='http://www.nistagram.com/CQUKbjjHKzM.jpg', user_id=user2_public.id)

post1_user3 = Post(description='Light up the night... or trail, or garage, or anywhere that\'s dark', image_url='http://www.nistagram.com/CQJaKwMHsL_.jpg', user_id=user3_private.id)
post2_user3 = Post(description='Photo of the Day: Magic sandbar selfie', image_url='http://www.nistagram.com/CQRfhHln-8O.jpg', user_id=user3_private.id)

post1_user4 = Post(description='Soar alongside scenic mountains', image_url='http://www.nistagram.com/CQO8o_6nyN7.jpg', user_id=user4_private.id)
post2_user4 = Post(description='Photo of the Day: Work less, ride more', image_url='http://www.nistagram.com/CQOh3kdN3Tg.jpg', user_id=user4_private.id)
post3_user4 = Post(description='Photo of the Day: Enjoying the show', image_url='http://www.nistagram.com/CQGzBtFrWjW.jpg', user_id=user4_private.id)

db_session.add(post1_user1)
db_session.add(post2_user1)
db_session.add(post1_user2)
db_session.add(post2_user2)
db_session.add(post3_user2)
db_session.add(post1_user3)
db_session.add(post2_user3)
db_session.add(post1_user4)
db_session.add(post2_user4)
db_session.add(post3_user4)
db_session.commit()