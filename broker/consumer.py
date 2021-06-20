import json

import sqlalchemy
from sqlalchemy.orm import sessionmaker, scoped_session
from os import environ
engine = sqlalchemy.create_engine(f'{environ.get("DB_TYPE")}+{environ.get("DB_DRIVER")}://{environ.get("DB_USER")}:{environ.get("DB_PASSWORD")}@{environ.get("DB_HOST")}/{environ.get("DB_NAME")}')
Session = scoped_session(sessionmaker(bind=engine))

class UserConsumer:
    def __init__(self, channel):
        self.queue_name = 'user'
        self.channel = channel
        channel.queue_declare(queue=self.queue_name)
        channel.basic_consume(queue=self.queue_name, on_message_callback=self.on_message, auto_ack=True)

    def on_message(self, ch, method, properties, body):
        data = json.loads(body)

        if properties.content_type == 'user.created':            
            with engine.connect() as con:
                con.execute(sqlalchemy.text('INSERT INTO public.user (id) VALUES (:val)'), val=data['id'])
        elif properties.content_type == 'user.deleted':
            with engine.connect() as con:
                con.execute(sqlalchemy.text('DELETE FROM public.user WHERE id=:val'), val=data['id'])
        elif properties.content_type == 'user.follow.created':
            with engine.connect() as con:
                con.execute(sqlalchemy.text('INSERT INTO public.follow (id, src, dst, mute) VALUES (:id, :src, :dst, :mute)'), id=data['id'], src=data['src'], dst=data['dst'], mute=data['mute'])
        elif properties.content_type == 'user.block.created':
            with engine.connect() as con:
                con.execute(sqlalchemy.text('INSERT INTO public.block (id, src, dst) VALUES (:id, :src, :dst)'), id=data['id'], src=data['src'], dst=data['dst'])
        elif properties.content_type == 'user.follow.updated':
            with engine.connect() as con:
                con.execute(sqlalchemy.text('UPLDATE public.follow SET mute=:mute WHERE id=:id'), id=data['id'], mute=data['mute'])

class AdminConsumer:
    def __init__(self, channel):
        self.queue_name = 'admin'
        self.channel = channel
        channel.queue_declare(queue=self.queue_name)
        channel.basic_consume(queue=self.queue_name, on_message_callback=self.on_message, auto_ack=True)

    def on_message(self, ch, method, properties, body):
        data = json.loads(body)

        if properties.content_type == 'post.delete':
            with engine.connect() as con:
                con.execute(sqlalchemy.text('DELETE FROM public.post WHERE id=:val'), val=data['id'])

