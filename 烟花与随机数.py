import numpy as np
from js import document, window
from pyodide.ffi import create_proxy

# 定义显示随机数的函数
def show_random(event=None):
    # 使用 NumPy 生成一个随机数
    random_num = np.random.random()
    random_str = f"Random Number: {random_num:.5f}"  # 格式化为小数点后 5 位
    document.getElementById("random-number").innerHTML = random_str

    # 触发烟花效果
    window.triggerFireworks()

# 创建代理函数并绑定按钮点击事件
proxy_show_random = create_proxy(show_random)
document.getElementById("show-random-btn").addEventListener("click", proxy_show_random)
