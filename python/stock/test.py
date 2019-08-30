#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re

if __name__ == '__main__':
    content = 'Hello 1234567 World_This is a Regex Demo'
    result = re.match('.*?(\d+).*Demo$', content)
    print(result.group(1))

    text = '<td class="pad01"><a class="a100" href="http://app.finance.ifeng.com/custom/mystock_opt.php?type=add&amp;code=sh600031" target="_blank" title="添加我的自选股"></a><a href="http://app.finance.ifeng.com/report/search.php?yb_search_type=stock&amp;code=600031" target="_blank">三一重工</a></td>'
    a=re.match('.*code=?(\d+).*',text)
    print(a.group(1))