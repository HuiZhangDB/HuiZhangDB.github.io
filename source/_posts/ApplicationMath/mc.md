---
title: Markov Chains & HMM
date: 2017-04-27 14:40:05
tags:
  - Math
categories:
  - 应用工程数学
---


会其意，知其形。
## Markov Chain
服从马尔可夫性（无记忆性）：当前状态只与前一个状态有关，与更往前的状态无关。

## HMM(Hiden Markov Model)
一个概率模型，用于描述系统隐性状态的转移和隐性状态的表现（输出）概率。

* 可见状态链
* 隐含状态链  
	{% asset_img chains.jpg %}
* 隐含状态数量  
* 隐含状态之间的转换概率(transition probability)  
	{% asset_img transition.jpg %}
* 隐含状态到可见状态的输出概率(emission probability)  
	{% asset_img emission.jpg %}  
	
### HMM能做什么，怎么做？
1. 估计(evaluation)  
	转换概率+输出概率 -> 可见状态出现的概率 （动态规划、forward algorithm）
2. 解码(decoding)  
	转换概率+输出概率+可见状态链 -> 隐含状态链 （极大似然、Viterbi algorithm）      
3. 学习(learning)  
	a. 有可见状态链和隐含状态链->HMM模型  
	b. 只有可见状态链->HMM模型