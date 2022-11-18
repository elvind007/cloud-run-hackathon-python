import os
import logging
import random
from flask import Flask, request

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
logger = logging.getLogger(__name__)

app = Flask(__name__)
moves = ['F', 'T', 'L', 'R']

@app.route("/", methods=['GET'])
def index():
    return "Let the battle begin!"

@app.route("/", methods=['POST'])
def move():
    request.get_data()
    logger.info(request.json)

    info=request.get_json()
    self_url=info["_links"]["self"]["href"]
    x_lim=info["arena"]["dims"][0]
    y_lim=info["arena"]["dims"][1]
    x_pos=info["arena"]["state"][self_url]["x"]
    y_pos=info["arena"]["state"][self_url]["y"]
    my_dir=info["arena"]["state"][self_url]["direction"]
    hit=info["arena"]["state"][self_url]["wasHit"]
    all_x=[]
    all_y=[]
    x_dir=[]
    y_dir=[]
    for i in info["arena"]["state"].values():
        if i["x"]==x_pos:
            if (i["y"]-y_pos)<=3 and (i["y"]-y_pos)>=-3 and i["y"]!=y_pos:
                #all_x.append( i["x"])
                all_y.append(i["y"]-y_pos)
                # y_dir.append(i["direction"])
        elif i["y"]==y_pos:
            if (i["x"]-x_pos<=3) and (i["x"]-x_pos)>=-3 and i["x"]!=x_pos:
                all_x.append(x_pos-i["x"])
                #all_y.append(i["y"])
                # x_dir.append(i["direction"])
    # (x_dir,y_dir)=relative_direction(all_x,all_y,x_dir,y_dir)
    for i in all_y:
        if i<0 and my_dir=="N":
            return moves[1]
        elif i>0 and my_dir=="S":
            return moves[1]
    for i in all_x:
        if i<0 and my_dir=="E":
            return moves[1]
        elif i>0 and my_dir=="W":
            return moves[1]
    return moves[can_move(x_pos,y_pos,x_lim-1,y_lim-1,my_dir)]
    # TODO add your implementation here to replace the random response
    
    # return moves[random.randrange(len(moves))]

def can_move(x_pos,y_pos,x_lim,y_lim,dir):
    if x_pos<=0 and dir=="W":
        if y_pos!=0:
            return 3
        else:
            return 2
    elif x_pos>=x_lim and dir=="E":
        if y_pos==y_lim:
            return 2
        else:
            return 3
    elif y_pos<=0 and dir=="N":
        if x_pos>=x_lim:
            return 2
        else:
            return 3
    elif y_pos>=y_lim and dir=="S":
        if x_pos<=0:
            return 2
        else:
            return 3
    return 0

if __name__ == "__main__":
  app.run(debug=False,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))