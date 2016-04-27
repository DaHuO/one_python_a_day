# -*- coding: UTF-8 -*-

import redis


def saveToRedis():
    file_in = open('activation_code', 'r')
    r = redis.Redis(host = 'localhost',
                    port = 6379,
                    password = '')
    activation_code = {}
    count = 0
    for line in file_in:
        activation_code[count] = line[:-1]
        count += 1
    r.hmset('activation_code', activation_code)
    file_in.close()

if __name__ == "__main__":
    saveToRedis()
