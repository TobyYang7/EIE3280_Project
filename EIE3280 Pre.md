### EIE3280 Pre

In our previous research, we analyzed how various factors impact PageRank using real-world data from the online environment. We validated these findings in an actual network setting. By delving into the analysis of these factors, we can effectively optimize our website for improved performance.

3.36

We validated these findings in an actual network setting by build a personal photography homepage.

To increase PageRank, we fristly chose a powerful domain. This decision significantly boosts potential exposure. We also optimized by labeling keywords for specific searches. Crucially, link is the most important.

3.51

We use web crawling to gather the backlink data. There are about 400 pages, including their link information. On the right side of this image, we have visualized the data showing the interconnected network of these links. The bigger nodes indicate the more powerful domain.

4.14

These two pages are examples of the backlink page. I highlighted the link of my homepage. If you google "Chongqing Wallpaper" or simply search my name, you can easily find these two images.

4.27

So what had we done?

Firstly, our choice of powerful domain is important. 

You can see that our homepage's resources are referenced by these app or pages, like Notion, and Figma.

We also actively placed links on other websites and pointing back to my homepage. These two strategies significantly increase our homepage's PageRank. 

4.40

This graph shows the growth of external links to our homepage. Following my initial efforts to increase links earlier in the year, we witnessed a gradual rise in the link count. Notably, in May, we observed a substantial increase, we think it is some websites were crawling our content. The increased exposure from other websites crawling had led to a significant boost in link count. These findings show the success of our SEO strategy.

5.06

In further research, we analyzed the SEO strategy from the perspective of the game theory model.

In the read world,  SEO cannot happen in isolation. Due to the complexity of the online environment, PageRank is significantly influenced by various external factors. Our website is an example—other sites seeking to reference more links contribute to the benefit and increase of our pagerank.

Game theory in SEO helps us understand and predict competitor behaviors, leading to better strategy formulation. 

5.40

Now, let's revisit how Pagerank based on the alpha random walk is calculated.

1. **ϕuv​(x) (Potential or Probability)**: This symbol represents the probability of transition from two pages. If xi = 0, it means this page had deleted link i.

2. **qu​**: This symbol denotes the probability distribution on each vertex in graph G. Simply, we treated it as a uniform distribution.

In this model, the condition of reaching a Nash Equilibrium  is pi(1) greater than pi(x)

NE represents a scenario where all pages in the network have found their optimal linking configurations, and no single page can improve its ranking by changing its link structure. 

This is an example of  NE graph.

In our vision, while adjusting links can increase PageRank, it may also lead to unhealthy competition among pages. This equilibrium state reveals a point of stability in the network environment.

For example, if two pages are in direct competition, instinctively, removing links from the rival domain might temporarily boost one's own PageRank. However, the effects could be short-lived, potentially leading to a decrease in search results for both pages. 

Next, our work will involve collecting more data from a real network to simulate and validate our guess and model.

Therefore, in an ideal scenario, we believe that elevating keywords and improving content quality to achieve larger flow is more crucial than engaging in link adjustments, considering the potential pitfalls of direct competition.

That's all for our presentation, thank you

6.22


