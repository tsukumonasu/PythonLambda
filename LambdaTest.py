#!/usr/bin/env python
# -*- coding: utf-8 -*-

fib = lambda n: n if n < 2 else fib(n-1) + fib(n-2)
for i in range(1,11):
    print "fibo引数%d=%d" % (i, fib(i))

# 読みやすく
for i in range(1,31):
    print "FizzBuzz引数%d=%s" % (i, (lambda g:g(3,'Fizz') + g(5,'Buzz') or i)(lambda j,s:''if i%j else s))