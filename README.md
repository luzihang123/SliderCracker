# 滑块验证码 js 破解

* 极验2

* 安居客:
    轨迹加密: AES CBC 模式, Pkcs7Padding补全,
    问题: 目前安居客已完全变成手势验证。

* 美团
* 京东:
    轨迹加密: 自定义算法。
    说明: 轨迹算法需要重写。
    
* 易盾:
    轨迹加密: 自定义算法(删除关键 js, 请自行补全)。
    
* 云片:
    轨迹算法: AES 加密轨迹, RSA 加密AES密钥与偏移量传递, 避免密钥泄露。
    说明: 验证码图像处理缺口定位成功率有待提高。
    
* 数美:
    轨迹加密: DES CBC模式, ZeroPadding 补全。
    说明: 当接口返回数据中 riskLevel 字段为 PASS 即为验证通过, 在之后的请求中携带 rid 即可。

* 携程
    轨迹加密: 固定密钥, 随机偏移量 AES 加密轨迹, md5 加密验签(删除关键js, 请自行补全)。
    
* 搜狐
    轨迹加密: RSA 加密。
    图像处理: 返回乱序图片, 前端: js drawImage() 方法还原; 处理: python 复写 js 生成正确位置 PIL 切割粘贴还原。
    js cookie: 
        接口: https://v4.passport.sohu.com/i/jf/code 。
        返回数据: js , 处理后生成 cookie jv 值。
        作用: 提高验证码通过几率。
    
* 虎牙
    轨迹加密: AES ECB模式, Pkcs7Padding补全。
    说明: 滑块通过后台未返回通过签名参数, 后续请求直接使用滑块标识ID code 作为 ticket 即可
   
* 爱奇艺安全盾
    轨迹加密: AES CBC 模式, Pkcs7Padding补全。(已删除部分关键js, 请自行补全)
    加密流程: 
        1、初始化密钥, 前端与后端约定加解密密钥, 包括 AES 密钥、hMacSHA256 密钥
            接口: https://qcaptcha.iqiyi.com/api/outer/sbox/sbox_init_key 。
            密钥生成: 根据当前时间戳生成随机32位字符串 r 和64位字符串 i, i 明文传输, r 经过RSA等一系列加密处理传输给服务器, 
                sha256 加密验签, 经过特定格式组合成参数 secure, 服务器接收确认参数无误返回 sr, sr 与 i、r 一起通过
                sha256 加密生成 AES 密钥与 hMacSHA256 密钥。
            返回数据说明: 
                sr: 用于生成密钥。
                sid: 用于前端传递用户行为加密数据时服务器判断用户滑动的是哪张验证码与密钥, 以便解密以及判断缺口是否拟合、行为是否异常等。
                sign: 签名参数, 用于前端判断是否服务器传回的响应报文。
        2、初始化验证码
            接口: https://qcaptcha.iqiyi.com/api/outer/verifycenter/initpage 。
            参数说明: 
                cryptSrcData: 根据 注册或登录失败返回的 token 与传递的 dfp 环境参数 AES 加密加上 hMacSHA256 签名生成。
                cryptVersion: 密钥初始化接口返回的 sid。
        3、最终验证
            接口: https://qcaptcha.iqiyi.com/api/outer/verifycenter/verify 。
            参数说明: 
                cryptSrcData: token、dfp、轨迹等信息 AES 加密加上 hMacSHA256 签名生成。
                cryptVersion: 密钥初始化接口返回的 sid。
    图像处理: 接口返回还原数组, 前端: 经过 js 处理后 drawImage() 方法还原; 处理: python 复写 js 生成正确位置 PIL 切割粘贴还原。
                 
* 完美世界通行证
    轨迹加密: AES CBC模式, Pkcs7Padding补全。
    图像处理: 接口返回还原数组, 前端: js 处理生成 css 插入 html, css 还原; 处理: python 复写 js 生成正确位置 PIL 切割粘贴还原。
    说明: 轨迹需要重写。

* 螺丝帽点选验证
    轨迹加密: AES CBC 模式, ZeroPadding补全。
    图像处理: 接口返回还原数组, 前端: js 处理生成 css 插入 html, css 还原; 处理: python 复写 js 生成正确位置 PIL 切割粘贴还原。
    说明: 点选定位使用超级鹰打码平台, 请自行更换超级鹰账号密码。
    

环境依赖
--------

* 使用 execjs 执行 js, 安装: pip install PyExecjs 。 
* python 复写的加密使用的包为 pycryptodemo, 安装: pip install pycryptodemo 。
* execjs 执行环境为 node.js。自行下载安装 node.js。
  注意: 安装完毕后, 使用 execjs.get().name 判断运行环境是否已成功切换为 'Node.js(V8)', 若未切换成功, 使用 os.environ["EXECJS_RUNTIME"] = "Node" 切换。
* 使用 PIL 结合 cv2 进行图像处理识别, 安装: pip install pillow, pip install cv2。

结果展示
--------

* 极验2
![image](https://github.com/Esbiya/SliderCracker/blob/master/view/geetest2.png)

* 安居客
![image](https://github.com/Esbiya/SliderCracker/blob/master/view/anjuke.png)

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

* 螺丝帽
![image](https://github.com/Esbiya/SliderCracker/blob/master/view/luosimao.png)

公告
--------

该项目仅供学习参考, 请勿用作非法用途! 如若涉及侵权, 请联系2995438815@qq.com/18829040039@163.com, 收到必删除! 