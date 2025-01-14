data = {
    "创建默认的类": {
        "prefix": "Class1",
        "body": "local ${1:ClassName} = Class(function(self, inst)\n\tself.inst = inst \nend)",
        "description": "添加代码片段 local ClassName = Class(function(self, inst)\n\tself.inst = inst \nend)"
    },
    "创建带有触发属性的类": {
        "prefix": "Class2",
        "body": "local ${1:ClassName} = Class(function(self, inst)\n\tself.inst = inst\nend,\nnil,\n{\n})",
        "description": "local ClassName = Class(function(self, inst)\n\tself.inst = inst\nend,\nnil,\n{\n})"
    },
    
 
    "检查全局变量": {
        "prefix": "rawget",
        "body": "if rawget(GLOBAL, \"${1:TheSim}\") then\n\t${0}\nend",
        "description": "不触发任何元方法的情况下 获取 table[index] 的值.判断是否存在全局变量"
    },
    "全局模拟器": {
        "prefix": "TheSim",
        "body": "TheSim",
        "description": "userdata类型,是c层暴露给lua里使用的,游戏系统本身"
    },
    "查找指定范围内实体": {
        "prefix": "TheSim:FindEntities",
        "body": "TheSim:FindEntities(x, y or 0, z, radius or 4, must_have_tags, cant_have_tags, must_have_one_of_tags)",
        "description": "must_have_tags:必须具有全部标签的, cant_have_tags:从结果中排除标签的, must_have_one_of_tags:至少有一个标签的"
    },
    "输入": {
        "prefix": "TheInput",
        "body": "TheInput",
        "description": "(仅客户端的)是集成了各种输入方法的类.与TheInputProxy有关"
    },
    "前端": {
        "prefix": "TheFrontEnd",
        "body": "TheFrontEnd",
        "description": "(仅客户端的)通常在modworldgenmain.lua文件或者Ui文件里"
    },
    "摄像机": {
        "prefix": "TheCamera",
        "body": "TheCamera",
        "description": "(仅客户端的)是游戏中玩家身后的摄像机一般是跟随玩家."
    },
    "当前客户端玩家": {
        "prefix": "ThePlayer",
        "body": "ThePlayer",
        "description": "(仅客户端)是玩家实体的引用,在服务器上值为nil"
    },
    "当前世界": {
        "prefix": "TheWorld",
        "body": "TheWorld",
        "description": "是世界实体的引用,双端都有.每个独立线程都是有一个."
    },
    "全局网络单例": {
        "prefix": "TheNet",
        "body": "TheNet",
        "description": "userdata类型,是与网络相关联的内容"
    },
    "当前分片": {
        "prefix": "TheShard",
        "body": "TheShard",
        "description": "userdata类型,与配置相关,TheShard:IsMaster()判断是否为主世界"
    },
    "常量表": {
        "prefix": "TUNING",
        "body": "TUNING",
        "description": "各类的数值存放在这个表里"
    },
    "字符串集": {
        "prefix": "STRINGS",
        "body": "STRINGS",
        "description": "各类的字符串存放在这个表里"
    },
    "全局表": {
        "prefix": "GLOBAL",
        "body": "GLOBAL",
        "description": "指向饥荒本体环境的全局表"
    },
    # "注册服务器rpc": {
    #     "prefix": "AddModRPCHandler",
    #     "body": "AddModRPCHandler(\"${1:name}\",\"${2:$1}\", function(player, str)\n\tif player == nil or str == nil then return end\n\tlocal success, savedata = RunInSandboxSafe(str)\n\tif success then\n\n\telse\n\t\tprint(\"服务器接收RPC失败\")\n\tend\nend)",
    #     "description": "参数1:命名空间;参数2:RPC名称;参数3:执行函数(形参1:玩家<code>是发起的客机对之服务器玩家</code>, ...).前两个是唯一标识符"
    # },
    # "发送服务器RPC调用": {
    #     "prefix": "SendModRPCToServer",
    #     "body": "SendModRPCToServer(GetModRPC(\"${1:name}\", \"${2:$1}\"), DataDumper({\"参数\"}, nil, true))",
    #     "description": "从客机发送指令给主机.参数1:通过GetModRPC(形参1:命名空间,形参2:RPC名称)获取对应RPC;参数2:附带参数对应str"
    # },
    # "注册客户端rpc": {
    #     "prefix": "AddClientModRPCHandler",
    #     "body": "AddClientModRPCHandler(\"${1:name}\",\"${2:$1}\", function(str)\n\tif str == nil then return end\n\tlocal success, savedata = RunInSandboxSafe(str)\n\tif success then\n\n\telse\n\t\tprint(\"客户端接收RPC失败\")\n\tend\nend)",
    #     "description": "参数1:命名空间;参数2:RPC名称;参数3:执行函数(...).前两个是唯一标识符"
    # },
    # "发送客户端RPC调用": {
    #     "prefix": "SendModRPCToClient",
    #     "body": "SendModRPCToClient(GetClientModRPC(\"${1:name}\", \"${2:$1}\"), userid or nil, DataDumper({\"参数\"}, nil, true))",
    #     "description": "从主机发送指令给客机.参数1:GetClientModRPC(形参1:命名空间,形参2:RPC名称)获取对应RPC;参数2:userid<code>可为nil|字符串|字符串表</code>;参数3:附带参数对应str"
    # },
    # "注册服务器分片rpc": {
    #     "prefix": "AddShardModRPCHandler",
    #     "body": "AddShardModRPCHandler(\"${1:name}\",\"${2:$1}\", function(wordid, str)\n\tif wordid == nil or str == nil then return end\n\tlocal success, savedata = RunInSandboxSafe(str)\n\tif success then\n\n\telse\n\t\tprint(\"分片接收RPC失败\")\n\tend\nend)",
    #     "description": "参数1:命名空间;参数2:RPC名称;参数3:执行函数(...).前两个是唯一标识符"
    # },
    # "发送服务器其他世界RPC调用": {
    #     "prefix": "SendModRPCToShard",
    #     "body": "SendModRPCToShard(GetShardModRPC(\"${1:name}\", \"${2:$1}\"), sender_list or nil, DataDumper({\"参数\"}, nil, true))",
    #     "description": "从主机分片发送指令给主机其他分片.参数1:GetShardModRPC(形参1:命名空间,形参2:RPC名称)获取对应RPC;参数2:sender_list<code>可为nil|字符串|字符串表</code>;参数3:附带参数对应str"
    # },
    "网络变量": {
        "prefix": "net_bool",
        "body": "inst.${1:_xx} = net_bool(inst.GUID, \"${2:$1}\",\"${3:$1}\")",
        "description": "仅两个值true|false"
    },
    "网络变量_2": {
        "prefix": "net_tinybyte",
        "body": "inst.${1:_xx} = net_tinybyte(inst.GUID, \"${2:$1}\",\"${3:$1}\")",
        "description": "数值范围是[0..7]"
    },
    "网络变量_3": {
        "prefix": "net_smallbyte",
        "body": "inst.${1:_xx} = net_smallbyte(inst.GUID, \"${2:$1}\",\"${3:$1}\")",
        "description": "数值范围是[0..63]"
    },
    "网络变量_4": {
        "prefix": "net_byte",
        "body": "inst.${1:_xx} = net_byte(inst.GUID, \"${2:$1}\",\"${3:$1}\")",
        "description": "数值范围是[0..255]"
    },
    "网络变量_5": {
        "prefix": "net_shortint",
        "body": "inst.${1:_xx} = net_shortint(inst.GUID, \"${2:$1}\",\"${3:$1}\")",
        "description": "数值范围是[-32767..32767]"
    },
    "网络变量_6": {
        "prefix": "net_ushortint",
        "body": "inst.${1:_xx} = net_ushortint(inst.GUID, \"${2:$1}\",\"${3:$1}\")",
        "description": "数值范围是[0..65535]"
    },
    "网络变量_7": {
        "prefix": "net_int",
        "body": "inst.${1:_xx} = net_int(inst.GUID, \"${2:$1}\",\"${3:$1}\")",
        "description": "数值范围是[-2147483647..2147483647]"
    },
    "网络变量_8": {
        "prefix": "net_uint",
        "body": "inst.${1:_xx} = net_uint(inst.GUID, \"${2:$1}\",\"${3:$1}\")",
        "description": "数值范围是[0..4294967295]"
    },
    "网络变量_9": {
        "prefix": "net_float",
        "body": "inst.${1:_xx} = net_float(inst.GUID, \"${2:$1}\",\"${3:$1}\")",
        "description": "32位浮点数"
    },
    "网络变量_10": {
        "prefix": "net_hash",
        "body": "inst.${1:_xx} = net_hash(inst.GUID, \"${2:$1}\",\"${3:$1}\")",
        "description": "可以通过哈希或字符串设置（自动转换为hash），但仅在读取时返回哈希值。网络成本与net_uint相同"
    },
    "网络变量_11": {
        "prefix": "net_string",
        "body": "inst.${1:_xx} = net_string(inst.GUID, \"${2:$1}\",\"${3:$1}\")",
        "description": "可变长度字符串"
    },
    "网络变量_12": {
        "prefix": "net_entity",
        "body": "inst.${1:_xx} = net_entity(inst.GUID, \"${2:$1}\",\"${3:$1}\")",
        "description": "实体实例"
    },
    "网络变量_13": {
        "prefix": "net_bytearray",
        "body": "inst.${1:_xx} = net_bytearray(inst.GUID, \"${2:$1}\",\"${3:$1}\")",
        "description": "最大31,成员8-bit(与net_byte相当)"
    },
    "网络变量_14": {
        "prefix": "net_smallbytearray",
        "body": "inst.${1:_xx} = net_smallbytearray(inst.GUID, \"${2:$1}\",\"${3:$1}\")",
        "description": "最大31,成员6-bit(与net_smallbyte相当)"
    },
    "网络变量_15": {
        "prefix": "net_ushortarray",
        "body": "inst.${1:_xx} = net_ushortarray(inst.GUID, \"${2:$1}\",\"${3:$1}\")",
        "description": "最大31,成员16-bit(与net_ushortint相当)"
    },
    "添加预制体信息": {
        "prefix": "STRINGS+PREFAB",
        "body": "STRINGS.NAMES.${1:PREFABNAME} = \"${2:$1}\"\nSTRINGS.RECIPE_DESC.${3:$1} = \"${4:$1} 科技栏描述\"\nSTRINGS.CHARACTERS.GENERIC.DESCRIBE.${5:$1} = \"${6:$1} 的检查描述\"",
        "description": "设置预制体名称,科技栏描述,检查描述"
    },
    "设置mod环境": {
        "prefix": "GLOBAL+env",
        "body": "GLOBAL.setmetatable(env,{__index=function(t,k) return GLOBAL.rawget(GLOBAL,k) end})",
        "description": "设置在mod环境中可以直接访问本体环境中的全局参数"
    },
    "打印表": {
        "prefix": "dumptable",
        "body": "print(dumptable(${1:table}, 1, 5))",
        "description": "打印表1~5层"
    },
    "三维向量": {
        "prefix": "Vector3",
        "body": "Vector3(${1:0}, ${2:$1}, ${3:$1})",
        "description": "创建三维向量"
    },

    "BufferedAction": {
        "prefix": "BufferedAction",
        "body": "BufferedAction",
        "description": "dst-未定义的"
    },
    "创建缓冲动作": {
        "prefix": "BufferedAction+",
        "body": "local action = BufferedAction(inst, target or nil, ACTIONS.${1:XXX}, invobject or nil, pos or nil, nil, distance or nil)",
        "description": "添加一个缓冲动作代码片段"
    },
    "CreateEntity": {
        "prefix": "CreateEntity",
        "body": "CreateEntity",
        "description": "dst-未定义的"
    },
    "deepcopy": {
        "prefix": "deepcopy",
        "body": "deepcopy",
        "description": "dst-未定义的"
    },
    "require": {
        "prefix": "require",
        "body": "require",
        "description": "dst-未定义的"
    },
    "GUID": {
        "prefix": "GUID",
        "body": "GUID",
        "description": "dst-未定义的"
    },
    "HUD": {
        "prefix": "HUD",
        "body": "HUD",
        "description": "dst-未定义的"
    },
    "prefab": {
        "prefix": "prefab",
        "body": "prefab",
        "description": "dst-未定义的"
    },
    "animover": {
        "prefix": "animover",
        "body": "animover",
        "description": "dst-未定义的"
    },
    "idle": {
        "prefix": "idle",
        "body": "idle",
        "description": "dst-未定义的"
    },
    "GoToState": {
        "prefix": "GoToState",
        "body": "GoToState",
        "description": "dst-未定义的"
    },
    "HasStateTag": {
        "prefix": "HasStateTag",
        "body": "HasStateTag",
        "description": "dst-未定义的"
    },
    "Update": {
        "prefix": "Update",
        "body": "Update",
        "description": "dst-未定义的"
    },
    "OnLoad": {
        "prefix": "OnLoad",
        "body": "OnLoad",
        "description": "dst-未定义的"
    },
    "OnSave": {
        "prefix": "OnSave",
        "body": "OnSave",
        "description": "dst-未定义的"
    },

    "GetDebugString": {
        "prefix": "GetDebugString",
        "body": "GetDebugString",
        "description": "dst-未定义的"
    },
    "GetTime": {
        "prefix": "GetTime",
        "body": "GetTime",
        "description": "dst-未定义的"
    },
    "帧": {
        "prefix": "FRAMES",
        "body": "FRAMES",
        "description": "常量,代表一帧"
    },
    "是否参与保存": {
        "prefix": "persists",
        "body": "persists",
        "description": "默认值为true.修改实体属性为false,那么不会被保存下来"
    },

} 