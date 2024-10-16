import typing, PIL
class BaseItem:
    def __init__(self, name:str, pos:tuple(float,float,int), texture:PIL.Image.Image, SysTag:dict(str:Any), UsrTag:dict(str:Any)):
        # 物品的物理属性
        self.pos = pos
        self.size = self.texture.size()
        a
        dsx

？为啥自动检查不好使了
我明明选了python格式为啥还是不报错