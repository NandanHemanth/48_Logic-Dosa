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

        #adding the newly created block to the blockchain
        self.current_transactions = []
        self.chain.append(block)
        return block
    
    def new_transaction(self, sender,  recipient, amount):
        self.current_transactions.append.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })
        
        return self.last_block['index'] + 1
    
    
    @property
    def last_block(self):
        return self.chain[-1]
    
    
    #static method to hash each block and even check the proof of work
    @staticmethod
    def hash(block):
        
        #THe main Hashing of the data in each block is done here
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
    
    def proof_of_work(self, last_block):
        last_proof = last_block['proof']
        last_hash = self.hash(last_block)
        
        proof = 0
        while self.valid_proof(last_proof, proof, last_hash) is False:
            proof += 1
        return proof
    
    @staticmethod
    def valid_proof(last_proof, proof, last_hash):
        guess = f'{last_proof}{proof}{last_hash}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()

        # This is to Adjust your mining difficulty! The more zeroes, the more difficult
        return guess_hash[:4] == "0000"
    
    
# ---- Below here is the stuff needed for the idea of our blockchain becoming a "distributed ledger." ---- 

    
    
        
        
        
        
        
        


