---
title: 实验分析中的假设检验
date: 2018-08-30 16:41:00
tags:
  - experiment
  - statistics
categories:
---

<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>

我们经常会设计实验来检验某种工具的可用性或者使用效果，在实验过后，要对实验所得到的数据进行分析。在实验数据分析的过程中就往往要用到假设检验。我们可以使用假设检验来反映样本均值之间的差别是否可以推广到总体中去（计算从样本统计结果推论至总体时犯错的概率）。

<!--More-->

> 例如，我们抽样10个用户来做实验，他们不使用工具完成一个任务的时间均值为\\(\overline{X_1}\\)，在使用某个工具后完成该任务的时间均值为\\(\overline{X_2}\\)，那么这10个用户在使用工具前后所花的时间差为\\(d = \overline{X_1} - \overline{X_2} < 0\\)。这说明对于这10个用户，该工具的确提高了他们的效率。但我们可不可以说对于所有用户而言，这种差异还存在呢？假设检验可以帮我们回答这个问题。

假设检验中首先要提出统计假设，一般同时提出两个完全相反的假设（零假设\\(H_0\\)和备择假设\\(H_a\\)），其中备择假设是我们根据样本资料想要得到支持的假设（通过拒绝零假设）。

对于总体参数\\(\theta\\)的假设有三种情况：

1. \\(H_0: \theta \ge \theta_0\\), \\(H_a: \theta < \theta_0\\)
2. \\(H_0: \theta \le \theta_0\\), \\(H_a: \theta > \theta_0\\)
3. \\(H_0: \theta = \theta_0\\), \\(H_a: \theta \ne \theta_0\\)

其中 1 2 为单边检验(one-tail)， 3 为双边检验(two-tail)。

## T-Test
t检验可以在样本总体为正态分布的前提下，用于检验某个样本的期望是否为某一实数，或者比较两个样本的期望值之差是否为某一实数。

### 双体检验
双体检验可以用于比较两个总体的均值或者比较两种处理的效应，可以分为：

* 配对双体检验
* 非配对双体检验

在前面的例子中，就可以用配对双体检验来证明，在一特定显著度下，是否使用该工具完成任务的时间有显著差异（双边检验）或者直接证明该工具的确可以提高效率（单边检验）。但要特别注意的是，单一情况下的t检验只能证明是否有足够的理由来拒绝零假设，也就是说不管得到怎样的结果，t检验都是不能接受零假设的（只能说没有充分的理由来拒绝原假设）。

> 这种陷阱可能出现在医药公司中，试图说明更改原材料后的效果不变性。。

## Equivalence-Test
其实，想要证明某种改变对样本表现完全不会带来影响是不可能的，除非样本量是无限的。。但我们可以这种影响不会超过某个区间。例如，我们可以证明，这个改变对样本表现的影响程度不会超过0.4。那么问题就变成了要同时检验两个单边假设：

 $$H_0: \quad \theta \le 0.4 \\ or \\ \theta \ge 0.4 \\\\  H_a: \quad 0.4 < \theta < 0.4$$
 
 
例如，拿[这里的数据](http://blog.minitab.com/blog/statistics-and-quality-data-analysis/equivalence-testing-for-quality-analysis-part-ii-what-difference-does-the-difference-make)来举例：

> Null hypothesis:         Difference ≤ -0.42 or Difference ≥ 0.42  
> Alternative hypothesis:  -0.42 < Difference < 0.42  
> α level:                 0.05  
>
> Null Hypothesis     DF  T-Value  P-Value  
> Difference ≤ -0.42  99   8.3290    0.000  
> Difference ≥ 0.42   99  -4.1046    0.000  
 
这里的结果中，两个P值(0.000)都小于0.05，可以认为等价假设成立。 
