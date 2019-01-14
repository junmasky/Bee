from pyecharts import Gauge

"""
@project:Bee
@author:junma
@date:2019-01-14
"""

"""
安装主题插件 $ pip install echarts-themes-pypkg
主题：vintage、macarons、infographic、shine、roma、westeros、wonderland、chalk、halloween、essos、walden、purple-passion、romantic
"""

gauge = Gauge("仪表盘示例")
gauge.use_theme('macarons')
gauge.add("业务指标", "完成率", 66.66)
gauge.render('gauge_仪表盘.html')
