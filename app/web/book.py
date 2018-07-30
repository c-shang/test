# coding:utf8
# created at 2018/7/19.
import json

from flask import jsonify,request
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook

from app.view_models.book import BookCollection
from . import web
from app.forms.book import SearchForm
from app.view_models.book import BookViewModel

@web.route('/book/search')
def search():
    form = SearchForm(request.args)
    books = BookCollection()

    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        yushu_book = YuShuBook()

        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)
            # result = YuShuBook.search_by_isbn(q)
            # result = BookViewModel.package_single(result,q)
        else:
            yushu_book.search_by_keyword(q,page)
            # result = YuShuBook.search_by_keyword(q,page)
            # result = BookViewModel.package_collection(result,q)

        books.fill(yushu_book,q)
        # return jsonify(books)
        return json.dumps(books,default=lambda o: o.__dict__)
    else:
        return jsonify(form.errors)
    # return json.dumps(result),200,{'content-type':'application/json'}

