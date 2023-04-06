#!/usr/bin/env python

#importing the necessary libraries - hashing(sha256), time, urlparser, json
import hashlib
import json
import time
from urllib.parse import urlparse
from uuid import uuid4

import requests
from flask import Flask, jsonify, request


#defining the blockchain for the cryptocurrency - DosaCoin
class Blockchain:
    def __init__(self):
        self.current_transactions = []
        self.chain = []
        self.nodes = set()

        #Creating the Genesis BLock - initial block with previous hash defined with POF
        self.new_block(previous_hash="1", proof="200")

    def new_block(self, proof, previous_hash):

        #Each BLock consists of 5 fields which define a unique block
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
            'proof': proof
        }

        self.current_transactions = []
        self.chain.append(block)
        return block
    
    def new_transaction(self,)

