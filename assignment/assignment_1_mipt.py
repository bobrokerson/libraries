#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 16:49:11 2022

@author: jimmy
"""
import re
from numpy import zeros, dot, savetxt
from numpy.linalg import norm
 
def cosine_distance(u, v):
    return 1.0 - (dot(u, v) / (norm(u) * norm(v)))
 
if __name__ == "__main__":
    with open("sentences.txt") as fin:
        lines = sum(1 for _ in fin)
        fin.seek(0)
        words = {}
        lcount, wcount = 0, 0
        for line in fin:
            p = re.compile(r"[^a-z]+")
            tokens = p.split(line.lower())
            tokens.pop()
            for token in tokens:
               
                if token not in words:
                    words[token] = {"i": wcount, "o": [0] * lines}
                    wcount += 1
                elif words[token]["o"][lcount] != 0:
                    continue
                
                words[token]["o"][lcount] = tokens.count(token)    
            lcount += 1
        
        arr = zeros((lines, len(words)))
       
        for word in words:
            i, j = 0, words[word]["i"]
            for occ in words[word]["o"]:
                arr[i, j] = occ
                i += 1
    
        st = [] 
        u = arr[0,] 
        for i in range(1, lines):
            v = arr[i,]
            st.append({"index": i, "distance": cosine_distance(u, v)})    
        
        st.sort(key=lambda x: x["distance"])
        print("The 1st closest sentence #%d with a cosine distance of %.2f.\n"\
        "The 2nd closest sentence  #%d with a cosine distance of %.2f." % (
            st[0]["index"], st[0]["distance"], st[1]["index"], st[1]["distance"]))
 
