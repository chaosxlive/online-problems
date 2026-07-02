# Leetcode

## 平台連結

[Leetcode 官方網站](https://leetcode.com/)

## 總覽

| No.  | Problem Title                                        | C++ | Python3 | Go  | TS  | JS  | Java | Notes             |
| :--: | :--------------------------------------------------- | :-: | :-----: | :-: | :-: | :-: | :--: | ----------------- |
| 0045 | Jump Game II                                         |  V  |    V    |  V  |  V  |  V  |  V   |                   |
| 0380 | Insert Delete GetRandom O(1)                         |     |    V    |     |     |     |      |                   |
| 1189 | Maximum Number of Balloons                           |     |    V    |  V  |     |     |      |                   |
| 1344 | Angle Between Hands of a Clock                       |  V  |    V    |  V  |  V  |  V  |  V   |                   |
| 1358 | Number of Substrings Containing All Three Characters |     |    V    |     |     |     |      |                   |
| 1732 | Find the Highest Altitude                            |  V  |    V    |  V  |  V  |  V  |  V   |                   |
| 1768 | Merge Strings Alternately                            |     |    V    |     |  V  |  V  |      |                   |
| 1833 | Maximum Ice Cream Bars                               |     |    V    |  V  |     |     |      |                   |
| 1840 | Maximum Building Height                              |     |    V    |  V  |     |     |      | [#1840](#no-1840) |
| 1846 | Maximum Element After Decreasing and Rearranging     |     |    V    |     |     |     |      |                   |
| 1967 | Number of Strings That Appear as Substrings in Word  |     |    V    |     |     |     |      | [#1967](#no-1967) |
| 2095 | Delete the Middle Node of a Linked List              |     |    V    |  V  |     |     |      |                   |
| 2130 | Maximum Twin Sum of a Linked List                    |     |    V    |     |     |     |      |                   |
| 2812 | Find the Safest Path in a Grid                       |     |    V    |     |     |     |      |                   |
| 3020 | Find the Maximum Number of Elements in Subset        |     |    V    |  V  |     |     |      |                   |
| 3286 | Find a Safe Walk Through a Grid                      |     |    V    |     |     |     |      |                   |
| 3612 | Process String with Special Operations I             |     |    V    |     |     |     |      |                   |
| 3614 | Process String with Special Operations II            |     |    V    |  V  |     |     |      |                   |
| 3699 | Number of ZigZag Arrays I                            |     |    V    |     |     |     |      |                   |
| 3700 | Number of ZigZag Arrays II                           |     |    V    |  V  |     |     |      |                   |
| 3737 | Count Subarrays With Majority Element I              |     |    V    |     |     |     |      |                   |
| 3739 | Count Subarrays With Majority Element II             |     |    V    |     |     |     |      |                   |
| 3838 | Weighted Word Mapping                                |     |    V    |     |     |     |      |                   |

### 備註

#### No. 1840

> **Maximum Building Height**

- Solve 1: Min Heap

  利用 Min Heap 來依序找最小的，並更新左右兩側節點的限制值，與之相比更大的必定要滿足更小的點的需求。

- Solve 2: Greedy

  利用 Greedy 的限制方式，每個節點依序分別往左、右上畫斜線，剛好切到的部分就是其他節點可以達到的最大高度，最後對所有區間取最大。

#### No. 1967

> **Number of Strings That Appear as Substrings in Word**

- Solve 1: String Matching

  暴力破解的直接檢查每個 pattern 是否是 word 的子字串。

  因為這題是 `Easy` ，所以暴力破解是可行的，甚至可能反而表現最好。

- Solve 2: Aho–Corasick Algorithm

  使用 `AC 自動機` 來一次性檢查所有 pattern 是否是 word 的子字串。

  同樣的，因為這題是 `Easy` ，數量級太小了，沒辦法體現他的優勢，所以表現可能會差一點。

  [Aho–Corasick Algorithm - Wiki](https://zh.wikipedia.org/zh-tw/AC%E8%87%AA%E5%8A%A8%E6%9C%BA%E7%AE%97%E6%B3%95)
