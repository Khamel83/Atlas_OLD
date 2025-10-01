# Excel heat map hack – FlowingData

**Source**: inputs/New Docs/html/flowingdata.com_2015_06_22_excel-heat-map-hack.html
**Type**: article
**Created**: 2025-08-25T02:53:53.719423

---

John Nelson from IDV Solutions explains how he uses [a Microsoft Excel hack to make geographic cell maps](https://www.linkedin.com/pulse/excel-map-hack-john-nelson).

> While pivoting data in Excel, it occurred to me that I could drag the latitude data into the row and the longitude data into the column. The result would be a 1980’s-Nintendo-looking chunky cell map (which, if I make the cells square, happens to be a pseudo-equirectangular projection). Low and behold.

It’s essentially four quick steps: Round latitude and longitude coordinates, bin them with a pivot table, reverse the order of said table, and color with conditions. You’ve got a rough overview map in a couple of minutes.

And once again, we see Excel provides flexibility to do some stuff. [Like Excel paintings](https://flowingdata.com/2013/09/16/excel-paintings/). [via @[philogb](http://twitter.com/philogb)]