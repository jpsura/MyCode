#!/usr/bin/env python3

#function push commands
def fruitsize(fruit):
    s_count = 0
    m_count = 0
    l_count = 0
    for size in fruit:
        if len(size) < 5:
            s_count += 1
        elif len(size) < 10:
            m_count += 1
        else:
            l_count += 1
    print({s_count}, {m_count}, {l_count})
stuff  = ['banana', 'apple', 'blueberries', 'nuts']
fruitsize(stuff)

