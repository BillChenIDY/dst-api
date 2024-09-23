import re,pyperclip

SPACE = ' '
SEPERATOR = ['-'*20]
BR = [' '] #换行
data = [
    ['※为避免登github,我后面会将补全提示和更新信息放在这里!'],
    SEPERATOR,
    ['※触发','补全'],
    ['p+预制物id',r'预制物id补全,可以输中文译名查找'],
    ['g+方法名',r'不常用全局方法查询(常用的可以直接敲出来,不常用的会被丢进g+里)'],
    ['com+组件名',r'不常用组件查询'],
    ['正常触发方法+i',r'启发模式:提供一些快捷代码块'],
    BR,
    ['contri+components',r'成为贡献者!(注释模板)'],
    ['lan+param',r'方法形参注释---$param: (param) <type> [desc] {others}'],
    ['lan+return',r'方法返回注释---$return: <type> [desc]'],
    SEPERATOR,
    ['※其他','...'],
    ['用户自定义注释',r'-- @用户名: 注释'],
    ['※Todo'],
    ['收集模组代码,计算api的使用频率,过低的api直接放进不常用方法中']
]

res = ' '
for items in data:
    for content in items:
        res += content + '/'
    res = res.rstrip('/')
    res += '\\n '

#
with open('./version.txt','r',encoding='utf-8') as f:
    version = f.read()
        
version = 'v' + version.strip(' ')
#
res = ' ※插件版本: '+ version + '\\n' + res

snp = f"""
    "dst-lan:帮助": {{
        "prefix": "help",
        "body": "help",
        "description": "{res}"
    }},
"""
pyperclip.copy(snp)
print(res)
