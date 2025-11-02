
import os
import json
class Config:
    def __init__(self):
        self.server=os.getenv("SERVER")
        self.value_deserializer=lambda v: json.loads(v.decode('utf-8'))
        self.auto_offset_reset='earliest'
        self.enable_auto_commit=True
        self.group= os.getenv("GROUP")
        self.value_serializer= lambda v: json.dumps(v).encode('utf-8')



    def set_auto_offset_reset(self, auto_offset_reset):
        self.auto_offset_reset=auto_offset_reset

    def get_configs(self) -> dict:
        config= {'bootstrap_servers':self.server,
                'value_deserializer': self.value_deserializer,
                'auto_offset_reset': self.auto_offset_reset,
                'enable_auto_commit': self.enable_auto_commit,
                'group_id': self.group}
        
        return config

    def get_configs_producer(self):
        config= {'bootstrap_servers':self.server,
                'value_serializer': self.value_serializer,}
        
        return config