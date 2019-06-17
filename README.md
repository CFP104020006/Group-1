# **Group-1**

## **Gel Permeation**

## **I. Members**

- 余宇恒 (104020006)

- 黃偉誌 (104021230)

- 許孟楷 (104022140)

- 李偉志 (104020010)

## **II. Goal**

1. Create a simple classical model for gel permeation chromatography

## **III. Theoretical Background**

大顆粒子與小顆粒子通過多孔材料所需時間不同

分析一個未知混合物的比例與成分

![pic](./gel.jpg)


## **IV. Expected Result**

畫出落下數量vs(時間or路徑)關係圖

![pic](./result.jpg)


## **V. Tasks**

- 設置多孔材料的邊界、障礙物大小、排列、偵測器位置(許孟楷)

- 設置高分子材料初速、位置、環境重力加速度、彈性碰撞(余宇恒、李偉志)

- 畫時間、路徑對位置圖，做成動畫(黃偉誌)

## **VI. Program Setup**

模組:pygame, math, Matplotlib, time, Numpy, random, scipy.optimize, sys

藍色方塊排列模擬多孔材料的排列

橘色球模擬高分子材料

設置均勻向下重力場，並將碰撞情形設為完全彈性碰撞

![pic](./permeation1.PNG)

使用class建立球與方塊，每個物件可以有自己的屬性(attribute)以及方法(method)

![pic](./class.png)

物體移動: 用一個迴圈不斷更新物件狀態以及畫面，達成動畫的效果

![pic](./move.png)

碰狀問題: 抖動、膠著在一起的情形，可以在判定碰撞的時候多加一個兩顆碰撞的球速度需要是讓他們分開的條件解決

![pic](./collision.png)

畫時間對路徑，個數的關係圖。球走了多少時間，多少距離

![pic](./draw.png)
![pic](./draw1.png)


## **VII.Results**
R = 橘色球半徑，x軸為時間

![pic](./result1.png)

將上圖峰值發生位置與R拿去做fitting，可以得到漂亮的exponential關係
![pic](./peak.png)

改變方塊高度，則沒什麼影響

![pic](./H.png)

## **VIII.Reference**
-https://en.wikipedia.org/wiki/Elastic_collision

-https://en.wikipedia.org/wiki/Gel_permeation_chromatography

-https://www.agilent.com/cs/library/primers/Public/5990-6969EN%20GPC%20SEC%20Chrom%20Guide.pdf
