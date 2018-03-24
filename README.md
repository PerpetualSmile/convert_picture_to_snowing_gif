# convert_picture_to_snowing_gif
给一张静态图片增加下雪动态效果，并生成gif效果图

![](https://raw.githubusercontent.com/PerpetualSmile/picture/master/picture_snow/snow.gif)

## Step One

- 使用python的turtle库绘制科赫雪花曲线

![](https://raw.githubusercontent.com/PerpetualSmile/picture/master/picture_snow/draw_snow.gif)

## Step Two

- 将雪花保存为png格式的带透明通道的图片
- 使用pygame加载出背景图和雪花图

## Step Three

- 使用pygame的精灵模块模拟出雪花下落的动态画面

## Step Four

- 在pygame的主循环中每次都保存画面
- 使用PIL库将前面保存的连续画面帧绘制成gif

