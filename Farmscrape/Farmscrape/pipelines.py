# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3
from web.models import Product

class FarmscrapePipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect("Farmitems.db")
        self.curr = self.conn.cursor()

        # self.conn = mysql.connector.connect(
        #     host='localost',
        #     user='root',
        #     passwd='nidhi85745',
        #     database='myquotes'
        # )


    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS item_tb""")
        self.curr.execute("""CREATE TABLE item_tb(
                            name text,
                            price text,
                            seller text
                            )""")

    def process_item(self, item, spider):
        # self.store_db(item)
        # item.save()
        print("??????????????????????????????????????????????")


        product = Product()
        product.name = item["name"]
        product.price = item["price"]
        product.seller = item["seller"]
        product.save()
        return item

    def store_db(self, item):
        item_length = 20
        for i in range(0, item_length):
            self.curr.execute("""insert into item_tb values (?,?,?)""", (
                item['name'][i],
                item['price'][i],
                item['seller'][i]
            ))

        self.conn.commit()
