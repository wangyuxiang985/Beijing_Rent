### Rent Crawler 租房爬虫

参考学习：https://github.com/waylife/RentCrawer

python2.7

安装Requests以及BeautifulSoup库

**运行步骤**
1. 【必须】配置config.ini中key_search_word_list字段为需要搜索的地名，例：大屯路,立水桥
2. 【必须】配置config.ini中custom_black_list字段为不想搜到的内容,不配置则为空
3. 【必须】配置config.ini中start_time字段为帖子开始时间
4. 【可选】其他配置可可选择进行配置，删除rentdata.db3以及rentdata_result.html和rentdata_result.xls文件，如果不希望本次结果与上次混合在一起，可以删除相关文件
5. 【必须】运行RentCrawler.py文件
6.  结果文件存储在result目录下
