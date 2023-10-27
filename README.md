# Can multiple-choice questions really be useful in detecting the abilities of LLMs?

<table align="center" style="border: 1px solid white;">
  <tr>
    <td style="border: 1px solid white;"><img src="figs/meetyou-logo.png" width="250"/></td>
    <td style="border: 1px solid white;"><img src="figs/Ethical-logo.jpg" width="60"/></td>
  </tr>
</table>

Multiple-choice questions (MCQs) are widely used in knowledge ability evaluation of large language models (LLMs) due to their simplicity in form and efficiency during inference. However, concerns have been raised regarding whether MCQs can really reveal the true ability of LLMs; specifically, since LLMs are usually utilized in knowledge-intensive scenarios where the models are required to do long-form generation (LFG), using MCQs for evaluation naturally introduces misalignment between what is tested and what is needed. 

## Background and Experimental Details
To investigate the preferences of LLMs to the order of options and the differences between MCQs and LFGQs, we conduct experiments on six evaluation benchmarks.
The evaluation benchmarks that we use are listed below:
| **Source**                                                                                   | **Language**   | **Size**      |
|----------------------------------------------------------------------------------------------|----------------|--------------:|
|[CARE-MI](https://github.com/Meetyou-AI-Lab/CARE-MI)   | ZH           |            1612 |
|[MLEC-QA](https://github.com/Judenpech/MLEC-QA)                                      | ZH            |            136236 |
|[MEDQA](https://arxiv.org/abs/2009.13081)                                                                                           | ZH/EN             |            61,097 |
|[M3KE](https://github.com/tjunlp-lab/M3KE)                 | ZH             |           20477  |
|[ARC](https://arxiv.org/abs/1803.05457)                 | EN             |           7,787 |
|[MATH]                                                | EN           |           300 |

The samples of the benchmarks we use can be found in `Datasets`.

The paper is currently on [arXiv](https://arxiv.org/abs/XXXXX). 

## Are LLMs sensitive to the order of candidate answers?
We first investigat the impact of the order of the candidate answers in the evaluation of LLM on MCQ datasets. We find that when the LLMs are presented with some options in different orders, they consistently show a strong preference for the same position, as illustrated in the following figure.

![order_preference](figs/order_preference_3.pdf)

## Multiple Choice Questions vs Long Form Generation Questions

**Authors**:

<div style="overflow: hidden;">
  <ul>
    <li>Wangyue Li  (<a href="mailto:alee90792@gmail.com">alee90792@gmail.com</a>)
    <li>Liangzhi Li (<a href="mailto:liliangzhi@xiaoyouzi.com">liliangzhi@xiaoyouzi.com</a>)
    <li>Tong Xiang  (<a href="mailto:xiangtong@xiaoyouzi.com">xiangtong@xiaoyouzi.com</a>)
    <li>Xiao Liu (<a href="mailto:liuxiao@xiaoyouzi.com">liuxiao@xiaoyouzi.com</a>)
    <li>Wei Deng (<a href="mailto:dengwei@swufe.edu.cn">dengwei@swufe.edu.cn</a>)
    <li>Noa Garcia  (<a href="mailto:noagarcia@ids.osaka-u.ac.jp">noagarcia@ids.osaka-u.ac.jp</a>)<sup>*</sup>
  </ul>
</div>

<sup>*</sup>Corresponding author.
