
# Copyright 2020 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import logging
import random
from flask import Flask, request


app = Flask(__name__)
moves = ['F', 'T', 'L', 'R']

@app.route("/", methods=['GET'])
def index():
    return "Let the battle begin!"

@app.route("/", methods=['POST'])
def move():
    request.get_data()
        
    dims = request.json['arena']['dims']
    
    m_state = request.json['arena']['state']['https://cloud-run-hackathon-python-z7wwhw7czq-uc.a.run.app']
    a_state = request.json['arena']['state']


    if m_state['x'] == (dims[0] - 1) and m_state['y'] == 0 :
        for key, value in a_state.items():
            if key != 'https://cloud-run-hackathon-python-z7wwhw7czq-uc.a.run.app':
                if m_state['x'] == value['x'] and m_state['y'] >= (value['y'] - 3):
                    if m_state['direction'] == 'S':
                        return 'T'
                    elif m_state['direction'] == 'E' or m_state['direction'] == 'N':
                        return 'R'
                    else:
                        return 'L'
                elif m_state['x'] <= (value['x'] + 3) and m_state['y'] == value['y']:
                    if m_state['direction'] == 'W':
                        return 'T'
                    elif m_state['direction'] == 'N' or m_state['direction'] == 'E':
                        return 'L'
                    else:
                        return 'R'
    
    if m_state['y'] > 0:
        if m_state['direction'] == 'N' :
            for key, value in a_state.items():
                if key != 'https://cloud-run-hackathon-python-z7wwhw7czq-uc.a.run.app':
                    if m_state['x'] == value['x'] and m_state['y'] <= (value['y'] + 3):
                        return 'T'
            return 'F'
        elif m_state['direction'] == 'E' or m_state['direction'] == 'S':
            return 'L'
        elif m_state['direction'] == 'W' :
            return 'R'

    if  m_state['x'] < (dims[0] - 1) :
        if m_state['direction'] == 'E' :
            for key, value in a_state.items():
                if key != 'https://cloud-run-hackathon-python-z7wwhw7czq-uc.a.run.app':
                    if m_state['x'] >= (value['x'] - 3) and m_state['y'] == value['y']:
                        return 'T'
            return 'F'
        elif m_state['direction'] == 'W' or m_state['direction'] == 'N':
            return 'R'
        elif m_state['direction'] == 'S' :
            return 'L'

    return 'T'

if __name__ == "__main__":
  app.run(debug=False,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
  
