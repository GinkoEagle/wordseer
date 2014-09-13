import json

from flask import abort
from flask import request
from flask.json import jsonify
from flask.views import View

from app import app
from app import db
from .. import wordseer
from .. import helpers


class WordFrequenciesView(View):
    """Utilities for fetching word counts over a dimension of metadata"""
    def __init__(self, operation):
        """deal with all the variables"""
        # for use in dispatch_request
        self.operation = operation
        
    #===========================================================================
    # endpoint methods
    #===========================================================================
    
    def bar_chart(self):
        # php equivalent: word-frequencies/bar-charts.php
        pass
    
    def dispatch_request(self):
        operations = {
            "bar_chart": self.bar_chart,
        }

        result = operations[self.operation](self)
        return jsonify(result)
    
wordseer.add_url_rule("/api/word_frequencies/bar_chart",
    view_func=WordFrequenciesView.as_view("word_freq_bar_chart", "bar_chart"))