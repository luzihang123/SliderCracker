# 各类验证码 js 破解

* Vaptcha<br>
    * 轨迹加密: 自定义加密。<br>
    * 说明: <br>
        * 使用超级鹰打码平台识别手势, 返回四个坐标点, 根据坐标点绘制轨迹, 自行更换超级鹰用户名密码。<br>
        * 轨迹来源: [点击这里](https://github.com/clllanqing/solve_captcha/blob/master/wuba/utils.py), 通过率不高, 自行改写。

* 极验2

* 安居客<br>
    * 轨迹加密: AES CBC 模式, Pkcs7Padding 填充。<br>
    * 问题: 目前安居客已完全变成手势验证。
    * 补充: 参考58同城, 两者为同一套验证码。

* 58同城<br>
    * 轨迹加密: AES CBC 模式, Pkcs7Padding 填充。<br>
    * 说明: 
        * 滑块轨迹算法已删除, 请自行编写, 或调用安居客的轨迹（收集自别人的轨迹)。<br>
        * 增加点选验证类型, 超级鹰识别, 自行更换超级鹰用户名密码。
        * 增加手势验证类型, 轨迹来源: [点击这里](https://github.com/clllanqing/solve_captcha/blob/master/wuba/utils.py)。
    
* 美团

* 京东<br>
    * 轨迹加密: 自定义算法: jd_slider.js 。<br>
    * 说明: 轨迹算法需要重写。
    
* 易盾<br>
    * 轨迹加密: 自定义算法: yd_slider.js、generate_fp.js (删除关键 js, 请自行补全, 如有需要, 且是正当需求, 请提issue或者发邮件给我)。
    
* 云片<br>
    * 轨迹算法: AES 加密轨迹, RSA 加密AES密钥与偏移量传递, 避免密钥泄露。<br>
    * 说明: 验证码图像处理缺口定位成功率有待提高。
    
* 数美<br>
    * 轨迹加密: DES CBC模式, ZeroPadding 填充。<br>
    * 说明: 当接口返回数据中 riskLevel 字段为 PASS 即为验证通过, 在之后的请求中携带 rid 即可。

* 携程<br>
    * 轨迹加密: 固定密钥, 随机偏移量 AES 加密轨迹, md5 加密验签(删除关键js, 请自行补全, 如有需要, 且是正当需求, 请提issue或者发邮件给我)。
    
* 搜狐<br>
    * 轨迹加密: RSA 加密。<br>
    * 图像处理: 返回乱序图片。<br>
        * 前端: js drawImage() 方法还原。<br>
        * 处理: python 复写 js 生成正确位置 PIL 切割粘贴还原。<br>
    * js cookie: <br>
        * 接口: https://v4.passport.sohu.com/i/jf/code 。<br>
        * 返回数据: js , 处理后生成 cookie jv 值。<br>
        * 作用: 提高验证码通过几率。<br>
    
* 虎牙<br>
    * 轨迹加密: AES ECB模式, Pkcs7Padding 填充。<br>
    * 说明: 滑块通过后台未返回通过签名参数, 后续请求直接使用滑块标识ID code 作为 ticket 即可
   
* 爱奇艺安全盾<br>
    * 轨迹加密: AES CBC 模式, Pkcs7Padding 填充。(已删除部分关键js, 请自行补全, 如有需要, 且是正当需求, 请提issue或者发邮件给我)<br>
    * 加密流程: <br>
        * 1、初始化密钥, 前端与后端约定加解密密钥, 包括 AES 密钥、hMacSHA256 密钥<br>
            * 接口: https://qcaptcha.iqiyi.com/api/outer/sbox/sbox_init_key 。<br>
            * 密钥生成: 根据当前时间戳生成随机32位字符串 r 和64位字符串 i, i 明文传输, r 经过RSA等一系列加密处理传输给服务器, 再通过 sha256 加密验签, 经过特定格式组合成参数 secure, 服务器接收确认参数无误返回 sr, sr 与 i、r 一起通过sha256 加密生成 AES 密钥与 hMacSHA256 密钥。<br>
            * 返回数据说明: <br>
                * sr: 用于生成密钥。<br>
                * sid: 用于前端传递用户行为加密数据时服务器判断用户滑动的是哪张验证码与密钥, 以便解密以及判断缺口是否拟合、行为是否异常等。<br>
                * sign: 签名参数, 用于前端判断是否服务器传回的响应报文。<br>
        * 2、初始化验证码<br>
            * 接口: https://qcaptcha.iqiyi.com/api/outer/verifycenter/initpage 。<br>
            * 参数说明: <br>
                * cryptSrcData: 根据 注册或登录失败返回的 token 与传递的 dfp 环境参数 AES 加密加上 hMacSHA256 签名生成。<br>
                * cryptVersion: 密钥初始化接口返回的 sid。<br>
        * 3、最终验证<br>
            * 接口: https://qcaptcha.iqiyi.com/api/outer/verifycenter/verify 。<br>
            * 参数说明: <br>
                * cryptSrcData: token、dfp、轨迹等信息 AES 加密加上 hMacSHA256 签名生成。<br>
                * cryptVersion: 密钥初始化接口返回的 sid。<br>
    * 图像处理: 接口返回还原数组。
        * 前端: 经过 js 处理后 drawImage() 方法还原。
        * 处理: python 复写 js 生成正确位置 PIL 切割粘贴还原。
                 
* 完美世界通行证<br>
    * 轨迹加密: AES CBC模式, Pkcs7Padding 填充。<br>
    * 图像处理: 接口返回还原数组。<br>
        * 前端: js 处理生成 css 插入 html, css 还原<br>
        * 处理: python 复写 js 生成正确位置 PIL 切割粘贴还原。<br>
    * 说明: 轨迹需要重写。

* 同盾滑块<br>
    * 轨迹加密: 目前发现有两套加密, 一套自定义加密, 一套 AES CBC Pkcs7Padding 加密, 加密代码混淆每天自动生成, 轨迹加密隐藏很深, 调试难度大。<br>
    * 图像处理: 接口返回还原数组加密数据。<br>
        * 前端: js 解密处理, getImageData() 方法切割乱序验证码, putImageData() 方法绘制正确验证码。<br>
        * 处理: python 复写 js, PIL 切割粘贴还原。<br>
    * 说明: 轨迹已删除。
    
* 螺丝帽点选验证<br>
    * 轨迹加密: AES CBC 模式, ZeroPadding 填充。<br>
    * 图像处理: 接口返回还原数组。<br>
        * 前端: js 处理生成 css 插入 html, css 还原。<br>
        * 处理: python 复写 js 生成正确位置 PIL 切割粘贴还原。<br>
    * 说明: 点选定位使用超级鹰打码平台, 请自行更换超级鹰账号密码。
    
* 猎聘点选验证<br>
    * 轨迹加密: AES CBC 模式, Pkcs7Padding 填充。<br>
    * 图像处理: js 生成还原数组(固定不变)。<br>
        * 前端: js 处理生成 css 插入 html, css 还原。<br>
        * 处理: execjs 执行 js 生成正确位置 PIL 切割粘贴还原。<br>
    * 说明:<br> 
        * 点选定位使用超级鹰打码平台, 请自行更换超级鹰账号密码<br>
        * 鼠标点击移动数据伪造方法已删除, 如有需要, 且是正当需求, 请提issue或者发邮件给我。

* 蘑菇街旋转图片朝上验证<br>
    * 轨迹加密: 自定义加密算法, mgj_encrypt.js、get_auth.js 。<br>
    * 说明:<br>
        * 未进行图像识别, 人工手动输入旋转点击图片次数。
        * 轨迹伪造方法已删除, 请自行编写, 如有需要, 且是正当需求, 请提issue或者发邮件给我。

* 大街注册点选
    * 点选位置加密: AES ECB模式。<br>
    * 图像处理: 接口返回加密数据, AES 解密获取还原数组。<br>
        * 前端: js 处理生成 css 插入 html, css 还原。<br>
        * 处理: python 复写 js 生成正确位置 PIL 切割粘贴还原。<br>
    * 说明:<br> 
        * 点选定位使用超级鹰打码平台, 请自行更换超级鹰账号密码<br> 
    
环境依赖
--------

``` shell script
$ pip install -r ./requirements.txt
```

* 使用 execjs 执行 js。 
* python 复写的加密使用的包为 pycryptodemo。
* execjs 执行环境为 node.js。自行下载安装 node.js。
  注意: 安装完毕后, 使用 execjs.get().name 判断运行环境是否已成功切换为 'Node.js(V8)', 若未切换成功, 使用 os.environ["EXECJS_RUNTIME"] = "Node" 切换。
* 使用 PIL 结合 cv2 进行图像处理识别。

结果展示
--------

* Vaptcha
![image](https://github.com/Esbiya/SliderCracker/blob/master/view/vaptcha.png)

* 极验2
![image](https://github.com/Esbiya/SliderCracker/blob/master/view/geetest2.png)

* 安居客
![image](https://github.com/Esbiya/SliderCracker/blob/master/view/anjuke.png)

* 58同城
![image](https://github.com/Esbiya/SliderCracker/blob/master/view/58city.png)

* 美团
![image](https://github.com/Esbiya/SliderCracker/blob/master/view/meituan.png)

* 易盾
![image](https://github.com/Esbiya/SliderCracker/blob/master/view/yidun.png)

* 云片
![image](https://github.com/Esbiya/SliderCracker/blob/master/view/yunpian.png)

* 数美
![image](https://github.com/Esbiya/SliderCracker/blob/master/view/shumei.png)

* 携程
![image](https://github.com/Esbiya/SliderCracker/blob/master/view/xiecheng.png)

* 搜狐
![image](https://github.com/Esbiya/SliderCracker/blob/master/view/souhu.png)

* 虎牙
![image](https://github.com/Esbiya/SliderCracker/blob/master/view/huya.png)

* 爱奇艺
![image](https://github.com/Esbiya/SliderCracker/blob/master/view/aiqiyi.png)

* 同盾
![image](https://github.com/Esbiya/SliderCracker/blob/master/view/tongdun.png)

* 螺丝帽
![image](https://github.com/Esbiya/SliderCracker/blob/master/view/luosimao.png)

* 猎聘
![image](https://github.com/Esbiya/SliderCracker/blob/master/view/liepin.png)

* 蘑菇街
![image](https://github.com/Esbiya/SliderCracker/blob/master/view/mogujie.png)

* 大街
![image](https://github.com/Esbiya/SliderCracker/blob/master/view/dajie.png)


公告
--------

该项目仅供学习参考, 请勿用作非法用途! 如若涉及侵权, 请联系2995438815@qq.com/18829040039@163.com, 收到必删除! 