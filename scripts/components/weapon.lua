data = {

    ["OnRemoveFromEntity"] = {
        params = {

        },
        returns = {
            
        },
        tips = "",
        author = "",
    },
        
    ["SetDamage"] = {
        params = {
            {
                param = "dmg", explain = "伤害值或伤害函数", type = "number|function",
                params = {
                    {param = "inst", explain = "武器的inst", type = "table"},
                    {param = "attacker", explain = "攻击者的inst", type = "table"},
                    {param = "target", explain = "攻击目标的inst", type = "table"},
                },
            },

        },
        returns = {
            nil,
        },
        tips = "如果dmg为函数型参数，show me等信息模组无法显示正确的攻击力",
        author = "Runar",
    },
        
    ["SetRange"] = {
        params = {
            {param = "attack", explain = "", type = ""},
            {param = "hit", explain = "", type = ""},

        },
        returns = {
            
        },
        tips = "",
        author = "",
    },
        
    ["SetOnAttack"] = {
        params = {
            {param = "fn", explain = "", type = ""},

        },
        returns = {
            
        },
        tips = "",
        author = "",
    },
        
    ["SetOnProjectileLaunch"] = {
        params = {
            {param = "fn", explain = "", type = ""},

        },
        returns = {
            
        },
        tips = "",
        author = "",
    },
        
    ["SetOnProjectileLaunched"] = {
        params = {
            {param = "fn", explain = "", type = ""},

        },
        returns = {
            
        },
        tips = "",
        author = "",
    },
        
    ["SetProjectile"] = {
        params = {
            {param = "projectile", explain = "", type = ""},

        },
        returns = {
            
        },
        tips = "",
        author = "",
    },
        
    ["SetProjectileOffset"] = {
        params = {
            {param = "offset", explain = "", type = ""},

        },
        returns = {
            
        },
        tips = "",
        author = "",
    },
        
    ["SetElectric"] = {
        params = {
            {param = "damage_mult", explain = "", type = ""},
            {param = "wet_damage_mult", explain = "", type = ""},

        },
        returns = {
            
        },
        tips = "",
        author = "",
    },
        
    ["SetOverrideStimuliFn"] = {
        params = {
            {param = "fn", explain = "", type = ""},

        },
        returns = {
            
        },
        tips = "",
        author = "",
    },
        
    ["CanRangedAttack"] = {
        params = {

        },
        returns = {
            
        },
        tips = "",
        author = "",
    },
        
    ["SetAttackCallback"] = {
        params = {
            {param = "fn", explain = "", type = ""},

        },
        returns = {
            
        },
        tips = "",
        author = "",
    },
        
    ["GetDamage"] = {
        params = {
            {param = "attacker", explain = "", type = ""},
            {param = "target", explain = "", type = ""},

        },
        returns = {
            
        },
        tips = "",
        author = "",
    },
        
    ["OnAttack"] = {
        params = {
            {param = "attacker", explain = "", type = ""},
            {param = "target", explain = "", type = ""},
            {param = "projectile", explain = "", type = ""},

        },
        returns = {
            
        },
        tips = "",
        author = "",
    },
        
    ["LaunchProjectile"] = {
        params = {
            {param = "attacker", explain = "", type = ""},
            {param = "target", explain = "", type = ""},

        },
        returns = {
            
        },
        tips = "",
        author = "",
    },
        
}
return data