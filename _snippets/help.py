data = {
    "dst-lan:帮助": {
        "prefix": "help",
        "body": "help",
        "description": " ※为避免登github,我后面会将补全提示和更新信息放在这里!\n --------------------\n ※触发/补全\n g+方法名/不常用全局方法查询(常用的可以直接敲出来,不常用的会被丢进g+里)\n com+组件名/不常用组件查询\n  \n contri+components/成为贡献者!(注释模板)\n lan+param/方法形参注释---$param: (param) <type> [desc] {others}\n lan+return/方法返回注释---$return: <type> [desc]\n --------------------\n ※其他/...\n 用户自定义注释/-- @用户名: 注释\n ※Todo\n 收集模组代码,计算api的使用频率,过低的api直接放进不常用方法中\n "
    },
    "成为贡献者:组件": {
        "prefix": "contri+components",
        "body": "components.${1:组件名}[\"${2:方法名}\"] = {\n\tparams = {\n\t\t-- 此处填参数,如果无参数,请留空\n\t\t-- param: 参数名(自动生成) explain: 参数说明(万能的群友们,请帮我注释吧) type: 参数类型\n\t\t-- {param = \"\", explain = \"\", type = \"\"},\n\n\t\t-- 参数为带参函数时\n\t\t-- {param = \"\", explain = \"\", type = \"function\",\n\t\t-- fn_params = {\n\t\t\t-- {param = \"\", explain = \"\", type = \"\"},\n\t\t-- },\n\t\t-- fn_returns = {\n\t\t\t-- {explain = \"\", type = \"\"},\n\t\t-- }\n\t\t$3\n\t},\n\treturns = {\n\t\t-- 此处填返回值,如果无返回值,请留空\n\t\t-- 返回格式 explain: 参数说明(万能的群友们,请帮我注释吧) type: 参数类型\n\t\t-- {explain = \"\", type = \"\"}\n\t\t$4\n\t},\n\ttips = \"$5\", -- 简明扼要的说明方法的用途\n\tauthor = \"$6\", -- 贡献者id (填上您的名字,作为贡献者,你的名字会出现在补全提示中)\n\t-- filepath = \"scripts/components/weapon\" -- 如果你觉得有必要标注出方法的路径和行数就写\n\t-- line = \"所在行数: 200\" -- 如果你觉得有必要标注出方法的路径和行数就写\n\t-- replace_body = \"\" -- 补全的代码块(这一项会替换掉默认补全,如果不会,请不要写) \n},",
        "description": "组件以外的单个方法也可以用此种形式来注释,成为贡献者,让饥荒社区变得更好吧~ 上不去github,也可以直接丢给我"
    }
} 