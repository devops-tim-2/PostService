import json
from common.database import db_session
from models.models import User, Follow, Block
from service import post_service

class UserConsumer:
    def __init__(self, channel):
        self.exchange_name = 'user'
        self.channel = channel
        channel.exchange_declare(exchange=self.exchange_name, exchange_type='fanout')
        q = channel.queue_declare(queue='')
        channel.queue_bind(exchange=self.exchange_name, queue=q.method.queue)
        channel.basic_consume(queue=q.method.queue, on_message_callback=self.on_message, auto_ack=True)

    def on_message(self, ch, method, properties, body):
        try:
            data = json.loads(body)

            if properties.content_type == 'user.created':            
                user = User(id=data['id'], public=data['public'])
                db_session.add(user)
                db_session.commit()
            elif properties.content_type == 'user.deleted':
                User.query.get(data['id']).delete()
                Follow.query.filter(Follow.src == data['id']).delete()
                Follow.query.filter(Follow.dst == data['id']).delete()
                Block.query.filter(Block.src == data['id']).delete()
                Block.query.filter(Block.dst == data['id']).delete()
                db_session.commit()
                post_service.delete(data['id'])
            elif properties.content_type == 'user.updated':
                user = User.query.get(data['id'])
                if user.public != data['public']:
                    user.public = data['public']
                    db_session.commit()
            elif properties.content_type == 'user.follow.created':
                follow = Follow(id=data['id'], src=data['src'], dst=data['dst'], mute=data['mute'])
                db_session.add(follow)
                db_session.commit()
            elif properties.content_type == 'user.block.created':
                block = Block(id=data['id'], src=data['src'], dst=data['dst'])
                db_session.add(block)
                db_session.commit()
            elif properties.content_type == 'user.follow.updated':
                follow = Follow.query.get(data['id'])
                follow.mute = data['mute']
                db_session.commit()
        except Exception:
            # don't crash
            pass

class AdminConsumer:
    def __init__(self, channel):
        self.queue_name = 'admin'
        self.channel = channel
        channel.queue_declare(queue=self.queue_name)
        channel.basic_consume(queue=self.queue_name, on_message_callback=self.on_message, auto_ack=True)

    def on_message(self, ch, method, properties, body):
        try:
            data = json.loads(body)

            if properties.content_type == 'post.delete':
                post_service.delete(data['id'])
        except Exception:
            # don't crash
            pass
