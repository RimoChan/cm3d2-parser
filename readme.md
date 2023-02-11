# cm3d2-parser

我最近玩了3D定制女仆，自己做MOD的时候经常想做一些批量处理，比如批量换材质、颜色，批量修改参数等等，却发现没有Python包可以直接读取MOD文件。

但是好在我非常聪明，所以就自己写了一个！


## 安装

首先你需要1个Python3.8以上版本，然后——

```sh
pip install git+https://github.com/RimoChan/cm3d2-parser.git
```

这样就装好了。


## 接口

```python
from cm3d2_parser import cm3d2_load, cm3d2_dump
```

首先import。


```python
def cm3d2_load(p: PathLike) -> Union[Mate, Menu, Texture]: ...
```

这个函数可以读取`.mate`/`.menu`/`.tex`文件，返回一个`Mate`、`Menu`或`Texture`对象。


```python
def cm3d2_dump(p: PathLike, data: Union[Mate, Menu, Texture]): ...
```

这个函数可以把`Mate`、`Menu`或`Texture`对象写入`.mate`/`.menu`/`.tex`文件。


## 例子

```python
from cm3d2_parser import cm3d2_load, cm3d2_dump
menu = cm3d2_load('./CyberMask/Armor-CyberMask_i_.menu')
print(menu)
```

可以得到一个典型的`Menu`对象的结构，如下：

```python
Menu(
    version=1000,
    text_path='Armor-CyberMask_i_.txt',
    name='Armor-CyberMask',
    category='accHana',
    description='Armor-CyberMask',
    attrs={
        'メニューフォルダ': [['DRESS']],
        'category': [['accHana']],
        'catno': [['0']],
        '属性追加': [['所持数表示しない']],
        'priority': [['9999']],
        'name': [['Cyberpunk-Mask-Original-Color']],
        'setumei': [['A Cyberpunk Style Mask']],
        'icons': [['Armor-CyberMask_i_.tex']],
        'onclickmenu': [[]],
        'additem': [['Armor-CyberMask.model', 'accHana']],
        'マテリアル変更': [['accHana', '0', 'Armor-CyberMask.mate']],
        'テクスチャ変更': [['accHana', '0', '_MainTex', 'Armor-CyberMask.tex']]
    }
)
```

然后就可以修改对应的属性，再用`cm3d2_dump`写回去啦。


## 结束

就这样，我要去和女仆亲热了，大家88！

还有这个包里的一些代码是对着<https://github.com/CM3D2user/Blender-CM3D2-Converter>写的，但是因为我是メスガキ，所以不会感谢他。
